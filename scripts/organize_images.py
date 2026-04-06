#!/usr/bin/env python3
"""
Organize local images under assets/img/<caller-md-dir>/...

Rules implemented:
- Look for Obsidian embeds: ![[something.png]] (also supports ![[path/to.png|alias]])
- Look for Markdown images: ![alt](path) where path is not http(s)
- For each referenced local image, place it under:
    assets/img/<relative_dir_of_md>/<original_filename>
  Example: career/courses/foo.md -> assets/img/career/courses/<file>
- Update the Markdown to reference the new relative path (standard Markdown image syntax).

Notes:
- If the same source image is referenced from multiple notes in different dirs,
  we move it to the first destination and copy it to the others.
"""

from __future__ import annotations

import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


RE_OBSIDIAN_EMBED = re.compile(r"!\[\[([^\]]+?)\]\]")
RE_MD_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


@dataclass(frozen=True)
class ImageRef:
    md_path: Path
    raw: str  # full match
    kind: str  # "obsidian" | "markdown"
    alt: str | None
    target: str  # path inside embed/link, before any |alias


def is_remote_url(p: str) -> bool:
    p = p.strip()
    return p.startswith("http://") or p.startswith("https://")


def normalize_obsidian_target(t: str) -> str:
    # Split alias: "file.png|Some alias" -> "file.png"
    return t.split("|", 1)[0].strip()


def iter_md_files(root: Path) -> Iterable[Path]:
    for p in root.rglob("*.md"):
        # Do not touch the /gitignore folder.
        try:
            rel = p.relative_to(root)
        except ValueError:
            continue
        if rel.parts and rel.parts[0] == "gitignore":
            continue
        yield p


def find_image_refs(md_path: Path) -> list[ImageRef]:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    refs: list[ImageRef] = []

    for m in RE_OBSIDIAN_EMBED.finditer(text):
        target = normalize_obsidian_target(m.group(1))
        if Path(target).suffix.lower() not in IMAGE_EXTS:
            continue
        refs.append(
            ImageRef(
                md_path=md_path,
                raw=m.group(0),
                kind="obsidian",
                alt=None,
                target=target,
            )
        )

    for m in RE_MD_IMAGE.finditer(text):
        alt = m.group(1)
        target = m.group(2).strip()
        if is_remote_url(target):
            continue
        if Path(target).suffix.lower() not in IMAGE_EXTS:
            # Sometimes people put YouTube links as "images"; we leave those alone.
            continue
        refs.append(
            ImageRef(
                md_path=md_path,
                raw=m.group(0),
                kind="markdown",
                alt=alt,
                target=target,
            )
        )

    return refs


def resolve_source_image(root: Path, md_path: Path, target: str) -> Path | None:
    """
    Resolve an image reference target to an actual file on disk.

    Strategy:
    1) If target is a path and exists relative to the md file, use that.
    2) If exists under assets/img/<filename>, use that (common vault attachment pattern).
    3) If target is already under assets/img/... and exists, use that.
    """
    # Target might contain URL-encoded spaces etc; we keep literal.
    t = target.strip()
    t_path = Path(t)

    # Relative to md file
    candidate = (md_path.parent / t_path).resolve()
    if candidate.exists() and candidate.is_file():
        return candidate

    # Relative to repo root
    candidate = (root / t_path).resolve()
    if candidate.exists() and candidate.is_file():
        return candidate

    # Common: just the filename, stored in assets/img
    candidate = (root / "assets" / "img" / t_path.name).resolve()
    if candidate.exists() and candidate.is_file():
        return candidate

    return None


def rel_md_dir(root: Path, md_path: Path) -> Path:
    rel = md_path.relative_to(root)
    # caller directory, relative to root
    return rel.parent


def ensure_parent(p: Path) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)


def make_rel_link(from_md: Path, to_file: Path) -> str:
    rel = os.path.relpath(to_file, start=from_md.parent)
    # Use forward slashes for Markdown links across platforms.
    return rel.replace(os.sep, "/")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    img_root = root / "assets" / "img"
    if not img_root.exists():
        print("assets/img not found; nothing to do.")
        return 0

    # Collect all refs first to detect multi-use.
    all_refs: list[ImageRef] = []
    for md in iter_md_files(root):
        all_refs.extend(find_image_refs(md))

    by_source_name: dict[str, list[ImageRef]] = {}
    for r in all_refs:
        by_source_name.setdefault(Path(r.target).name, []).append(r)

    # Track where the "canonical" moved file ended up for multi-use.
    canonical_path_by_name: dict[str, Path] = {}

    # Update markdown files in-memory, then write back.
    text_by_md: dict[Path, str] = {}
    for md in iter_md_files(root):
        text_by_md[md] = md.read_text(encoding="utf-8", errors="replace")

    missing: list[tuple[Path, str]] = []

    # Process refs, stable order by md path then appearance.
    for r in sorted(all_refs, key=lambda x: (str(x.md_path), x.md_path.stat().st_mtime)):
        md_dir = rel_md_dir(root, r.md_path)
        src = resolve_source_image(root, r.md_path, r.target)
        if src is None:
            missing.append((r.md_path, r.target))
            continue

        name = src.name
        dest = img_root / md_dir / name
        ensure_parent(dest)

        # Move/copy strategy for multi-use images.
        refs_for_name = by_source_name.get(name, [])
        if len(refs_for_name) > 1:
            if name not in canonical_path_by_name:
                # First time: move into first destination
                if src.resolve() != dest.resolve():
                    if dest.exists():
                        # Prefer not to overwrite.
                        pass
                    else:
                        shutil.move(str(src), str(dest))
                canonical_path_by_name[name] = dest
            else:
                # Subsequent: copy from canonical into this destination if needed
                canon = canonical_path_by_name[name]
                if dest.resolve() != canon.resolve():
                    if not dest.exists():
                        shutil.copy2(str(canon), str(dest))
        else:
            # Single-use: just move it if needed
            if src.resolve() != dest.resolve():
                if dest.exists():
                    # Avoid overwrite; keep source where it is and just link to it.
                    dest = src
                else:
                    shutil.move(str(src), str(dest))

        rel_link = make_rel_link(r.md_path, dest)
        alt = r.alt if (r.kind == "markdown" and r.alt is not None) else Path(name).stem
        replacement = f"![{alt}]({rel_link})"

        # Replace only the exact raw match occurrence(s).
        text_by_md[r.md_path] = text_by_md[r.md_path].replace(r.raw, replacement)

    # Write back
    for md, text in text_by_md.items():
        md.write_text(text, encoding="utf-8")

    if missing:
        print("Missing image targets (left unchanged):")
        for md, target in missing:
            print(f"- {md.relative_to(root)} -> {target}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


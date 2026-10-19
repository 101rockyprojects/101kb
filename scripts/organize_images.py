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
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


RE_OBSIDIAN_EMBED = re.compile(r"!\[\[([^\]]+?)\]\]")
RE_MD_IMAGE = re.compile(r"!\[([^\]]*)\]\(((?:[^()]|\([^()]*\))+)\)")

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


def kebab_case(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = "".join(char for char in normalized if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", "-", ascii_value.casefold()).strip("-") or "image"


def rename_pasted_images(root: Path) -> None:
    root = root.resolve()
    img_root = root / "assets" / "img"
    pasted_images = sorted(
        (
            path.resolve()
            for path in img_root.rglob("*")
            if path.is_file()
            and path.name.casefold().startswith("pasted")
            and path.suffix.casefold() in IMAGE_EXTS
        ),
        key=lambda path: str(path.relative_to(root)).casefold(),
    )
    markdown_files = sorted(
        iter_md_files(root), key=lambda path: str(path.relative_to(root)).casefold()
    )

    refs_by_image: dict[Path, list[ImageRef]] = {}
    for md_path in markdown_files:
        for ref in find_image_refs(md_path):
            source = resolve_source_image(root, md_path, ref.target)
            if source is not None and source.resolve() in pasted_images:
                refs_by_image.setdefault(source.resolve(), []).append(ref)

    unresolved = [image for image in pasted_images if image not in refs_by_image]
    primary_by_image: dict[Path, Path] = {}
    images_by_primary: dict[Path, list[Path]] = {}
    for image, refs in refs_by_image.items():
        refs.sort(
            key=lambda ref: (
                str(ref.md_path.relative_to(root)).casefold(),
                ref.md_path.read_text(encoding="utf-8", errors="replace").find(ref.raw),
            )
        )
        primary = refs[0].md_path
        primary_by_image[image] = primary
        images_by_primary.setdefault(primary, []).append(image)

    planned_destinations: dict[Path, Path] = {}
    reserved_destinations: set[Path] = set()
    referenced_images = set(refs_by_image)
    for primary, images in images_by_primary.items():
        images.sort(key=lambda image: str(image.relative_to(root)).casefold())
        base = kebab_case(primary.stem)
        for index, image in enumerate(images, start=1):
            stem = f"{base}({index})" if len(images) > 1 else base
            destination = image.with_name(f"{stem}{image.suffix}")
            suffix_index = 1
            while (
                destination in reserved_destinations
                or (destination.exists() and destination.resolve() not in referenced_images)
            ):
                destination = image.with_name(f"{base}({suffix_index}){image.suffix}")
                suffix_index += 1
            planned_destinations[image] = destination
            reserved_destinations.add(destination)

    text_by_md: dict[Path, str] = {}
    for image, refs in refs_by_image.items():
        destination = planned_destinations[image]
        if destination == image:
            continue
        for ref in refs:
            text = text_by_md.setdefault(
                ref.md_path,
                ref.md_path.read_text(encoding="utf-8", errors="replace"),
            )
            link = make_rel_link(ref.md_path, destination)
            if ref.kind == "obsidian":
                inner = ref.raw[3:-2]
                alias = f"|{inner.split('|', 1)[1]}" if "|" in inner else ""
                replacement = f"![[{link}{alias}]]"
            else:
                replacement = f"![{ref.alt or ''}]({link})"
            text_by_md[ref.md_path] = text.replace(ref.raw, replacement)

    for md_path, text in text_by_md.items():
        md_path.write_text(text, encoding="utf-8")

    temporary_paths: dict[Path, Path] = {}
    for image, destination in planned_destinations.items():
        if image == destination:
            continue
        temporary = image.with_name(f".{image.name}.organize-images-tmp")
        while temporary.exists() or temporary in reserved_destinations:
            temporary = temporary.with_name(f".{temporary.name}")
        image.rename(temporary)
        temporary_paths[image] = temporary

    for image, temporary in temporary_paths.items():
        destination = planned_destinations[image]
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary.rename(destination)
        print(f"{image.relative_to(root)} -> {destination.relative_to(root)} (Renamed)")

    for image in unresolved:
        print(f"UNRESOLVED: {image.relative_to(root)} (no Markdown reference found)")


def organize_images(root: Path) -> int:
    img_root = root / "assets" / "img"
    if not img_root.exists():
        print("assets/img not found; nothing to do.")
        return 0

    # Collect all refs first to detect multi-use.
    all_refs: list[ImageRef] = []
    for md in iter_md_files(root):
        all_refs.extend(find_image_refs(md))

    source_by_ref: dict[ImageRef, Path] = {}
    missing: list[tuple[Path, str]] = []
    for r in all_refs:
        src = resolve_source_image(root, r.md_path, r.target)
        if src is None:
            missing.append((r.md_path, r.target))
            continue
        source_by_ref[r] = src.resolve()

    refs_by_source: dict[Path, list[ImageRef]] = {}
    for r in all_refs:
        src = source_by_ref.get(r)
        if src is not None:
            refs_by_source.setdefault(src, []).append(r)

    canonical_path_by_source: dict[Path, Path] = {}
    destination_by_source_and_dir: dict[tuple[Path, Path], Path] = {}

    # Update markdown files in-memory, then write back.
    text_by_md: dict[Path, str] = {}
    for md in iter_md_files(root):
        text_by_md[md] = md.read_text(encoding="utf-8", errors="replace")

    # Process refs, stable order by md path then appearance.
    for r in sorted(all_refs, key=lambda x: (str(x.md_path), x.md_path.stat().st_mtime)):
        md_dir = rel_md_dir(root, r.md_path)
        src = source_by_ref.get(r)
        if src is None:
            continue

        name = src.name
        dest = img_root / md_dir / name
        ensure_parent(dest)

        # Move/copy strategy for multi-use images.
        refs_for_source = refs_by_source[src]
        if len(refs_for_source) > 1:
            destination_key = (src, md_dir)
            if src not in canonical_path_by_source:
                # First time: move into first destination
                if src != dest.resolve():
                    if dest.exists():
                        canonical_path_by_source[src] = src
                        dest = src
                    else:
                        shutil.move(str(src), str(dest))
                        canonical_path_by_source[src] = dest
                else:
                    canonical_path_by_source[src] = dest
                destination_by_source_and_dir[destination_key] = dest
            else:
                # Subsequent: copy from canonical into this destination if needed
                known_destination = destination_by_source_and_dir.get(destination_key)
                if known_destination is not None:
                    dest = known_destination
                else:
                    canon = canonical_path_by_source[src]
                    if dest.resolve() == canon.resolve():
                        destination_by_source_and_dir[destination_key] = dest
                    elif not dest.exists():
                        shutil.copy2(str(canon), str(dest))
                        destination_by_source_and_dir[destination_key] = dest
                    else:
                        dest = canon
                        destination_by_source_and_dir[destination_key] = dest
        elif src != dest.resolve():
            # Single-use: just move it if needed
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


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    result = organize_images(root)
    rename_pasted_images(root)
    return result


if __name__ == "__main__":
    raise SystemExit(main())

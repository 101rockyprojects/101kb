# AGENTS.md

Obsidian knowledge vault (Markdown + images), maintained with Git. Not a software project: no build, test, or lint toolchain.

## Before any push (MUST)

```bash
python3 scripts/organize_images.py
```

Moves referenced local images under `assets/img/<relative dir of the referencing note>/`, rewrites Markdown links, and renames referenced `Pasted*` images to kebab-case note names (numbered when a note has several). Stdlib only, idempotent. Commit any changes it makes before pushing.

## Layout and conventions

- Top-level folders: `concepts/`, `tools/`, `career/`, `projects/`, `scripts/`, `snippets/`, `resources/`, `assets/`. Each has a `WH!.md` index — update it when adding content.
- Navigation is wikilinks (`[[Note Name]]`), not deep hierarchies. Notes are a mix of Spanish and English; do not translate or "fix" language.
- Images: `assets/img/<caller-note-dir>/...`, referenced with standard relative Markdown syntax (`![alt](../../assets/img/...)`). Obsidian embeds `![[img.png]]` get converted by the script above.
- External links often carry OpenGraph cards via ` ```cardlink ` blocks (Auto Card Link plugin) — leave them as-is.
- Commit style: Conventional Commits (`docs(concepts): ...`, `chore(assets): ...`).

## Git gotchas

- `/gitignore/` is an intentional private folder (untracked personal notes, e.g. monthly budgets). Never force-add it.
- Never commit: `.ssh/`, `.obsidian/`, `.copilot/`, `copilot/`, `Agents/`, `.opencode/`, `*secrets`, `*.env`.
- Remote `origin` uses SSH host alias `github-101kb` (local `~/.ssh/config`, not in repo).
- `.opencode/` holds OpenCode skills for this vault (`obsidian-markdown`, `obsidian-cli`, `obsidian-bases`, `json-canvas`, etc.) — load the relevant skill before editing Obsidian-specific syntax.

## Scripts (`scripts/`)

- Stdlib only, idempotent, declarative names, one script one job (see `scripts/WH!.md`).
- Verify a script after editing: `python3 -m py_compile scripts/<name>.py`.

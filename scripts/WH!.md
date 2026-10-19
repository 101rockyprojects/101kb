# Snippets

This folder is for helpful executable commands to keep the information organized.

## What belongs here

- Executable (python) code

## Conventions

- The name has to be declarative: `organize_images` tells the action and the expected output.
- Keep it simple: One command does one thing. Avoid complex processes that can make a mess.
- MUST be indempotent: No matter how many times you execute, it has the same result if has the same input.
- Stdlib only, so a script never becomes a dependency you have to install.

## Scripts

### `organize_images.py`

Moves local images under `assets/img/`, updates Markdown references, and
renames referenced `Pasted*` images to kebab-case note names (with numbered
suffixes when a note has multiple pasted images).

```bash
python3 scripts/organize_images.py
```

## Suggested Links

- Why: [[README]]

# 101kb

> A lightweight knowledge base. Engineering notes, code concepts, tools, and career learnings — all in Markdown. Works by synopsis, you learn new concepts by linking them to ones you already know.

This repo is also meant to be maintained with Git: small commits, clear history, and knowledge that lives in plain files.

## Why the name?

**101** — My favorite number. Also represents fundamentals (like "subject 101").

**KB** — Knowledge Base. And a joke: Markdown files are so light, this whole archive *feels* like it fits in **101 kilobytes**.

## What's inside?

This is my second brain. Every folder is a piece of my engineering journey.

| Section      | What you'll find                                                        |
| ------------ | ----------------------------------------------------------------------- |
| `concepts/`  | Code fundamentals, algorithms, system design, programming paradigms     |
| `tools/`     | Useful CLI commands, extensions, workflows, productivity hacks          |
| `career/`    | Lessons from my engineering degree, internship insights, soft skills    |
| `projects/`  | Documentation of my own projects — architecture, decisions, reflections |
| `scripts/`   | Quick life-quality commands                                             |
| `snippets/`  | Reusable code blocks, patterns, and solutions I keep coming back to     |
| `resources/` | Books, courses, articles, and references that changed how I think       |
| `assets/`    | Images and attachments used by the notes                                |

Quick entry points (folder "What's Here" notes):
- [[concepts/WH!]]
- [[tools/WH!]]
- [[career/WH!]]
- [[projects/WH!]]
- [[snippets/WH!]]
- [[resources/WH!]]
- [[assets/WH!]]

## Who is this for?

Mostly me. But if you're an engineering student or a curious developer, you might find something useful here. Feel free to explore, learn, and star the repo if it helps you too.
It is a quick and useful way to keep track of my knowledge, concepts and interesting topics, using a version control system (Git) to edit and preview Markdown files (Obsidian).

If you open this as an Obsidian vault, internal links like `[[Zettelkasten]]` and `[[Obsidian]]` become your main navigation system.

## How To Navigate

- Start from a folder index: see the `WH!.md` inside each top-level folder.
- Use links instead of hierarchies: prefer connecting ideas with `[[links]]` over creating deeper folders.
- Keep notes skimmable: begin with a short definition, then examples, then related links.

## Philosophy

- **Markdown first** — Simple, portable, future-proof.
- **Own your knowledge** — No paywalls, no vendor lock-in.
- **Stay light** — Every note justifies its weight.
- **[[Zettelkasten]]** — Relations between notes.
- **[[Obsidian]]** — A practical way to browse and maintain the vault.

---

## Configurations, plugins and addons

Personal configurations for better performance
- **Theme**: Maple
- **Community Plugins**:
	- **Auto Card Link**: Enhance links with a card (OpenGraph).
	- **Code Styler**: Enhance code-blocks style
	- **Copilot/Smart Second Brain**: Integration of chat with agents
	- **Git**: Integration of git UI
	- **Linter**: Lint when save 
	- **Remember cursor position**: Automatic re-position of a previous opened file
	- **Style Settings**: Enhance style customization (ft. Maple)

### Basic Style Settings

**Config** > **Community Plugins** > **Style Settings** > **Import**  > *Paste the next json configuration:*

```json
{
  "maple-editor@@font-override-editor-font-size": false,
  "maple-editor@@font-maple-interface": false,
  "maple-editor@@font-maple-text": false,
  "maple-editor@@font-maple": true,
  "maple-basic@@app-layout-card-bg": "app-layout-card-gradient",
  "maple-basic@@setting-accent-h-dark": 30,
  "maple-basic@@color-active-dark": "color-active-custom-dark",
  "maple-basic@@setting-bg-delta-dark": 0.4,
  "maple-basic@@color-modify-bg-dark": true,
  "maple-basic@@app-layout-card-border": false,
  "maple-basic@@color-highlight-only": false,
  "maple-basic@@color-dark-dim-disable": true,
  "maple-editor@@heading-color-style": "heading-color-accent",
  "maple-editor@@heading-h1-center": true,
  "maple-editor@@heading-h1-italic": false,
  "maple-editor@@setting-h1-weight": "800",
  "maple-editor@@setting-h1-size": 1.8,
  "maple-editor@@heading-h1-caps": false,
  "maple-editor@@heading-h2-style": "heading-h2-full-line",
  "maple-editor@@heading-h2-full-line-direction": "heading-h2-full-line-left",
  "maple-editor@@heading-h2-center": false,
  "maple-editor@@heading-h2-italic": true,
  "maple-editor@@setting-h2-size": 1.4,
  "maple-editor@@setting-h2-weight": "550",
  "maple-editor@@heading-h2-caps": false,
  "maple-editor@@heading-h3-caps": true,
  "maple-editor@@setting-h3-size": 1.3,
  "maple-editor@@setting-h4-size": 1.2,
  "maple-editor@@heading-h5-caps": true,
  "maple-editor@@heading-h3-style": "heading-h3-underline",
  "maple-editor@@hr-enable": true,
  "maple-editor@@code-line-number": false,
  "maple-editor@@code-language": true,
  "maple-editor@@code-nowrap": true,
  "maple-editor@@code-preview-bg": false,
  "maple-editor@@code-theme": true,
  "maple-editor@@editor-bg-pattern": "editor-bg-grid-dots",
  "maple-editor@@setting-editor-bg-grid-spacing": 30,
  "maple-editor@@setting-editor-bg-grid-dots@@dark": "#403B21",
  "maple-editor@@setting-editor-p-spacing": 10,
  "maple-editor@@setting-editor-letter-spacing": -0.1,
  "maple-editor@@setting-editor-p-indent": 2,
  "maple-editor@@setting-line-height": 1.6,
  "maple-editor@@setting-file-line-width": "clamp(600px, 80%, 1000px)",
  "maple-editor@@quote-italic": true,
  "maple-editor@@quote-mark": true,
  "maple-editor@@setting-hr-icon": "//",
  "maple-editor@@line-indicator": "line-indicator-enable",
  "maple-editor@@line-active": "line-active-enable",
  "maple-editor@@editor-custom-bottom-spacing": false,
  "maple-editor@@setting-editor-bottom-spacing": 40,
  "maple-editor@@link-hover-expand": false,
  "maple-editor@@link-icon": true,
  "maple-editor@@link-heading": true,
  "maple-editor@@link-click-to-edit-in-live-preview": false,
  "maple-editor@@setting-link-internal-color@@dark": "#D0A031",
  "maple-editor@@setting-link-external-color@@dark": "#777DD5",
  "maple-editor@@table-full": true,
  "maple-editor@@table-style": "table-style-default",
  "maple-editor@@table-round": true,
  "maple-workspace@@explorer-title-wrap": false,
  "maple-workspace@@explorer-icon": true,
  "maple-workspace@@explorer-folder-bold": true,
  "maple-workspace@@outline-enable": false,
  "maple-workspace@@labeled-nav": false,
  "maple-workspace@@tab-float": false,
  "maple-workspace@@setting-tab-stack-header-width": 40,
  "maple-workspace@@tab-slide-up": false,
  "maple-workspace@@status-bar-style-float": false,
  "maple-workspace@@status-bar-style": "status-bar-default",
  "maple-workspace@@message-tooltip-hide-arrow": false,
  "maple-workspace@@scrollbar-hide": true,
  "maple-basic@@color-scheme": "color-use-custom",
  "maple-workspace@@message-modify": true,
  "maple-basic@@setting-color-active-custom-dark": "#AB7C44",
  "maple-basic@@setting-color-inactive-custom-dark": "#6B5845",
  "maple-workspace@@setting-color-dirs@@dark": "#D0A416",
  "maple-editor@@setting-list-marker@@dark": "#0E7653",
  "maple-editor@@setting-list-guide-color@@dark": "#2CAF84",
  "maple-editor@@setting-code-inline@@dark": "#2CAF84"
}
```

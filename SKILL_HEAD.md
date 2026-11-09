---
name: kai-report-creator
description: Generate zero-dependency HTML reports — 8 themes, 9 component types, a three-layer AI-readable structure, and an animated render mode. For business reports, data dashboards, research docs, KPI dashboards, and more.
version: 1.28.1
user-invocable: true
metadata: {"openclaw": {"emoji": "📊"}}
---

# kai-report-creator

Generate zero-dependency single-file HTML reports that mix text, charts, KPIs, timelines, and more.

## Highlights

- **Full-screen cover** — forest-editorial renders a cover by default; other themes opt in with `cover: hero`
- **8 built-in themes** — corporate-blue, minimal, dark-tech, dark-board, data-story, newspaper, regular-lumen, forest-editorial
- **9 component types** — KPI, chart, table, timeline, flow diagram, code block, callout, image, list
- **Report Review system** — 14 checkpoints for automatic refinement
- **AI-readable output** — three-layer machine-readable structure
- **Animated render mode** — `animations: scrollytelling` (dark GSAP scroll narrative) or `animations: iridescence` (light WebGL iridescent landing page, no CDN)
- **Mobile responsive**

---

## Installation

**Claude Code:** tell Claude "Install https://github.com/kaisersong/kai-report-creator"

**OpenClaw:** `clawhub install kai-report-creator`

> ClawHub page: https://clawhub.ai/skills/kai-report-creator

---

## Usage

```bash
/report --from file.md          # generate from a document
/report --from URL              # generate from a web page
/report --plan "topic"          # generate a .report.md outline
/report --generate file.report.md # generate HTML from an outline
/report --review file.html      # refine using the review checklist
/report --themes                # preview the theme gallery
```

---

## Command routing

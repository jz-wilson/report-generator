---
title: report-creator Technical Guide
theme: dark-tech
author: Engineering Team
date: 2024-10-08
lang: en
abstract: Complete usage guide for the report-creator skill, covering the IR format spec, the CLI interface and agent integration.
---

## System Architecture

:::diagram type=sequence
actors: [User/Agent, Claude, File System]
steps:
  - from: User/Agent
    to: Claude
    msg: /report --plan "Quarterly report"
  - from: Claude
    to: File System
    msg: write report.report.md
  - from: User/Agent
    to: Claude
    msg: /report --generate report.report.md
  - from: Claude
    to: File System
    msg: write report.html
:::

## Quick Start

:::code lang=bash title=Basic usage
# Two-step flow (recommended)
/report --plan "2024 engineering retrospective"
/report --generate report-2024.report.md

# One-step output
/report "30-day data report after product launch"

# Pick a theme
/report --theme minimal "Market research report"
:::

## Supported Components

:::list
- `:::kpi` — KPI cards with scroll-triggered counting animation
- `:::chart` — charts (bar/line/pie/scatter/radar)
- `:::table` — data tables
- `:::timeline` — timeline / milestones
- `:::diagram` — sequence / flow / tree diagrams (SVG)
- `:::code` — syntax-highlighted code blocks
- `:::callout` — note/warning blocks (note/tip/warning/danger)
- `:::image` — image-and-text layout (left/right/full)
:::

## Notes

:::callout type=danger
`--bundle` mode inlines every external library into the HTML, so the file can reach 2-4MB. Use it only when you need to run fully offline.
:::

:::callout type=note
When used as a downstream agent node, the upstream agent only needs to put the IR content in context and call `/report --generate`; no extra arguments are required.
:::

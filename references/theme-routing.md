# Theme Routing

## Language

Use `en` for placeholders, TOC labels, date display, and shell labels.

## Theme Selection (first match wins)

| Signal | Theme |
|--------|-------|
| weekly/daily/monthly/work progress | `regular-lumen` |
| sales/revenue/KPI/quarterly/business | `corporate-blue` |
| research/survey/whitepaper/internal | `minimal` |
| tech/architecture/API/system/performance | `dark-tech` |
| news/industry/trend | `newspaper` |
| retrospective/proposal/work summary/project summary/phase summary/year-end summary | `forest-editorial` |
| annual/story/growth | `data-story` |
| board/dashboard/status | `dark-board` |
| generic project progress/project status | `corporate-blue` |

`forest-editorial` sits below the more specific signals on purpose: an explicit
weekly/monthly report stays `regular-lumen`, quarterly results stay
`corporate-blue`, and a technical proposal stays `dark-tech` — only the
retrospective/summary/proposal reports that no sharper signal claims land here.
`data-story` is purely the data-shaped narrative (annual/growth); the
retrospective keywords moved out.
`forest-editorial` also implies a full-screen cover
(`references/html-shell/cover.md`) with no way to turn it off, so it conflicts
with `animations: scrollytelling|iridescence`.

Summary keywords are matched as compounds (`work summary`, `project summary`)
rather than a bare `summary`, because keyword matching runs over the whole IR
text — a bare `summary` would be claimed by every report that merely has a
summary section. The style word `editorial` also selects it.

## Report Class

Classify content by numeric density: `narrative` < 5%, `mixed` 5-20%, `data` > 20%; short topics default to `mixed`.

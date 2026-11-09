# Audit Pass

Load this file for `--review --focus audit`. It is a technical diagnosis: do not fix anything. Document the issues so other passes can fix them.

Adapted from Impeccable's `audit` command (Apache 2.0). Read `references/design-refine.md` first for the ground rules and severity levels. This is a code and render audit of what is measurable. For judgment about hierarchy and clarity, use `--focus critique`.

## Diagnostic Scan

Score each of five dimensions from 0 to 4. Start with the mechanical tools, then verify each finding in context and drop false positives.

```
python scripts/html_quality_gate.py <report.html>
python scripts/guard_validate.py <report.report.md>
```

Also open the report at 1280px and 390px, in print preview, and with scripts blocked.

### 1. Accessibility

Check:
- **Contrast.** Text under 4.5:1, or large text under 3:1. Check text on tinted cards, badges, chart labels, and dark themes.
- **Headings.** One `h1`, no skipped levels, headings in a sensible order.
- **Landmarks and semantics.** Real headings, lists, tables with header cells; buttons that are buttons.
- **Text alternatives.** Charts and images carry a summary or alt text that states what they show.
- **Keyboard.** The TOC toggle, export menu, summary card, and edit mode work by keyboard with a visible focus ring and no trap.
- **Not by color alone.** Status and chart series differ by label, shape, or pattern too.
- **Motion.** `prefers-reduced-motion` has an intentional alternative that removes spatial movement but keeps state changes. Flag a blanket "all animation off" rule that erases useful feedback, flashing, and motion that blocks reading.

Score: **0** fails WCAG A · **1** major gaps · **2** partial, significant gaps · **3** AA mostly met · **4** AA fully met.

### 2. Performance

Check:
- File size and what dominates it (inline images, fonts, libraries).
- External dependencies: a chart or animation library on a CDN, and whether `--bundle` is offered or the page degrades without it.
- Images: sized sensibly, compressed, lazy where below the fold.
- Fonts: a system stack, or a small number of weights.
- Expensive effects: `backdrop-filter` and large blur areas, shadows on many elements.
- Animation on layout properties (`width`, `height`, `top`, `left`, margins); `will-change` left on at rest.
- Animated modes: WebGL or canvas work pauses when off-screen; the page stays smooth on a mid-range device.

Score: **0** severe · **1** major problems · **2** partial · **3** mostly lean · **4** fast and lean.

### 3. Theming

Check:
- Colors come from the theme's CSS variables; no hard-coded colors outside the theme or a deliberate `theme_overrides`.
- `data-theme`, `data-template`, and `data-version` match the theme and shell in use.
- Dark themes have their own contrast and surface elevation; they are not an inverted light theme.
- Component colors keep one meaning across the page (status, accent, series).

Score: **0** none · **1** mostly hard-coded · **2** tokens used inconsistently · **3** tokens used, minor strays · **4** fully token-driven, dark theme correct.

### 4. Responsive And Export

Check:
- No horizontal scroll at 390px; wide tables scroll inside their own container.
- Text readable at phone size (16px for prose) and at 200% zoom.
- Tap targets at least 44×44px; WCAG AA's floor is 24px.
- Print: sensible page breaks, no clipped KPI rows or charts, controls hidden, backgrounds handled.
- Summary card and image exports (`im`, `mobile`, `desktop`): legible, correct background, no hidden TOC or export button in the capture.
- Content stays in the same order at every width.

Score: **0** desktop only · **1** major issues · **2** works, rough edges · **3** good, minor overflow or target issues · **4** fluid across phone, print, and export.

### 5. Implementation Integrity

Start here. Does the report express a coherent, subject-specific system, or is it a template with the words swapped? Check:
- The quality gate and guard results, verified in context.
- JSON-LD present and valid; `ir-hash` and `irHash` agree; the `report-summary` block is present.
- No `[INSERT VALUE]` residue unless data is genuinely missing, and then it is flagged.
- No pattern from `references/anti-patterns.md`: fake KPI, decorative chart, pseudo-timeline, template heading, color flood.
- No duplicate date, no stale version or "as of" text, figures that match the text around them.
- Headings and components that could belong to an unrelated report.

Score: **0** systemic problems · **1** major repeated failures · **2** several verified issues · **3** minor isolated issues · **4** coherent and intentional.

## Report

Give an Audit Health Score table.

| # | Dimension | Score | Key finding |
|---|---|---|---|
| 1 | Accessibility | ? | most critical issue, or "—" |
| 2 | Performance | ? | |
| 3 | Theming | ? | |
| 4 | Responsive and export | ? | |
| 5 | Implementation integrity | ? | |
| | **Total** | **?/20** | rating band |

Bands: **18–20** Excellent · **14–17** Good · **10–13** Acceptable · **6–9** Poor · **0–5** Critical.

Then:

1. **Integrity verdict.** Pass or fail, with the evidence.
2. **Executive summary.** The score, issue counts by severity (P0/P1/P2/P3), the top 3–5 issues, and next steps.
3. **Findings by severity.** For each: `[P?] name`, **Location** (section, selector, or line), **Category**, **Impact** on the reader, **Standard** (WCAG criterion, if any), **Fix**, **Suggested pass**.
4. **Systemic issues.** Patterns that point to a gap, not a one-off: "KPI deltas fail contrast in every dark theme card."
5. **What's working.** Good practice to keep.
6. **Recommended actions.** Passes in order, P0 first. Only passes that fix something. End with `polish`.

Do not report an issue without its impact. Do not give generic advice. Do not skip what works. Everything cannot be P0. Keep P3s few.

> I can run these one at a time or all at once. Re-run `--focus audit` after the fixes to see the score move.

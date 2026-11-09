# Design Refinement

Load this file when `--review` is called with `--focus <pass>`, or when the user asks for a design pass on an existing report: typography, layout, color, simplifying, copy, hardening, adaptation, motion, polish, a design critique, or a technical audit.

Adapted from [Impeccable](https://github.com/pbakaus/impeccable) (Apache 2.0; license and notice in `.claude/skills/impeccable/`). Only the parts that fit a generated, single-file HTML report are kept. Impeccable's detector, live browser mode, hooks, and image-comp pipeline are left out.

## Pick The Pass

| `--focus` | What it does | Edits? | Load |
|---|---|---|---|
| `critique` | Heuristic design review: score, issues by severity, reader personas | No | `references/design-refine/critique.md` |
| `audit` | Technical review: accessibility, performance, theming, responsive, integrity | No | `references/design-refine/audit.md` |
| `typeset` | Hierarchy, size, measure, rhythm | Yes | `references/design-refine/passes.md` |
| `layout` | Reading order, grouping, spacing rhythm | Yes | `references/design-refine/passes.md` |
| `color` | Color roles, contrast, data color | Yes | `references/design-refine/passes.md` |
| `distill` | Cut what does not earn its place | Yes | `references/design-refine/passes.md` |
| `clarify` | Headings, labels, terms, units | Yes | `references/design-refine/passes.md` |
| `harden` | Real-data edge cases: long, empty, many, missing | Yes | `references/design-refine/passes.md` |
| `adapt` | Phone, print, image export | Yes | `references/design-refine/passes.md` |
| `motion` | Animation purpose, timing, reduced motion | Yes | `references/design-refine/passes.md` |
| `polish` | Final pass before sharing | Yes | `references/design-refine/passes.md` |

Load only the file for the pass asked for. With no `--focus`, `--review` runs the 14-checkpoint checklist and does not load this file.

## Surface Mode

The mode names what the reader needs from this page. Choose it from the report, then scale ambition to it.

| Mode | Reader goal | Typical reports | Ambition shows as |
|---|---|---|---|
| **Read** | Understand something | `research`, `brief`, `comparison`, long-form | Structure for comprehension first. A calm column, clear heading ladder, wayfinding. Restraint and precision. |
| **Operate** | Scan state and act | Dashboards, `dark-board`, `regular-lumen`, `update`, weekly and monthly reports | Scan order, stable density, consistent components, real numbers, status that carries meaning. |
| **Persuade** | Decide and act | Pitches, launch and investor summaries | A clear claim, real proof, one obvious next step. |
| **Experience** | Be inside the work | `animations: scrollytelling` or `iridescence` | One authored focal moment; the artifact leads. |

Read and Operate reward restraint: fewer accents, flat surfaces, little motion. Persuade and Experience may commit harder to a visual idea. The reading text of an animated page still follows the Read rules.

## Ground Rules

- **Refine; never redesign.** Keep the theme, content, facts, and IR. Fix the cause at the narrowest level. If the concept is wrong, say so and recommend `--plan` again.
- **The brief wins.** Honor a pinned theme, palette, or font, even where it conflicts with a rule here. A built-in theme's signature (the `data-story` gradient title, the `forest-editorial` cover) is not a defect.
- **Never fabricate.** Do not add claims, numbers, sources, or quotes. Ask before changing a factual claim. Keep `[INSERT VALUE]` where data is missing.
- **Two judgments, kept apart.** A design judgment (you reading the page) and a mechanical check (`scripts/html_quality_gate.py`, `scripts/guard_validate.py`, contrast math). Form the design judgment first; a scan result anchors it. A clean scan is a floor, not proof of quality.
- **Look at the render.** Check it at the sizes it ships: desktop (about 1280px), phone (about 390px), print, and the summary card and image export when they are in scope. Batch the checks: fix everything one look shows before looking again. Two inspection rounds is the ceiling.
- **Valid captures only.** Before judging a screenshot, settle or disable entrance motion, capture full-page from the top, and open each file to confirm it shows what its name says. A half-loaded or blank capture is no evidence.
- **Evidence over assertion.** Answer each Verify item with a selector, a computed value, or what you saw. Never a bare "yes".
- **Say what stayed untested.** Name what you could not check (a real phone, Safari, a screen reader).
- **Fresh reviewer when you can.** When a sub-agent tool exists and the report was just generated or heavily edited, review it with a fresh agent that gets only the report, the IR, and the screenshots. It should not inherit your reasoning. If you run it inline, say so.

## Severity

Tag every finding.

| Level | Meaning | Action |
|---|---|---|
| **P0** | Blocks reading or misleads: wrong number, hidden content, broken export | Fix now |
| **P1** | Real difficulty or confusion, or a WCAG AA failure | Fix before sharing |
| **P2** | Annoyance with a workaround | Fix next pass |
| **P3** | Polish; no real reader impact | If time allows |

If unsure between two levels, ask: would a reader write back about it? If yes, it is at least P1. Keep P3s few; a long tail buries the issues that matter.

## Report-Specific Floor

Check these in every pass that touches the render.

- **Contrast.** Body 4.5:1; large text, controls, and icons 3:1. On tinted surfaces, derive secondary text from the surface hue, not flat gray.
- **Measure.** Prose column 60–75 characters. Body 15px or more (16px for long-form prose).
- **Numbers.** One format per metric, units beside values, a time period on every figure. `:::kpi` holds a short real metric (`references/anti-patterns.md`).
- **Headings.** Specific claims, not labels like "Overview". More space above a heading than below.
- **Coverage.** Every requirement in the brief is present and findable within seconds.
- **No hollow components.** No chart, timeline, or KPI card without real data behind it.
- **Content visible by default.** The page reads with scripts blocked or slow. Entrance motion never hides content.
- **Export.** Print, summary card, and image export keep the same hierarchy.

## After A Pass

- Report what changed and what you left alone, with the reason.
- If the pass edited content text, keep the HTML and its `.report.md` in step, and keep `<meta name="ir-hash">` and the JSON-LD hash consistent with the IR (`references/output-metadata.md`).
- Recommend the next pass only if it would fix a named finding. End with `polish` when any fix was made.

## Related

- `references/review-checklist.md` — the 14 automatic checkpoints that run in every `--review`
- `references/design-quality.md` — the baseline these passes refine
- `references/anti-patterns.md` — the report patterns to remove
- `references/impeccable-anti-patterns.md` — Impeccable's anti-pattern list mapped to report rules

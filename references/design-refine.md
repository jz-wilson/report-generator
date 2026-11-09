# Design Refinement Passes

Load this file when `--review` is called with `--focus <pass>`, or when the user asks for a typography, layout, color, simplification, copy, or final-polish pass on an existing report.

Adapted from [Impeccable](https://github.com/pbakaus/impeccable) (Apache 2.0, see `.claude/skills/impeccable/LICENSE`). Only the parts that fit a static, read-only HTML report are kept.

## Ground Rules

- **A report is a Read surface.** The reader came to understand something. Structure for comprehension first. Ambition shows as precision and restraint, not decoration. Animated modes (`scrollytelling`, `iridescence`) may be bolder; the passes below still apply to their reading text.
- **Refine, never redesign.** Keep the theme, the content, the facts, and the IR. Do not add claims or numbers (Core Principle 2). If the concept is wrong, say so and recommend `--plan` again.
- **The brief wins.** Honor a pinned theme, palette, or font. A built-in theme's signature move (for example the `data-story` gradient title or the `forest-editorial` cover kicker) is not a defect.
- **Look at the render.** Check the result at the sizes it ships: desktop (about 1280px), mobile (about 390px), and print. Batch the checks: fix everything one look shows before looking again.
- **Evidence over assertion.** Answer each Verify item with a selector, a computed value, or what you saw. A clean scan or a bare "yes" is not proof.
- **One pass at a time.** Run only the pass named by `--focus`. Finish with the final-polish pass only when asked for it.

## Passes

Use `--focus typeset|layout|color|distill|clarify|polish|critique`.

### `typeset`: hierarchy and reading

Assess:
- Can title, section heading, body, label, and metadata be told apart at a glance?
- Are adjacent sizes or weights too close to do different jobs?
- Is there one deliberate scale, or arbitrary values?

Apply:
- Body text at least 15px, in a 60–75 character column. Wider lines need more line height.
- Use the fewest families and weights that make the hierarchy clear. Combine size, weight, space, and tone; do not ask size alone.
- Same role, same style everywhere (every section heading, every label).
- Left-align body text. Keep monospace for code only.
- Paragraph spacing marks paragraphs; do not also indent.

Verify: roles are recognizable without reading the copy; long headings and the mobile width do not break the hierarchy.

### `layout`: order, grouping, rhythm

Assess:
- **Squint test.** With the page blurred, can you still find the lead element, the second element, and the major groups, in order?
- Are related items close and distinct groups apart, or are boxes standing in for weak spacing?
- Does one spacing value repeat until everything weighs the same?

Apply:
- Group by proximity before adding containers. Flatten nested cards.
- Alternate tight and generous intervals. More space above a heading than below it.
- Use one spacing scale; remove one-off gaps.
- Let hierarchy follow reader priority: the conclusion first, then evidence, then detail.
- Check DOM order matches reading order at mobile width.

Verify: the squint test passes; nothing overflows horizontally at 390px; export and print layouts keep the same order.

### `color`: meaning, not decoration

Assess:
- Which colors carry meaning (status, emphasis, series) and which are decoration?
- Where does gray hide hierarchy or state? Where does color alone carry information?

Apply:
- Let one accent own a role. Keep it rare enough to have force (`design-quality.md` §1, 90/8/2).
- Contrast: body text 4.5:1, large text and controls 3:1. Check text on tinted cards and on charts.
- Chart series and status must differ by more than hue: add labels, shape, or pattern.
- On tinted surfaces, derive secondary text from the surface hue, not a flat gray.
- Dark themes get their own elevation and contrast; do not invert a light theme.

Verify: computed contrast passes for every text and background pair; the report still reads in grayscale.

### `distill`: remove what does not earn its place

Assess: repeated information, decorative components, headings that restate the intro, callouts and charts that add no reading value, more than 2 colors plus neutrals.

Apply:
- Say each idea once. Cut filler, not meaning.
- Remove charts and callouts that only decorate (`anti-patterns.md`: `decorative-chart`).
- Cut secondary KPIs until the lead metrics stand out.
- Prefer short paragraphs, specific headings, and plain words.

Do not remove numbers a decision needs, caveats, or sources. Do not flatten the hierarchy completely.

Verify: the first screen answers the reader's question; nothing the reader needs for a decision was lost.

### `clarify`: copy

Assess: vague headings, internal jargon, unexplained abbreviations, inconsistent terms, missing units or time periods, labels that name the component instead of the finding.

Apply:
- Lead each section with its claim. Put the number and its unit together.
- One term per concept across the whole report. Define an abbreviation at first use.
- Actionable recommendations: who, what, by when, when the source gives it.
- Keep every fact and figure unchanged. Ask before changing a claim.

Verify: a reader with no background can state the main point and the next step after one scan.

### `polish`: final pass before shipping

Fix in this order:
1. Wrong, missing, or misleading content: `[INSERT VALUE]` left in, units missing, a chart that disagrees with its text.
2. Broken structure: TOC links, section IDs, `report-summary` JSON, export buttons.
3. Drift from the theme: spacing, radius, color roles.
4. Small visual faults: alignment, wrapping, widows, icon sizes.
5. Cleanup: no debug output, unused CSS, or leftover comments.

Then re-run the whole path: desktop, mobile, print, summary card, and image export. Do not perfect one section while the rest sits below the same bar.

### `critique`: diagnose only

Do not edit. Review the report as the reader and report:
- Scores out of 10 for **Hierarchy**, **Clarity**, and **Craft**, and an overall score out of 100.
- Issues ranked P0 (blocks reading or misleads), P1 (hurts comprehension), P2 (hurts polish), P3 (nit). One line each, with where it is and the fix.
- The single first fix.

Use `references/review-report-template.md` only if the user asks for a structured summary.

## Report-Specific Floor

Check these in every pass that touches the render:

- **Contrast.** Body 4.5:1; large text, controls, and icons 3:1.
- **Measure.** Body column 60–75 characters; body text at least 15px.
- **Numbers.** Aligned and consistent in format; units next to values; `:::kpi` holds a short real metric (`anti-patterns.md`).
- **Headings.** Specific, not labels like "Overview". More space above than below.
- **Coverage.** Every requirement in the brief is present and findable within seconds.
- **No hollow components.** No chart, timeline, or KPI card without data behind it.
- **Export.** Print, summary card, and image export keep the same hierarchy.

## Related

- `references/review-checklist.md` — the 14 automatic checkpoints that run in every `--review`
- `references/design-quality.md` — the baseline these passes refine
- `references/anti-patterns.md` — the patterns to remove

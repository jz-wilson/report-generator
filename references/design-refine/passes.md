# Refinement Passes

Load this file for `--review --focus typeset|layout|color|distill|clarify|harden|adapt|motion|polish`. Run only the pass asked for.

Adapted from Impeccable's `typeset`, `layout`, `colorize`, `distill`, `clarify`, `harden`, `adapt`, `animate`, and `polish` commands (Apache 2.0). Read `references/design-refine.md` first for the ground rules, surface modes, and severity levels.

Every pass has the same shape:

1. **Assess** the report as it is. Answer each question with a selector, a value, or what you saw.
2. **State the thesis** in a few lines before you edit.
3. **Apply** the smallest change that fixes the cause.
4. **Verify** at the sizes the report ships. Answer each item with evidence.
5. **Hand off.** When the result holds, recommend `polish`.

Edit the report HTML. If the fix changes wording or structure, change the matching `.report.md` too.

## `typeset`: hierarchy and reading

Typography carries information, hierarchy, and voice. Improve it inside the theme; do not swap the theme's identity.

**Mode.** Read and Operate: stability, scan order, and measure come first; one well-tuned family and a fixed role scale are often right. Persuade and Experience: display type may carry the voice.

**Assess**
- **Fit.** Which faces, weights, and roles does the theme set? Is every family needed?
- **Hierarchy.** Can title, section heading, body, label, metadata, and data be told apart at a glance? Are adjacent sizes or weights too close to do different jobs?
- **Scale.** Is there one deliberate role scale, or arbitrary values? Do repeated roles look identical everywhere?
- **Reading.** Is body copy within 60–75 characters per line? Do line height, paragraph rhythm, and contrast suit the face and the width?
- **Stress.** What happens with a very long heading, a narrow phone, 200% zoom, or a missing font?

**Thesis.** Name the roles the report needs, the contrast between them, the measure, and which theme faces are authoritative.

**Apply**
- Body text 15px or more; 16px for long-form prose. Labels and dense table text may go to 13–14px.
- Use the fewest roles and families that make the hierarchy plain. Combine size, weight, space, and tone; do not ask size alone to do the work.
- Wider lines need more line height. Light text on a dark ground needs a little more line height, a touch more tracking, and sometimes one step more weight.
- Same role, same style, everywhere.
- Align and format numbers consistently. Use tabular figures where columns of numbers line up.
- Left-align body text. Do not justify. Reserve monospace for code and data.
- Paragraph spacing marks paragraphs; do not also indent.
- Do not add a second family without a role only it can do. Do not make type decorative at the cost of comprehension.

**Verify**
- Title, heading, body, label, and metadata roles are recognizable without reading the words.
- Long headings and the phone width do not break the hierarchy.
- Prose stays within the measure; numbers line up.

## `layout`: order, grouping, rhythm

Layout turns reader priority into reading order, grouping, and space. Find the structural problem before moving boxes.

**Mode.** Read and Operate: predictable structure and stable density are features. Persuade and Experience may use asymmetry when the theme earns it.

**Assess**
- **Squint test.** Blur the page. Can you still find the lead element, the second, and the major groups, in order?
- **Grouping.** Are related items close and separate groups apart, or are boxes making up for weak spacing?
- **Rhythm.** Do tight and generous gaps create a cadence, or does one value repeat until everything weighs the same?
- **Structure.** Do repeated cards or columns hold truly equal items, or are they a default?
- **Density.** Does the amount of information per region suit the mode and the reader?
- **Adaptation.** At phone, mid, wide, and zoomed widths, what reorders, collapses, or scrolls? Does the DOM order still match the visual order?
- **Extremes.** Long text, empty data, many rows.

**Thesis.** Name the main reading path, what belongs together, what leads and what supports, the intended density, and how it changes by width.

**Apply**
- Group by proximity before adding containers. Flatten nested cards.
- Alternate tight and generous intervals. More space above a heading than below.
- Use one spacing scale. A 4-unit base gives the useful middle steps an 8-only scale misses. Replace one-off gaps.
- Let hierarchy follow reader priority: conclusion, then evidence, then detail. Not the order the source file happened to use.
- Use `gap` for sibling rhythm where it states the relationship directly.
- Keep distinct content visually distinct without boxing every group.
- Make responsive behavior structural: reorder, collapse, or reflow by what stays important.
- Repeat only to help recognition; break repetition when content or priority changes.

**Verify**
- The squint test still shows lead, second, and groups in order.
- Related content groups; unrelated content does not blur together.
- Tight and generous space make a rhythm, not a monotone.
- No horizontal overflow at 390px; DOM order matches visual order.
- Print and export keep the same order.

## `color`: meaning, not decoration

Introduce or correct color as hierarchy, meaning, and atmosphere. Keep the theme's palette and its semantic colors.

**Mode.** Read and Operate: color mainly encodes status, emphasis, data series, and wayfinding. Rarity gives an accent its force. Persuade and Experience may let one color own a large region.

**Assess**
- Which colors are the theme's commitments, and which are strays?
- Where does gray hide hierarchy or status? Where does color alone carry information?
- Which text and background pairs fail contrast? Check cards, badges, chart labels, and dark themes.
- What do chart series need to stay distinct?

**Thesis.** Name the color roles: surface, primary and secondary text, accent and emphasis, borders, success, warning, error, info, and chart series. Roles, not a bag of swatches.

**Apply**
- Let the strongest color own a deliberate role (`design-quality.md` §1, the 90/8/2 law). Do not scatter tiny accents.
- Keep status meanings consistent across the page; respect domain conventions.
- Contrast: body 4.5:1; large text, controls, and icons 3:1. Check computed pairs, not the eye alone.
- On tinted surfaces, derive secondary text from the foreground or surface hue, never flat gray.
- Chart series and status differ by lightness, label, shape, or pattern too, so color is not the only code.
- For a new palette, prefer OKLCH: lightness and chroma move predictably. Lower chroma near white and black. Prefer explicit colors over stacked translucent overlays, so contrast does not depend on what sits behind.
- Dark themes get their own surface elevation and contrast. Do not invert a light theme.
- Prefer theme variables over new hard-coded values. Use `theme_overrides` only for a small tone hint.

**Verify**
- Every color has a stable role.
- Attention lands on the lead content or state.
- Contrast and non-color cues pass.
- The report still reads in grayscale.
- It is still recognizably this theme.

## `distill`: remove what does not earn its place

Strip the report to its essence. Anything that does not help the reader decide or understand goes.

**Assess**
- **Complexity sources:** too many elements, repeated information, more than a few colors and weights, heavy decoration, a hierarchy with no clear lead.
- **The essence.** What is the one thing this report must get across? What is the 20% that delivers 80% of the value? What can be removed, merged, or moved behind the summary?
- Ask the user if the purpose is unclear. Do not guess.

**Apply**
- Say each idea once. If a heading says it, the intro adds something new or goes. Cut filler and hedging, not meaning.
- Remove charts, callouts, and KPI cards that only decorate (`anti-patterns.md`: `decorative-chart`, `fake-kpi`).
- Cut secondary KPIs until the lead metrics stand out. Merge near-duplicate sections.
- Use one or two colors plus neutrals. One family, a few sizes, two or three weights.
- Flatten structure. Drop borders, shadows, and backgrounds that do not serve hierarchy. Never nest cards in cards.
- Prefer short paragraphs, specific headings, and plain words. Active voice.
- Move secondary detail to a table or an appendix section.

**Do not**
- Remove a number a decision needs, a caveat, or a source.
- Make it so spare that it becomes unclear.
- Flatten the hierarchy completely; some things must stand out.
- Oversimplify a complex subject: match complexity to the real task.

**Verify**
- The first screen answers the reader's question.
- A decision-maker still has everything needed.
- The hierarchy is clearer, not flatter.
- Note what you removed and why.

## `clarify`: headings, labels, terms, units

Rewrite unclear text so the reader knows what is true, what matters, and what to do. Keep factual meaning, product terms, and the author's voice.

**Assess** the whole reading path, not single strings:
- Ambiguous nouns, verbs, and headings.
- Jargon or assumed knowledge; abbreviations without a definition.
- Missing units, baselines, or time periods ("12%" of what, since when).
- Inconsistent terms or capitalization.
- Repeated headings, intros, and captions.
- Tone that ignores risk, success, or urgency.

**Message hierarchy.** For each section decide: the one fact the reader needs now; the action available next; the context that changes the decision; the right tone.

**Apply**
- Lead each section with its claim. Put the number and its unit together.
- One term per concept across the whole report. Define an abbreviation at first use. Keep a short glossary if the same inconsistency recurs.
- Headings state the finding, not the topic: "Churn fell to 2.1% after the March fix", not "Churn".
- Recommendations name who, what, and by when, when the source gives it.
- Alt text and chart summaries convey the information; use empty alt for decoration.
- Captions answer the question the reader will ask, not restate the chart.
- Do not rely on punctuation, color, or icons to carry the message alone.
- Keep every fact and figure unchanged. Ask before changing a claim, a legal meaning, or a term that may be domain-specific.

**Verify**
- Read it in context with no hidden knowledge: can you state the main point and the next step?
- Terms, units, and periods are consistent and present.
- Headings and labels still fit at phone width.
- It is as short as it can be without losing meaning.

## `harden`: real data, not perfect data

A report that only works with ideal data is not ready. Test the edges.

**Test**
- **Very long** titles, labels, names, and table cells; very short or empty ones.
- **Special characters:** ampersands, quotes, `<`, emoji, long unbroken strings and URLs.
- **Large and small numbers:** millions, billions, very small percentages, negatives, zero versus missing.
- **Many rows or items:** a table of 200 rows; 12 KPIs; 30 timeline events.
- **No data:** empty section, empty table, all-placeholder chart (should have been downgraded).
- **Environment:** scripts blocked, a slow or blocked CDN, offline, print, dark-mode preference.

**Apply**
- Let text wrap (`overflow-wrap`) or clamp deliberately; never clip silently. Give flex and grid children `min-width: 0` so they can shrink.
- Wide tables scroll inside their own container; add a visible scroll cue.
- Show zero, missing, and not-applicable differently. Never print a blank or `NaN`.
- Format numbers with consistent separators, units, and decimals. Do not fix widths on text containers.
- Long lists: group, paginate by section, or move to an appendix instead of one tall block.
- Empty states say what is absent and why, and what to do next.
- Content is visible by default and reads with scripts blocked. A chart that needs a CDN has a text or table fallback, or the report is built with `--bundle`.
- Escape user-supplied text so markup never leaks into the output.

**Do not** assume English-length text in fixed boxes, leave a generic "error" or "N/A" with no cause, or rely on a client-side-only check.

**Verify**
- Run the report with 100+ character titles, empty values, 100+ rows, special characters, scripts blocked, and print preview.
- Nothing overflows, clips, shows `undefined`, or hides content.

## `adapt`: phone, print, image export

Adapting is rethinking the experience for a new context, not scaling pixels.

**Assess.** What was the report designed for? What breaks in the target context: width, input, connection, reading situation?

**Phone**
- One column. Stack side-by-side blocks. Full-width components.
- Text 16px for prose. Tap targets 44×44px.
- Prioritize: lead and conclusion first; secondary detail in sections that follow.
- Tables scroll in place or become stacked rows with labels.
- A 4-up KPI row becomes 2×2 or a stack.
- Do not hide core content on a phone. If it matters, make it fit.

**Tablet and desktop**
- Keep a readable measure; do not stretch text to the full width.
- Use extra width for asymmetric layouts (`2fr 1fr`), not for longer lines.

**Print**
- Page breaks at section boundaries; no split KPI rows, charts, or table headers.
- Remove controls and the TOC overlay; keep a clean margin.
- Backgrounds: ensure text stays legible when background printing is off.
- Show full URLs for links; keep page title and date.

**Image export and chat share**
- Legible at thumbnail size: large lead, short lines, few elements.
- Correct background; no stray controls or half-hidden TOC in the capture.
- The lead conclusion appears in the first screen of the image.

**Apply** content-driven breakpoints, not device names. Do not rely on hover for function. Do not change the information order between contexts.

**Verify** phone (390px), small phone (320px), tablet, 1280px, wide (1600px+), print preview, and each export mode in scope. Say what you could not test (a real phone, another browser).

## `motion`: purpose, timing, control

Use motion to explain state, relationship, or hierarchy, or for one authored moment the page has earned. Decoration without purpose is animation debt. Applies to the standard fade-in blocks and to the animated modes.

**Mode.** Read and Operate: motion serves feedback and continuity; keep it short and never make the reader wait. Persuade and Experience (`scrollytelling`, `iridescence`): one rehearsed focal sequence beats repeated section reveals.

**Assess**
- What job does each animation do: acknowledge an action, show a state change, keep continuity, direct attention, or express the theme?
- Is there one focal moment, or scattered effects and the same entrance on every section?
- What runs on scroll, and at what cost?

**Thesis.** Name the focal moment (if any), what needs continuity, what needs feedback, and the performance budget.

**Apply**
- Timing: 100–150 ms for feedback; 150–300 ms for routine changes; 300–500 ms for layout or overlay; 500–800 ms only for an authored focal entrance. Exit faster than entrance.
- Ease out with natural deceleration (`cubic-bezier(0.16, 1, 0.3, 1)`). No bounce or elastic by reflex.
- Prefer `transform` and `opacity`; allow blur, clip-path, and shadow when smooth and bounded to a small region. Do not animate layout properties (`width`, `height`, `top`, `left`, margins).
- Cap sibling stagger. Do not turn every scrolled section into a staggered list.
- **Content is visible in its default state.** A failed script must not hide the page.
- **`prefers-reduced-motion`** needs an intentional alternative: remove spatial movement and parallax, keep opacity and state changes that carry meaning. Not a blanket "all animation off".
- Stop any non-essential loop when off-screen or hidden. No autoplay sound.
- `will-change` only during a known animation.

**Verify**
- Each animation explains feedback, state, or relationship; removing it would lose meaning, not just decoration.
- The reduced-motion path still conveys every state change.
- Frame rate holds on a mid-range device; the page prints and exports with content visible.

## `polish`: the final pass

Polish is refinement, never concealed redesign. Keep the theme, content, and behavior. A scan result is defect evidence, not proof of quality: inspect the render.

**1. Establish the system.** Read the theme, shell contract, and tokens in use. If a prior critique exists (`<report-name>.critique.md`), use its priority issues as the backlog. Classify each drift before fixing it:
- **missing token:** the theme needs a reusable value;
- **one-off:** a shared component or pattern should replace it;
- **conceptual mismatch:** structure or hierarchy differs from the report's other sections;
- **local defect:** simply incomplete or inconsistent.

Fix the cause at the narrowest correct level.

**2. Gather evidence.** Look at the report at 1280px, 390px, and print preview; open the summary card and each export in scope. Note the quality bar and any known unfinished work.

**3. Triage, in this order.**
1. Wrong, missing, or misleading content: a stale figure, missing unit, `[INSERT VALUE]` left in, a chart that disagrees with its text.
2. Broken structure: TOC links, section IDs, `report-summary` JSON, export buttons, JSON-LD.
3. Missing states: empty or missing data, print, scripts blocked.
4. Hierarchy, responsive, and theme drift.
5. Visual and motion inconsistencies: alignment, wrapping, widows, icon sizes.
6. Cleanup: debug output, unused CSS, leftover comments.

Do not perfect one corner while the rest sits below the same bar.

**4. Polish the whole path.**
- **Flow and hierarchy:** the conclusion and next step are obvious; sections connect.
- **Layout and type:** align to the spacing scale; group tightly, separate generously; same role, same style; check wrapping at every width.
- **Color:** theme tokens, stable meanings, contrast in every state.
- **Content:** terms, capitalization, punctuation, units, and dates consistent. Ask before changing a claim.
- **Code:** no dead CSS or duplicated rules your edits created.

**5. Verify and finish.** Walk the whole path again: desktop, phone, print, summary card, image export. Run `scripts/html_quality_gate.py` and fix real defects. Finish by reviewing the source diff: remove accidental churn and temporary artifacts. Ship only when the report is complete and consistent from top to bottom. Note any narrow, intentional exceptions.

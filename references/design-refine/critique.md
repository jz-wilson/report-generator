# Critique Pass

Load this file for `--review --focus critique`. It is a diagnosis: do not edit the report.

Adapted from Impeccable's `critique` command and its heuristic, cognitive-load, and persona references (Apache 2.0). Read `references/design-refine.md` first for the ground rules, surface modes, and severity levels.

## Purpose

Resolve one target, run two independent assessments, and give a design critique the user can act on. The chat reply is the deliverable. Be direct and specific: name the exact element, say why it matters to the reader, and give a concrete fix. Do not soften. Do not write "consider exploring".

## Hard Rules

- Run **Assessment A** (design review) and **Assessment B** (mechanical evidence) independently. When a sub-agent tool exists, run them as two isolated agents that cannot see each other's output. Without one, finish and record A, then run B, then synthesize.
- A must finish before B's findings enter your synthesis. Mechanical output is exact but it still anchors judgment.
- Open the report in a browser at desktop and phone width when a browser tool exists. If none exists, say so; do not claim a visual check you did not run.
- The first line of the reply states the method:
  - `Method: dual-agent (A: <agent> · B: <agent>)`
  - `⚠️ DEGRADED: single-context (<reason>)`. A silent degraded critique is a failed critique.
- The questions come last. Write the whole report first, then ask. Nothing follows the questions.

## Assessment A: Design Review

Read the `.report.md` and the HTML, and look at the render. Judge as a design director would.

- **Specificity.** Is the report authored for this subject, or could an unrelated report use it unchanged? Judge this before you see any scan output.
- **Holistic design.** Hierarchy, information order, fit to the reader, composition, typography, color, accessibility, copy, edge cases.
- **Cognitive load.** Run the checklist below.
- **Reader journey.** Where does attention peak and drop? Is there a clear close with the conclusion and next step?
- **Heuristics.** Score the applicable ones (below).

Return: the specificity verdict, heuristic scores, cognitive load result, 2–3 strengths, 3–5 priority issues, persona red flags, minor notes, and 2–3 provocative questions.

## Assessment B: Mechanical Evidence

- `python scripts/html_quality_gate.py <report.html>` — shell, metadata, JSON-LD, placeholder, and theme checks.
- `python scripts/guard_validate.py <report.report.md>` — IR and component contracts.
- Render checks: horizontal overflow at 390px, computed contrast of text pairs, heading order, console errors, load with scripts blocked.

Return counts, rule names, locations, false positives, and any step that failed or was skipped, with the reason. Verify each finding in context before reporting it.

## Report Format

Synthesize both assessments. Say where they agree, where B caught what A missed, and which B findings are false positives. Use this order.

1. **Method line.**
2. **Design Health Score.** A table of the applicable heuristics, then `Total: n/N` and the rating band.
3. **Specificity Verdict.** Start here. Your unanchored judgment, then what the scan found.
4. **Overall Impression.** One short gut reaction: what works, what does not, the single biggest opportunity.
5. **What's Working.** 2–3 specific strengths and why they work.
6. **Priority Issues.** The 3–5 most important problems, most important first. Each has:
   - **[P0–P3] What** — name it clearly.
   - **Why it matters** — how it hurts the reader.
   - **Fix** — concrete.
   - **Suggested pass** — one of `typeset`, `layout`, `color`, `distill`, `clarify`, `harden`, `adapt`, `motion`, `polish`.
7. **Reader Red Flags.** 2–3 personas, each with what specifically breaks for them.
8. **Minor Observations.** Short notes.
9. **Questions to Consider.** Provocative, not generic: "What if the first screen stated the decision?"
10. **Questions** (see Ask The User).

Be honest with scores. A 4 means genuinely excellent. Most real reports score 60–80% of the maximum.

## Heuristics For A Report

Score each applicable heuristic 0–4. Mark one `n/a` with a one-line reason only when it genuinely cannot apply to a static document. The maximum is 4 × the number scored; never print `/40` over a partial set.

| # | Heuristic | In a report, check for | 
|---|---|---|
| 1 | **Visibility of status** | The reader always knows where they are: TOC and active section, "as of" dates on data, version and period, what is draft or placeholder |
| 2 | **Match to the reader's world** | Plain words, units and time periods on every figure, terms the audience knows, defined when not |
| 3 | **Control and freedom** | Usually `n/a` for a static page. Score it only when edit mode or export choices are central |
| 4 | **Consistency** | One term per concept, one number format, same component style for the same role, theme tokens used the same way |
| 5 | **Misreading prevention** | Units, baselines, truncated axes, ambiguous comparisons, percent versus points, mixed periods |
| 6 | **Recognition over recall** | A claim sits next to its figure; legends and labels are on the chart; the reader never flips back to decode |
| 7 | **Layered reading** | The page works at three depths: summary card or lead, headings and anchors, full detail |
| 8 | **Minimalism** | Every element earns its place; the hierarchy has one lead, a few supporting items, quiet detail |
| 9 | **Recovery from error** | Usually `n/a`. A static page has no error flow. Placeholder residue is an integrity issue, not this |
| 10 | **Help and sources** | Sources, method, definitions, caveats, and how to read the figures, where a reader needs them |

Score anchors: **0** broken or absent · **1** poor, most of it fails · **2** partial, major gaps remain · **3** good, minor gaps · **4** excellent, nothing to fix.

Rating bands, by percentage of the applicable maximum: **90%+ Excellent** (minor polish) · **70%+ Good** (address weak areas) · **50%+ Acceptable** (significant work needed) · **30%+ Poor** (major rework) · below that **Critical** (rebuild).

## Cognitive Load Checklist

Count the failed items. 0–1 failures: low load. 2–3: moderate, address soon. 4 or more: high, a critical fix.

- [ ] **Single focus.** The reader can find the main point without competing elements.
- [ ] **Chunking.** Information comes in groups of about 4 items or fewer.
- [ ] **Grouping.** Related items are visibly together.
- [ ] **Visual hierarchy.** It is obvious what matters most on each screen.
- [ ] **One thing at a time.** A paragraph or block makes one point before the next begins.
- [ ] **Minimal choices.** No decision point shows more than about 4 options or items to weigh.
- [ ] **Working memory.** The reader need not remember an earlier section to read this one; repeat the figure where it is used.
- [ ] **Progressive disclosure.** Detail is behind the summary, not in front of it.

Working memory holds about 4 items. 5–7 is pushing it; 8 or more makes readers skip. Common violations: a wall of KPIs, a figure explained three sections later, jargon without a definition, every block at the same visual weight, similar items styled differently.

## Reader Personas

Pick 2–3 for the report and walk through its main purpose as each. Report specific red flags, not generic worries. Name the exact element that fails.

| Persona | Who | Test | Red flags |
|---|---|---|---|
| **Skimmer** | An executive with 60 seconds | Can they state the conclusion and the decision after one screen and the summary card? | No bottom line up front; the answer sits in section 4; KPIs without meaning; headings that are labels |
| **Outsider** | Smart reader with no background | Is every term, abbreviation, period, and unit explained or obvious? | Undefined jargon; "Q3" with no year; a bare "12%" with no baseline |
| **Access-dependent reader** | Screen reader, keyboard, 200% zoom, low vision | Heading order, contrast 4.5:1, chart text alternatives, focusable controls, meaning not carried by color alone | Skipped heading levels; chart with no summary; red/green status only; unlabeled export buttons |
| **Stress tester** | Methodical; tries the edges | Long labels, empty and zero data, many rows, special characters, print, scripts blocked, CDN blocked | A table that overflows; "0" versus "missing" shown the same; chart blank offline; print cuts a KPI row |
| **Phone and chat reader** | One hand, interrupted, maybe a chat preview | 390px layout, 16px text, tap targets, the image export as shared in a chat | Horizontal scroll; tiny table text; a 4-column KPI row squeezed; export image unreadable at thumbnail size |

Match personas to the report:

| Report | Use |
|---|---|
| `brief`, `update`, periodic | Skimmer, Outsider, Phone and chat reader |
| `research` | Outsider, Access-dependent reader, Stress tester |
| `comparison` | Skimmer, Stress tester, Access-dependent reader |
| Dashboard, KPI board | Skimmer, Phone and chat reader |

When the IR has `audience`, add 1–2 personas from it. Do not invent audience details.

## Ask The User

After the report, ask targeted questions based on what you found. Each must cite a specific finding and offer 2–3 concrete answers.

- **Priority.** "I found weak hierarchy, a color-only status, and an unexplained KPI. Which should we fix first?"
- **Intent.** If the tone looks mismatched: "The report reads clinical. Is that intended, or should it feel warmer?"
- **Scope.** "Fix all N issues, or the top 3?"
- **Constraints** (only if relevant). "Should any section stay as it is?"

Ask 2–4 questions. If the report listed fewer than 3 priority issues you may skip the questions, but then end with the literal line `Questions skipped: <N> priority issues`. Count them; do not skip by feel. Ending with neither the questions nor that line is an incomplete critique.

## Recommended Actions

After the user answers, list the passes in order: the user's priorities first, then by impact. Map each priority issue to the pass that fixes it, skip passes that fix nothing, and respect off-limits areas. End with `polish` if any fix was recommended. Then say:

> I can run these one at a time or all at once. Re-run `--focus critique` after the fixes to see the score move.

To keep the critique for later, write the full report to `<report-name>.critique.md` beside the report. `--focus polish` reads the latest one as its backlog.

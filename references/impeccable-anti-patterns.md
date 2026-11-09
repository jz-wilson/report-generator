# Impeccable Anti-Pattern Integration

Integrates the 37 anti-patterns from [impeccable.style](https://impeccable.style/) into the report-creator rule system.

## Already Covered

These anti-patterns are already covered by existing report-creator rules and need no extra handling:

| Impeccable anti-pattern | Existing report-creator rule |
|---|---|
| AI color palette (purple gradients / cyan on dark) | `design-quality.md` §4 Forbidden Patterns + §1 90/8/2 Color Law |
| Defaulting to dark mode for safety | Content-Type → Theme Routing (light themes by default) |
| Dark mode with glowing accents | Same as above + shared.css dark-theme constraints |
| Flat type hierarchy (font sizes too close together) | §2 Typography: 10:1 Scale Ratio (enforced step between smallest and largest sizes) |
| Overused font (Inter, Roboto, Arial) | §4 Forbidden Patterns: `Inter as body font` |
| Single font for everything | Separate heading/body font stacks already exist |
| Wrapping everything in cards | §4 Forbidden Patterns: no card per section |
| Identical card grids | §3 KPI Grid Column Rules (column count adapts to item count) |
| Monotonous spacing | Visual rhythm rule: alternate prose → component → prose |
| Low contrast text | §7 Pre-Output Self-Check |
| Tight line height (<1.3x) | shared.css already defines line-height |
| Tiny body text (<12px) | §2 Typography min body 15px |
| Generic section headings | review-checklist.md §1.3 Anti-Template Section Headings |
| Prose walls | review-checklist.md §1.4 Prose Wall Detection |
| Rounded rectangles with generic drop shadows | shared.css border-radius/shadow definitions |
| Border accent on rounded element | shared.css accent implementation |
| Side-tab accent border | Same as above |
| Redundant information | BLUF Opening rule (§1.1) |
| Every button is a primary button | shared.css button styles |
| Gradient text | Already in the forbidden list |
| Hero metric layout | Visual rhythm rule (a big number is not forced on every page) |

## Anti-Patterns to Add

### Typography

| # | Anti-pattern | Description | Where to add |
|---|---|---|---|
| T1 | **Line length too long** | Text lines longer than ~75 characters cause reading fatigue | `design-quality.md` §7 self-check |
| T2 | **Wide letter-spacing on body text** | Body letter-spacing > 0.05em slows reading | `design-quality.md` §2 Typography: add an upper limit |
| T3 | **Justified text** | Justified text creates rivers of whitespace | `design-quality.md` §4 Forbidden Patterns |
| T4 | **All-caps body text** | All-caps body text breaks word-shape recognition | `design-quality.md` §4 Forbidden Patterns |
| T5 | **Monospace as technical shorthand** | Using monospace to fake a technical feel | `design-quality.md` §4 Forbidden Patterns |

### Color and Contrast

| # | Anti-pattern | Description | Where to add |
|---|---|---|---|
| C1 | **Pure black background (#000)** | A pure black background is harsh and unnatural | `design-quality.md` §7 self-check |
| C2 | **Gray text on colored background** | Gray text on a colored background lacks contrast | `design-quality.md` §7 self-check |
| C3 | **Gradient text** | Decorative gradient text | Already present; strengthen in self-check |

### Layout and Spacing

| # | Anti-pattern | Description | Where to add |
|---|---|---|---|
| L1 | **Nested cards** | Cards nested in cards create visual noise | `design-quality.md` §4 Forbidden Patterns |
| L2 | **Everything centered** | Centering by default lacks hierarchy | `design-quality.md` §4 Forbidden Patterns |
| L3 | **Cramped padding** | Content sits too close to the card edge | `shared.css` minimum padding constraint |
| L4 | **Glassmorphism everywhere** | Blur effects used as decoration | `design-quality.md` §4 Forbidden Patterns |

### Visual Details

| # | Anti-pattern | Description | Where to add |
|---|---|---|---|
| V1 | **Sparklines as decoration** | Meaningless mini-charts used as decoration | `rendering-rules.md` chart rules |
| V2 | **Icon tile stacked above heading** | Small rounded-square icon above a heading | `design-quality.md` §4 Forbidden Patterns |
| V3 | **Reaching for modals by reflex** | Modals interrupt the user's flow | Not applicable to reports; skipped |
| V4 | **Bounce or elastic easing** | Dated bounce animations | `html-shell-template.md` animation constraints |

### Responsive

| # | Anti-pattern | Description | Where to add |
|---|---|---|---|
| R1 | **Amputating features on mobile** | Hiding key features on mobile | `html-shell-template.md` responsive rules |

## Detection Method Classification

Following Impeccable's three detection methods, existing and new rules are classified as:

| Type | Rule IDs | Notes |
|---|---|---|
| CLI (deterministic, machine-scannable) | T1, T2, T3, C1, C3, L3, V4 | Detectable directly via CSS/grep |
| Browser (needs real layout rendering) | L2, C2, L1 | Judged from the rendered result |
| LLM-only (needs semantic understanding) | T4, T5, V1, V2, R1 | Needs AI judgment of whether content is reasonable |

**Execution strategy:** CLI rules are scanned automatically in the `--generate` pre-write validation stage; Browser rules are checked in the review stage through HTML structure analysis; LLM rules act as constraints during generation and as suggestions during review.

## Implementation Plan

| Priority | Change | Affected file | Effort |
|---|---|---|---|
| P0 | Add 5 self-check rules | `design-quality.md` §7 | 5 min |
| P0 | Add 6 forbidden patterns | `design-quality.md` §4 | 5 min |
| P0 | Add letter-spacing upper limit | `design-quality.md` §2 | 2 min |
| P1 | shared.css minimum padding/line-height constraints | `templates/themes/shared.css` | 5 min |
| P1 | Animation easing constraints | `references/html-shell-template.md` | 2 min |
| P2 | Chart sparklines constraints | `references/rendering-rules.md` | 2 min |
| P2 | Responsive feature-hiding constraints | `references/html-shell-template.md` | 2 min |

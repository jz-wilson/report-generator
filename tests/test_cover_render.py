"""Browser-measured contract for the report cover.

The gate proves a declaration exists in the CSS; it cannot prove the result is
full-bleed or readable. That gap is what produced the v1.26.1 anchor-block bug,
where correct-looking rules stopped matching the shipped DOM.

Skipped automatically when playwright is unavailable.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
COVER_REFERENCE = ROOT / "references" / "html-shell" / "cover.md"
THEMES = [
    "corporate-blue",
    "minimal",
    "dark-tech",
    "dark-board",
    "data-story",
    "newspaper",
    "regular-lumen",
    "forest-editorial",
]


def cover_css() -> str:
    """The last ```css fence in cover.md is the cover stylesheet."""
    blocks = re.findall(r"```css\n(.*?)```", COVER_REFERENCE.read_text(encoding="utf-8"), re.DOTALL)
    assert blocks, "cover.md has no ```css block"
    return blocks[-1]


def theme_css(theme: str) -> str:
    return (ROOT / "templates" / "themes" / f"{theme}.css").read_text(encoding="utf-8")


def document(theme: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="{theme}" data-cover="hero"><head><meta charset="utf-8">
<style>
  html, body {{ margin: 0; }}
  .card-mode-btn {{ padding: .28rem .65rem; border-radius: 4px; }}
  .toc-toggle {{ position: fixed; top: .75rem; left: .75rem; background: var(--primary); color: #fff; }}
  .export-btn {{ position: fixed; bottom: 16px; right: 16px; background: var(--primary); color: #fff; }}
{theme_css(theme)}
{cover_css()}
</style></head>
<body>
<button class="toc-toggle" id="toc-toggle-btn">☰</button>
<div class="main-with-toc">
  <section class="report-cover" id="report-cover">
    <p class="cover-eyebrow">LINGEE AIP · SEMANTIC OPERATING LAYER</p>
    <div class="cover-title-row">
      <h1>Build the <span class="cover-highlight">business semantic hub</span> first, then let AI run global fulfillment</h1>
      <button class="card-mode-btn" id="card-mode-btn">⊞ Summary card</button>
    </div>
    <p class="cover-lead">A product and technology plan for global trade supply chain companies: organize ERP, chat tools and data platforms into one explainable, traceable and actionable management platform.</p>
    <p class="cover-meta">2026-08-11 · Internal discussion draft</p>
    <div class="cover-chips">
      <span class="cover-chip">Based on meeting notes: 2026.08.03</span>
      <span class="cover-chip">Reference architecture: Semantic Layer API / MCP</span>
    </div>
    <div class="cover-cards">
      <div class="cover-card" data-accent="true"><p class="cover-card-label">CORE DECISION</p><p class="cover-card-title">The ontology is the starting point</p><p class="cover-card-text">The semantic hub is the product.</p></div>
      <div class="cover-card"><p class="cover-card-label">BUSINESS TARGET</p><p class="cover-card-title">Minute-level response</p><p class="cover-card-text">Humans only handle exceptions.</p></div>
      <div class="cover-card"><p class="cover-card-label">OPERATING MODEL</p><p class="cover-card-title">One loop per week</p><p class="cover-card-text">Two tracks run in parallel.</p></div>
    </div>
    <div class="cover-watermark" aria-hidden="true">ONTOLOGY → CONTEXT → ACTION</div>
  </section>
  <div class="report-wrapper"><section data-section="s"><h2>S</h2><p>body</p></section></div>
</div>
<button class="export-btn" id="export-btn">↓ Export</button>
</body></html>"""


def _channel(value: float) -> float:
    value /= 255
    return value / 12.92 if value <= 0.03928 else ((value + 0.055) / 1.055) ** 2.4


def luminance(rgb: tuple[float, float, float]) -> float:
    red, green, blue = (_channel(component) for component in rgb)
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def parse_rgb(value: str) -> tuple[float, float, float]:
    numbers = [float(n) for n in re.findall(r"[\d.]+", value)]
    assert len(numbers) >= 3, f"unparseable colour {value!r}"
    return numbers[0], numbers[1], numbers[2]


def contrast(foreground: str, background: str) -> float:
    light, dark = sorted(
        (luminance(parse_rgb(foreground)), luminance(parse_rgb(background))), reverse=True
    )
    return (light + 0.05) / (dark + 0.05)


def rendered_contrast(page, selector: str) -> float:
    """Text colour against the cover's painted background."""
    colour = page.eval_on_selector(selector, "el => getComputedStyle(el).color")
    background = page.evaluate(
        """() => {
            const cover = document.getElementById('report-cover');
            const painted = getComputedStyle(cover).backgroundColor;
            if (painted && painted !== 'rgba(0, 0, 0, 0)') return painted;
            const image = getComputedStyle(cover).backgroundImage;
            const stops = image.match(/rgba?\\([^)]*\\)/g) || [];
            return stops.length ? stops[0] : getComputedStyle(document.body).backgroundColor;
        }"""
    )
    return contrast(colour, background)


@pytest.fixture
def cover_page(page):
    page.set_viewport_size({"width": 1280, "height": 900})
    return page


def test_cover_is_full_bleed_without_horizontal_scroll(cover_page):
    cover_page.set_content(document("forest-editorial"))
    width = cover_page.eval_on_selector("#report-cover", "el => el.getBoundingClientRect().width")
    viewport = cover_page.evaluate("document.documentElement.clientWidth")
    assert width == viewport
    assert cover_page.evaluate(
        "document.documentElement.scrollWidth <= document.documentElement.clientWidth"
    )


def test_cover_fills_the_first_screen(cover_page):
    cover_page.set_content(document("forest-editorial"))
    height = cover_page.eval_on_selector("#report-cover", "el => el.getBoundingClientRect().height")
    assert height >= cover_page.evaluate("window.innerHeight") - 1


@pytest.mark.parametrize("theme", THEMES)
def test_lead_and_headline_are_legible_in_every_theme(cover_page, theme):
    cover_page.set_content(document(theme))
    assert rendered_contrast(cover_page, ".cover-lead") >= 4.5, f"{theme}: lead too faint"
    assert rendered_contrast(cover_page, ".cover-title-row h1") >= 3.0, f"{theme}: headline too faint"


def test_highlight_span_uses_the_cover_highlight_variable(cover_page):
    cover_page.set_content(document("forest-editorial"))
    span = cover_page.eval_on_selector(".cover-highlight", "el => getComputedStyle(el).color")
    declared = cover_page.evaluate(
        "getComputedStyle(document.documentElement).getPropertyValue('--cover-highlight').trim()"
    )
    resolved = cover_page.evaluate(
        """(value) => {
            const probe = document.createElement('span');
            probe.style.color = value;
            document.body.appendChild(probe);
            const computed = getComputedStyle(probe).color;
            probe.remove();
            return computed;
        }""",
        declared,
    )
    assert span == resolved
    headline = cover_page.eval_on_selector(".cover-title-row h1", "el => getComputedStyle(el).color")
    assert span != headline, "highlight must differ from the headline colour"


def test_accent_card_is_filled_and_the_others_are_not(cover_page):
    cover_page.set_content(document("forest-editorial"))
    accent = cover_page.eval_on_selector(
        ".cover-card[data-accent]", "el => getComputedStyle(el).backgroundColor"
    )
    plain = cover_page.eval_on_selector(
        ".cover-card:not([data-accent])", "el => getComputedStyle(el).backgroundColor"
    )
    assert accent != plain


def test_fixed_chrome_stays_legible_over_the_cover(cover_page):
    cover_page.set_content(document("forest-editorial"))
    for selector in ("#toc-toggle-btn", "#export-btn"):
        colour = cover_page.eval_on_selector(selector, "el => getComputedStyle(el).color")
        background = cover_page.eval_on_selector(
            selector, "el => getComputedStyle(el).backgroundColor"
        )
        assert contrast(colour, background) >= 3.0, f"{selector} unreadable on the cover"


def test_narrow_viewport_stacks_the_cards_and_releases_the_height(cover_page):
    cover_page.set_viewport_size({"width": 768, "height": 900})
    cover_page.set_content(document("forest-editorial"))
    columns = cover_page.eval_on_selector(
        ".cover-cards", "el => getComputedStyle(el).gridTemplateColumns"
    )
    assert len(columns.split()) == 1, f"cards did not stack: {columns}"
    assert cover_page.eval_on_selector("#report-cover", "el => getComputedStyle(el).minHeight") == "auto"
    assert cover_page.eval_on_selector(".cover-watermark", "el => getComputedStyle(el).display") == "none"


NEUTRAL_COVER_BG = "rgb(20, 24, 27)"  # the shared #14181b fallback


def test_forest_cover_uses_its_own_palette_not_the_neutral_fallback(cover_page):
    """forest-editorial sets --cover-bg to a green gradient in its base :root.

    A set custom property must beat the use-site fallback regardless of the CSS
    load order, so the cover must render forest's gradient, never the neutral
    #14181b default that every other theme falls back to.
    """
    cover_page.set_content(document("forest-editorial"))
    style = cover_page.eval_on_selector(
        "#report-cover",
        "el => { const s = getComputedStyle(el); return {image: s.backgroundImage, color: s.backgroundColor}; }",
    )
    assert "gradient" in style["image"], f"forest cover is not a gradient: {style}"
    assert style["color"] != NEUTRAL_COVER_BG, f"forest cover fell back to neutral: {style}"
    stops = re.findall(r"rgba?\(([^)]*)\)", style["image"])
    assert stops, f"forest gradient carries no colour stops: {style['image']}"
    greens = [parse_rgb(stop)[1] for stop in stops]
    assert any(green > 24 for green in greens), (
        f"forest gradient lacks a green channel distinct from neutral: {style['image']}"
    )


def test_non_forest_theme_falls_back_to_the_neutral_cover_background(cover_page):
    """minimal declares no --cover-* overrides, so the use-site fallback paints #14181b."""
    cover_page.set_content(document("minimal"))
    style = cover_page.eval_on_selector(
        "#report-cover",
        "el => { const s = getComputedStyle(el); return {image: s.backgroundImage, color: s.backgroundColor}; }",
    )
    assert style["image"] == "none", f"minimal cover unexpectedly painted an image: {style}"
    assert style["color"] == NEUTRAL_COVER_BG, f"minimal cover is not the neutral #14181b: {style}"

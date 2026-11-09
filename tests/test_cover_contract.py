"""Quality gate assertions for the report cover.

The gate reads HTML and never the IR, so `data-cover="hero"` on <html> is the
only evidence that a cover was requested. Without it a render that dropped the
cover looks like an ordinary report.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests"))

from html_quality_gate import (  # noqa: E402
    _CoverStructure,
    extract_cover_mode,
    validate_cover,
)


def document(
    *,
    theme: str = "forest-editorial",
    cover_attr: str = ' data-cover="hero"',
    cover_body: str = "",
    cover_inside_wrapper: bool = False,
    cover_after_wrapper: bool = False,
    extra_h1: str = "",
    render_mode: str = "",
) -> str:
    cover = f"""<section class="report-cover" id="report-cover">
      <div class="cover-title-row"><h1>T</h1>
      <button class="card-mode-btn" id="card-mode-btn">S</button></div>
      <p class="cover-lead">L</p>{cover_body}
    </section>"""
    if cover_inside_wrapper:
        main = f'<div class="main-with-toc"><div class="report-wrapper">{cover}{extra_h1}</div></div>'
    elif cover_after_wrapper:
        main = f'<div class="main-with-toc"><div class="report-wrapper">{extra_h1}</div>{cover}</div>'
    else:
        main = f'<div class="main-with-toc">{cover}<div class="report-wrapper">{extra_h1}</div></div>'
    return (
        f'<!DOCTYPE html><html lang="en" data-template="kai-report-creator"'
        f' data-version="9.9.9" data-theme="{theme}"{cover_attr}{render_mode}>'
        f"<head><title>T</title></head><body>{main}</body></html>"
    )


def codes(html: str) -> list[str]:
    return [f.code for f in validate_cover(html)]


def test_extract_cover_mode_reads_the_html_marker():
    assert extract_cover_mode(document()) == "hero"
    assert extract_cover_mode(document(cover_attr="")) is None


def test_conforming_cover_produces_no_findings():
    assert codes(document()) == []


def test_forest_editorial_without_the_marker_is_a_finding():
    html = document(theme="forest-editorial", cover_attr="")
    assert "cover.missing_for_theme" in codes(html)


def test_other_themes_without_the_marker_are_fine():
    assert codes(document(theme="minimal", cover_attr="")) == []


def test_marker_without_a_cover_element_is_a_finding():
    html = document().replace('id="report-cover"', 'id="not-the-cover"')
    assert "cover.missing" in codes(html)


def test_cover_nested_inside_the_wrapper_is_a_finding():
    html = document(cover_inside_wrapper=True)
    assert "cover.nested_in_wrapper" in codes(html)


def test_cover_placed_after_the_wrapper_is_a_finding():
    html = document(cover_after_wrapper=True)
    assert "cover.after_wrapper" in codes(html)


def test_second_h1_outside_the_cover_is_a_finding():
    html = document(extra_h1="<h1>duplicate</h1>")
    finding = next(f for f in validate_cover(html) if f.code == "cover.h1_count")
    assert "found 2" in finding.message

    structure = _CoverStructure()
    structure.feed(html)
    assert (structure.h1_total, structure.h1_in_cover) == (2, 1)


def test_the_single_h1_must_live_in_the_cover():
    html = document().replace("<h1>T</h1>", "").replace(
        '<div class="report-wrapper">', '<div class="report-wrapper"><h1>T</h1>'
    )
    assert "cover.h1_outside" in codes(html)


def test_h1_inside_an_inert_element_is_not_a_heading():
    for tag in ("template", "textarea"):
        html = document(cover_body=f"<{tag}><h1>ghost</h1></{tag}>")
        assert codes(html) == [], tag


def test_inert_text_inside_the_cover_stays_out_of_cover_text():
    html = document(cover_body='<script>const open = "[" + "[";</script>')
    structure = _CoverStructure()
    structure.feed(html)
    assert "[" not in structure.cover_text
    assert "L" in structure.cover_text
    assert codes(html) == []


def test_the_title_text_is_captured_even_though_title_is_inert():
    html = document().replace("<title>T</title>", "<title>Report [[name]]</title>")
    structure = _CoverStructure()
    structure.feed(html)
    assert structure.title_text == "Report [[name]]"
    assert "[[name]]" not in structure.cover_text


def cards(count: int, accents: int = 1) -> str:
    items = []
    for index in range(count):
        accent = ' data-accent="true"' if index < accents else ""
        items.append(f'<div class="cover-card"{accent}><p>c{index}</p></div>')
    return '<div class="cover-cards">' + "".join(items) + "</div>"


def chips(count: int) -> str:
    items = "".join(f'<span class="cover-chip">c{i}</span>' for i in range(count))
    return f'<div class="cover-chips">{items}</div>'


def test_three_cards_with_one_accent_is_allowed():
    assert codes(document(cover_body=cards(3))) == []


def test_two_cards_is_a_finding():
    assert "cover.card_count" in codes(document(cover_body=cards(2)))


def test_four_cards_is_a_finding():
    assert "cover.card_count" in codes(document(cover_body=cards(4)))


def test_two_accent_cards_is_a_finding():
    assert "cover.accent_count" in codes(document(cover_body=cards(3, accents=2)))


def test_four_chips_is_allowed_and_five_is_a_finding():
    assert codes(document(cover_body=chips(4))) == []
    assert "cover.chip_count" in codes(document(cover_body=chips(5)))


def test_watermark_must_be_hidden_from_assistive_tech():
    exposed = '<div class="cover-watermark">GHOST</div>'
    assert "cover.watermark_exposed" in codes(document(cover_body=exposed))
    hidden = '<div class="cover-watermark" aria-hidden="true">GHOST</div>'
    assert codes(document(cover_body=hidden)) == []


def test_unconsumed_highlight_marker_is_a_finding():
    html = document().replace("<h1>T</h1>", "<h1>Build the [[semantic hub]] first</h1>")
    assert "cover.marker_residue" in codes(html)


def test_marker_residue_in_the_title_element_is_a_finding():
    html = document().replace("<title>T</title>", "<title>Build the [[semantic hub]] first</title>")
    assert "cover.marker_residue" in codes(html)


def test_double_bracket_in_body_prose_is_not_a_finding():
    """The check is scoped to the cover and <title>; a code sample elsewhere is fine."""
    html = document().replace(
        '<div class="report-wrapper">', '<div class="report-wrapper"><pre>arr[[0]]</pre>'
    )
    assert codes(html) == []


def test_svg_title_marker_does_not_trip_marker_residue():
    """An inline <svg><title> icon label is not the document title; [[ inside it is fine."""
    html = document(cover_body='<svg><title>Icon [[x]]</title></svg>')
    assert "cover.marker_residue" not in codes(html)


def test_head_title_marker_still_trips_marker_residue():
    """A real <head><title> carrying [[ is still a residue finding."""
    html = document().replace("<title>T</title>", "<title>Deck [[topic]]</title>")
    assert "cover.marker_residue" in codes(html)


def test_single_card_button_inside_the_cover_is_allowed():
    assert codes(document()) == []


def test_missing_card_mode_button_is_a_finding():
    html = document().replace(
        '<button class="card-mode-btn" id="card-mode-btn">S</button>', ""
    )
    assert "cover.card_button_count" in codes(html)


def test_second_card_mode_button_is_a_finding():
    html = document(cover_body='<button id="card-mode-btn">dup</button>')
    assert "cover.card_button_count" in codes(html)


def test_card_mode_button_outside_the_cover_is_a_finding():
    html = (
        document()
        .replace('<button class="card-mode-btn" id="card-mode-btn">S</button>', "")
        .replace(
            '<div class="report-wrapper">',
            '<div class="report-wrapper"><button id="card-mode-btn">S</button>',
        )
    )
    assert "cover.card_button_outside" in codes(html)


def test_cover_plus_animated_mode_is_a_conflict():
    html = document(render_mode=' data-render-mode="animated" data-animation="scrollytelling"')
    assert "contract_conflict" in codes(html)


def test_run_checks_includes_cover_findings():
    from html_quality_gate import validate_html_text

    result = validate_html_text(document(cover_inside_wrapper=True))
    assert "cover.nested_in_wrapper" in [f["code"] for f in result["findings"]]


def test_cover_reference_carries_the_contract_markers():
    from reference_loader import SHELL_REFERENCE_FILES, read_reference

    assert "references/html-shell/cover.md" in SHELL_REFERENCE_FILES
    text = read_reference("references/html-shell/cover.md")
    for marker in (
        'id="report-cover"',
        "cover-title-row",
        "cover-lead",
        "cover-chip",
        "cover-card",
        "cover-watermark",
        "--cover-bg",
        "--cover-ink",
        "--cover-accent",
        "--cover-highlight",
        "min-height: 100svh",
        "break-after: page",
        "[[",
    ):
        assert marker in text, f"cover.md is missing {marker!r}"


def test_forest_editorial_theme_declares_its_cover_override():
    css = (ROOT / "templates" / "themes" / "forest-editorial.css").read_text(encoding="utf-8")
    assert "--cover-bg:" in css
    assert "--fe-anchor" in css.split("--cover-bg:")[1].split(";")[0]

"""The shared CSS must drop spatial movement when the reader asks for reduced motion."""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
PAGES = sorted(
    [p for p in (ROOT / "templates" / "en").glob("*.html")]
    + [p for p in (ROOT / "examples" / "en").glob("*.html")]
)
SOURCES = [
    ROOT / "templates" / "themes" / "shared.css",
    ROOT / "references" / "html-shell" / "shared-component-css.md",
]
SETUP = """() => {
  document.body.classList.remove('no-animations');
  const el = document.querySelector('.fade-in-up');
  if (!el) return false;
  el.classList.remove('visible');
  el.style.transition = 'none';
  return true;
}"""
READ = "() => getComputedStyle(document.querySelector('.fade-in-up')).transform"


@pytest.mark.parametrize("path", SOURCES, ids=lambda p: p.name)
def test_shared_css_has_a_reduced_motion_rule(path):
    css = path.read_text(encoding="utf-8")
    assert "@media (prefers-reduced-motion: reduce)" in css
    block = css.split("@media (prefers-reduced-motion: reduce)", 1)[1].split("}", 2)[0]
    assert "transform: none" in block
    assert "transition: opacity" in block


@pytest.mark.parametrize("path", PAGES, ids=lambda p: p.parent.name + "/" + p.name)
def test_reduced_motion_removes_the_entrance_movement(path, page):
    page.emulate_media(reduced_motion="no-preference")
    page.goto(f"file://{path}")
    if not page.evaluate(SETUP):
        pytest.skip("page has no .fade-in-up element")
    assert page.evaluate(READ) != "none", "entrance movement should apply by default"

    page.emulate_media(reduced_motion="reduce")
    assert page.evaluate(READ) == "none", "reduced motion should remove the movement"


def test_animated_shell_requires_a_reduced_motion_path():
    overview = (ROOT / "references" / "animated-shell" / "overview.md").read_text(encoding="utf-8")
    assert "## Reduced motion" in overview
    assert "prefers-reduced-motion: reduce" in overview
    assert "behavior:'auto'" in overview
    assert "static frame" in overview
    assert "Emulate `prefers-reduced-motion: reduce`" in overview

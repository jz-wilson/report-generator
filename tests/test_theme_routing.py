"""Theme routing tests — the keyword table had no coverage at all.

`resolve_theme` is first-match-wins over `THEME_KEYWORDS` and matches substrings
across the whole IR, so row order *is* the contract. These tests pin the
precedence decisions that are easy to break by appending a row in the wrong
place, and mirror the table in `references/theme-routing.md`.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from context_isolation import resolve_theme  # noqa: E402


def ir(title: str, body: str = "Placeholder content") -> str:
    return f"---\ntitle: {title}\n---\n\n## Overview\n\n{body}\n"


@pytest.mark.parametrize(
    "title,expected",
    [
        ("Q3 Project Retrospective", "forest-editorial"),
        ("Org Restructuring Proposal", "forest-editorial"),
        ("Launch Retrospective", "forest-editorial"),
        ("Pricing Proposal", "forest-editorial"),
    ],
)
def test_retrospective_summary_and_proposal_route_to_forest_editorial(title, expected):
    assert resolve_theme(ir(title)) == expected


@pytest.mark.parametrize(
    "title,expected",
    [
        ("Week 32 Weekly Report", "regular-lumen"),  # explicit periodic wins
        ("July Monthly Retrospective", "regular-lumen"),  # ...even when it says retrospective
        ("Q3 Quarterly Sales Report", "corporate-blue"),  # business signal wins
        ("Payment Gateway API Proposal", "dark-tech"),  # technical signal wins
        ("Industry Trend Review", "newspaper"),  # industry signal wins
    ],
)
def test_sharper_signals_outrank_forest_editorial(title, expected):
    assert resolve_theme(ir(title)) == expected


@pytest.mark.parametrize(
    "title,expected",
    [
        ("Annual Growth Story", "data-story"),
    ],
)
def test_data_story_keeps_the_data_shaped_narrative(title, expected):
    assert resolve_theme(ir(title)) == expected


def test_bare_summary_section_does_not_hijack_the_theme():
    """A "Summary" section is in almost every report; only compound phrases route."""
    assert resolve_theme(ir("Payment Success Rate Deep Dive", "## Summary\n\nConclusion.")) == "corporate-blue"


def test_explicit_frontmatter_theme_still_wins():
    text = "---\ntitle: Project Retrospective\ntheme: minimal\n---\n\n## Overview\n\nContent\n"
    assert resolve_theme(text) == "minimal"


def test_unmatched_text_falls_back_to_corporate_blue():
    assert resolve_theme(ir("Store shift schedule")) == "corporate-blue"

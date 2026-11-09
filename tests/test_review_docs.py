from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REVIEW_CHECKLIST = ROOT / "references" / "review-checklist.md"


def read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_review_checklist_exists():
    assert REVIEW_CHECKLIST.exists(), "references/review-checklist.md should exist"


def test_review_checklist_contains_expected_rule_sections():
    src = REVIEW_CHECKLIST.read_text(encoding="utf-8")
    assert "### 1.1 BLUF Opening" in src
    assert "### 1.2 Heading Stack Logic" in src
    assert "### 1.3 Anti-Template Section Headings" in src
    assert "### 1.4 Prose Wall Detection" in src
    assert "### 1.5 Takeaway After Data" in src
    assert "### 2.1 Insight Over Data" in src
    assert "### 2.2 Scan-Anchor Coverage" in src
    assert "### 2.3 Conditional Reader Guidance" in src
    assert "## Rejected Candidates" in src


def test_skill_documents_review_mode_and_generate_review_pass():
    src = read("SKILL.md")
    assert "--review [file]" in src
    assert "references/review-checklist.md" in src
    assert "silent final review pass" in src
    assert "one-pass automatic refinement" in src


def test_readmes_expose_review_mode_consistently():
    readme_en = read("README.md")

    assert "/report --review" in readme_en
    assert "14-checkpoint" in readme_en
    assert "silent final review" in readme_en
    assert "review-report-template.md" in readme_en


def test_design_quality_links_l0_and_l1_review_layers():
    src = read("references/design-quality.md")
    assert "## L1 Content Review" in src
    assert "review-checklist.md" in src
    assert "L0 (Visual)" in src
    assert "L1 (Content)" in src


def test_review_report_template_exists_and_is_documented():
    src = read("references/review-report-template.md")
    assert "# Review Report Template" in src
    assert "## Triggered Checkpoints" in src
    assert "## Files" in src

    skill = read("SKILL.md")
    assert "review-report-template.md" in skill


def test_design_refine_passes_are_routed_and_indexed():
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    index = (ROOT / "references" / "INDEX.md").read_text(encoding="utf-8")
    entry = (ROOT / "references" / "design-refine.md").read_text(encoding="utf-8")
    passes = {
        "references/design-refine/critique.md": ["critique"],
        "references/design-refine/audit.md": ["audit"],
        "references/design-refine/passes.md": [
            "typeset", "layout", "color", "distill", "clarify",
            "harden", "adapt", "motion", "polish",
        ],
    }

    assert "--focus <pass>" in skill
    assert "references/design-refine.md" in skill
    assert "`design-refine.md`" in index
    for path, names in passes.items():
        assert (ROOT / path).is_file(), f"missing {path}"
        assert f"`{path}`" in entry, f"design-refine.md should route to {path}"
        assert f"`{path.removeprefix('references/')}`" in index, f"INDEX.md should list {path}"
        body = (ROOT / path).read_text(encoding="utf-8")
        for name in names:
            assert name in skill, f"SKILL.md should name the {name} pass"
            assert f"`{name}`" in entry, f"design-refine.md should list the {name} pass"
            if path.endswith("passes.md"):
                assert f"## `{name}`" in body, f"passes.md is missing the {name} pass"


def test_plan_flow_has_a_brief_check_that_never_asks_for_style():
    plan = (ROOT / "references" / "plan-flow.md").read_text(encoding="utf-8")
    assert "Brief check" in plan
    assert "audience" in plan and "decision_goal" in plan
    assert "Never ask for colors, fonts, or style" in plan

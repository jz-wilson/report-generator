from pathlib import Path

from evals.contract_checks import (
    extract_block,
    validate_chart,
    validate_diagram,
    validate_kpi,
    validate_timeline,
)


ROOT = Path(__file__).resolve().parent.parent


def test_kpi_canonical_yaml_is_valid():
    body = """
items:
  - label: Total revenue
    value: $24.5M
    delta: ↑12%
    note: YoY
""".strip()
    assert validate_kpi(body) == {"status": "valid"}


def test_kpi_short_line_is_accepted_for_compatibility():
    body = "- Revenue: $2.45M ↑12%"
    assert validate_kpi(body) == {"status": "valid"}


def test_kpi_sentence_value_is_invalid_semantics():
    body = """
items:
  - label: Capability description
    value: Supports statistical summaries and trend analysis for CSV and Excel files
""".strip()
    assert validate_kpi(body) == {
        "status": "invalid_semantics",
        "auto_downgrade_target": "callout",
    }


def test_kpi_placeholder_value_is_invalid_for_any_report_class():
    body = """
items:
  - label: Metric A
    value: [INSERT VALUE]
""".strip()
    assert validate_kpi(body, report_class="data") == {
        "status": "invalid_semantics",
        "auto_downgrade_target": "callout",
    }


def test_kpi_value_must_be_quantitative():
    body = """
items:
  - label: Status
    value: Passed
""".strip()
    assert validate_kpi(body, report_class="data") == {
        "status": "invalid_semantics",
        "auto_downgrade_target": "callout",
    }


def test_timeline_requires_whitelisted_dates():
    good = "- 2024-10-15: Launch\n- Q4 2024: Expansion"
    bad = "- Core principle: sincere service\n- Core capability: professional and efficient"
    assert validate_timeline(good) == {"status": "valid"}
    assert validate_timeline(bad) == {
        "status": "invalid_semantics",
        "auto_downgrade_target": "list",
    }


def test_timeline_missing_date_separator_is_invalid_syntax():
    body = "- 2024-10-15 Launch"
    assert validate_timeline(body) == {
        "status": "invalid_syntax",
        "auto_downgrade_target": "list",
    }


def test_chart_requires_schema_for_each_type():
    standard = """
labels: [Jul, Aug, Sep]
datasets:
  - label: Actual
    data: [1, 2, 3]
""".strip()
    sankey = """
nodes: [A, B]
links: [A->B:120]
""".strip()
    broken = "datasets:\n  - label: Actual"

    assert validate_chart("line", standard) == {"status": "valid"}
    assert validate_chart("sankey", sankey) == {"status": "valid"}
    assert validate_chart("line", broken) == {
        "status": "invalid_syntax",
        "auto_downgrade_target": "table",
    }


def test_chart_placeholder_only_block_in_narrative_is_invalid_semantics():
    body = """
labels: [A, B]
datasets:
  - label: Placeholder
    data: [[INSERT VALUE], [INSERT VALUE]]
""".strip()
    assert validate_chart("bar", body, report_class="narrative") == {
        "status": "invalid_semantics",
        "auto_downgrade_target": "table",
    }


def test_diagram_requires_type_specific_schema():
    sequence = """
actors: [User, Claude]
steps:
  - from: User
    to: Claude
    msg: Request
""".strip()
    flowchart_broken = """
nodes:
  - id: start
    kind: oval
    label: Start
""".strip()

    assert validate_diagram("sequence", sequence) == {"status": "valid"}
    assert validate_diagram("flowchart", flowchart_broken) == {
        "status": "invalid_syntax",
        "auto_downgrade_target": "callout",
    }


def test_examples_follow_the_documented_contract():
    business = (ROOT / "examples" / "business-report.report.md").read_text(encoding="utf-8")
    tech = (ROOT / "examples" / "tech-doc.report.md").read_text(encoding="utf-8")

    _, business_kpi = extract_block(business, "kpi")
    assert validate_kpi(business_kpi) == {"status": "valid"}

    line_header, business_chart = extract_block(business, "chart")
    assert "type=line" in line_header
    assert validate_chart("line", business_chart) == {"status": "valid"}

    _, business_timeline = extract_block(business, "timeline")
    assert validate_timeline(business_timeline) == {"status": "valid"}

    diagram_header, tech_diagram = extract_block(tech, "diagram")
    assert "type=sequence" in diagram_header
    assert validate_diagram("sequence", tech_diagram) == {"status": "valid"}

# Periodic Report Content Extraction Rules

**Load when:** `theme: regular-lumen` OR keywords `daily|weekly|monthly|periodic report`.

## Extraction Rules

**1. Core KPIs** (render only when real metrics exist): use a KPI block only when the source provides short, explicit, verifiable quantitative metrics. Optional metrics include projects completed (`X/Y`), progress percentage (`XX%`), risk/blocker count (`N`), and ad-hoc requests handled (`N`).

Do not force KPIs into a periodic report layout. Dates, week numbers, version numbers, and section numbers are not KPIs. If there are no real business/work numbers, omit the KPI block and carry the period overview in a callout, timeline, table, or plain paragraph; use an empty array for `report-summary.kpis`.

**2. Project Progress** (three parts):
- Status badge: `In progress` / `Blocked` / `Done`
- Progress-this-period prose
- Timeline: use `MM-DD` when dates exist, `Week N` / `Day N` otherwise; mark future milestones `(future)` → `.timeline-item.future`
- Blocker callout: `.callout--warning` + blocker reason + days affected

**3. Period Divider**: always insert `<hr class="week-divider">` after the current-period sections.

**4. Next Period Plan**: Timeline (future) + a to-be-confirmed callout (`.callout--note`).

**5. Daily Work**: render as a table (`Type|Content|Time spent|Notes`), grouped into routine/ad-hoc.

## Density Rule

The Mixed rule applies: use `:::kpi`/`:::chart` only when the source has real numbers. If the user supplies only a text log ("had meetings, wrote code this week"), structure the narrative with callouts/timelines and **do not invent placeholder KPIs**.

## Section Order

1. Period overview (callout/prose; KPIs only when real metrics exist)
2. Project progress (badge + timeline + callout)
3. Daily work (table)
4. **Period Divider**
5. Next period plan (future timeline + callout)

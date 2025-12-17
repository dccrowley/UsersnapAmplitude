---
title: "SOP: Automated Feedback-to-Journey Analysis Workflow"
version: "1.2"
date: "2025-12-17T14:30:00Z"
owner: "Product Operations / Product Management"
goal: "Compress multi-week manual analysis into a fast, repeatable workflow that triangulates qualitative friction (Usersnap) with quantitative journey drop-off (Amplitude) and outputs an executive brief + a single-file dashboard."
---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.2 | 2025-12-17 | Added critical path identification guidance (Step 1B), iteration/refinement loop (Step 4), validation checklist improvements, sample output descriptions, handling for missing skill files |
| 1.1 | 2025-12-17 | Added semantic thresholds, improved dashboard spec, troubleshooting section |
| 1.0 | 2025-12-15 | Initial release |

---

## 1) Prerequisites

### A) Skill Files (Context Engine)

Upload these **first** so output is consistent and on-brand:

| File | Purpose | What happens if missing |
|------|---------|------------------------|
| `dashboard-design-SKILL.md` | Swiss grid, typography discipline, layout rules | Output may use inconsistent spacing, wrong fonts |
| `palettes-SKILL.md` | Alef palette + semantic colors | Colors may not match brand or accessibility standards |
| `charts-SKILL.md` | Chart rules: direct labels, donut limits, bar-axis rules | Charts may include chartjunk, wrong encodings |
| `stakeholder-communication-SKILL.md` | C-suite structure, simplified language rules | Executive summary may bury the lead or use jargon |

**If skill files are unavailable:** The workflow will still run, but explicitly state in your prompt: *"Apply Swiss design principles, 8-point grid, Fira Sans/Mono typography, WCAG AA contrast, and lead with the decision in the executive summary."*

### B) Data Inputs

Place exports in one folder (or upload to the chat):

**Usersnap export** (`usersnap.csv`)
- Must include (minimum): `Date`, `Category` (Issue/Bug/Feature Request/Positive), `Priority` (High/Critical useful), `Title`, `Description`
- Optional but valuable: `Theme` or `Tags` if pre-categorized

**Amplitude export** (`amplitude.csv`)
- Two supported shapes:
  - **Preferred (pre-aggregated funnel):** `Funnel Step Name`, `Drop-off Count`, `Drop-off %`, `Conversion Rate`
  - **Accepted (event-level):** `Event_Name`, `Task_Completed` plus `Retry_Attempts` / `Time_on_Task_Seconds` if available
    - In this case, derive conversion as: **% of events where `Task_Completed = TRUE`** per step

---

## 2) Workflow Steps

### Step 1A — Context Injection

1. Start a new chat
2. Upload all **4** skill files (or state the fallback instructions)
3. Upload `usersnap.csv` and `amplitude.csv`

### Step 1B — Critical Path Identification (New in v1.2)

Before running the full analysis, identify the critical path. The critical path is where:
- **Quantitative signal:** Highest drop-off rate OR lowest conversion rate in the funnel
- **Qualitative signal:** Most complaint mentions for a single theme
- **Alignment:** Both signals point to the same feature area or step

**Quick identification prompt:**
```
Scan the uploaded data and identify:
1. The journey step(s) with the worst conversion/drop-off
2. The most frequently mentioned complaint theme(s)
3. Whether these align (same feature area, similar user language)

Output a 2-3 sentence summary of the likely critical path before proceeding.
```

If multiple candidates exist with similar severity, flag them for stakeholder input before deep analysis.

### Step 2 — Execution (Master Prompt v1.2)

Copy/paste exactly:

---

**ROLE & OBJECTIVE**
Act as a Lead Product Strategist and Senior UI Engineer. Your goal is to triangulate qualitative teacher friction (Usersnap) with quantitative journey abandonment (Amplitude) to produce a "Feedback-to-Journey" analysis with a single critical path.

**CONTEXT SOURCES**
Govern output with the skill files:
- Design & layout: `dashboard-design-SKILL.md` (8-point grid, Swiss design)
- Colors: `palettes-SKILL.md` (Alef palette + semantic colors)
- Charts: `charts-SKILL.md` (donut ≤5 segments, direct labels, no chartjunk)
- Strategy: `stakeholder-communication-SKILL.md` (C-suite structure, simple language)

**TASK 1 — CRITICAL PATH IDENTIFICATION**
First, identify the critical path by scanning both datasets:
- Find the step(s) with highest drop-off / lowest conversion
- Find the complaint theme(s) with most mentions
- Confirm alignment (or flag divergence for stakeholder review)

State the critical path in one sentence before proceeding.

**TASK 2 — CORRELATION ANALYSIS (Critical Path Focus)**
Analyze `usersnap.csv` against `amplitude.csv`.
- Focus on the identified critical path (e.g., assign-to-student steps, onboarding, checkout).
- If Amplitude is event-level, compute:
  - conversion% per step = % `Task_Completed = TRUE`
  - drop-off% per step = 100 - conversion%
  - include avg retries + avg time-on-task if present (split by success/failure if possible)
- Produce a "mapping table" that links:
  - journey step → drop-off/conversion/attempts → dominant Usersnap theme + mention count

**TASK 3 — EXECUTIVE SUMMARY (Markdown)**
Write a strategic brief for CPO/DoP using the `stakeholder-communication-SKILL.md` structure:
1. **Decision Needed:** Recommendation first (what decision, why now)
2. **The Analysis:** Concise narrative linking qual → quant with specific numbers
3. **Cost of Inaction:** Quantify in operational terms (drop-off rate, retries, time wasted)
4. **The Ask:** Explicit decision + success metrics

**TASK 4 — HTML DASHBOARD (Single File, v1.2 spec)**
Generate a self-contained, interactive HTML dashboard.

**Information Architecture (priority order):**
1. Headline insight card (full-width, top of page) — the story in one sentence
2. KPI row with period context (e.g., "Dec 1–26, 2024")
3. Correlation insight block with decision callout — moved up, not buried
4. Mapping table (qual→quant audit trail)
5. Charts row (comparison bar chart + donut)
6. High-severity feedback feed (max 3 items, link to full list)
7. Method notes (quieter styling, bottom of page)

**Design system:**
- **Structure:** 12-column CSS grid; strict 8-point spacing
- **Typography:** **Fira Sans** for text + **Fira Mono** for numerals (KPIs, right-aligned numeric columns)
- **Color meaning:** Semantic thresholds on drop-off:
  - **Good (green):** drop-off < 30%
  - **Warning (orange):** 30–50%
  - **Concerning (red):** ≥ 50%
- **Categorical data (donut):** Use single-hue palette (e.g., blues) — color should NOT imply severity for neutral categories
- **Complaint cards:** Amber/yellow for High, red only for Critical

**Required components:**
- Headline insight (story-first, full-width)
- KPI cards: total complaints, high severity %, worst drop-off (with period context)
- Comparison chart (e.g., standard vs differentiated) with **semantic colors** and legend
- Donut chart of complaint categories (≤5 segments) with visible legend below
- Correlation insight block with teacher quotes
- Decision callout box (what decision is needed)
- "Feedback mapped to steps" table (audit trail)
- "Recent high-severity feedback" feed (max 3 items)
- Method notes (quieter styling)

**Interaction & motion (subtle):**
- Hover tooltips for bars + donut segments (D3)
- Hover emphasis (slight scale/radius changes)
- Respect `prefers-reduced-motion`

**OUTPUT ORDER:**
1. Critical path statement (1-2 sentences)
2. Executive Summary (Task 3)
3. HTML Dashboard (Task 4)

---

### Step 3 — Validation Checklist (v1.2)

Run through this checklist before sharing outputs:

**Visual system:**
- [ ] Alef palette + semantic colors used correctly
- [ ] Strict 8px grid (no arbitrary spacing like 10px, 15px, 22px)
- [ ] Fira Sans + Fira Mono loaded and applied
- [ ] WCAG AA: text contrast 4.5:1, graphics 3:1
- [ ] Donut uses neutral single-hue palette (not semantic colors for categories)

**Information architecture:**
- [ ] Headline insight is FIRST (top of dashboard, full-width)
- [ ] Correlation insight + decision callout appear BEFORE charts
- [ ] KPIs include period context (dates)
- [ ] Complaint feed is limited to 3 items with "see more" note
- [ ] Method notes are visually quieter than insights

**Charts:**
- [ ] Donut ≤5 segments, has visible legend below
- [ ] Bar comparisons start at zero
- [ ] Semantic state (green/orange/red) matches thresholds and has legend
- [ ] Direct labels used where possible

**Storytelling:**
- [ ] Critical path is stated explicitly
- [ ] Qual and quant are linked with specific numbers
- [ ] Teacher quotes are included (human voice)
- [ ] Decision callout is present with success criteria

**Strategy:**
- [ ] Executive brief starts with the decision + recommendation
- [ ] Language is short, direct, non-jargony
- [ ] Cost of inaction is quantified

### Step 4 — Iteration & Refinement Loop (New in v1.2)

After initial output, review against the checklist. If issues are found:

1. **Identify specific issues** (e.g., "donut uses red for Feature Request", "insight block is below charts")
2. **Request targeted fix:**
   ```
   Please revise the dashboard:
   - Move the correlation insight block above the charts row
   - Change donut palette to single-hue blues
   - Add period dates to KPI footer text
   ```
3. **Re-validate** using the checklist
4. **Repeat** until all checks pass (typically 1-2 iterations)

**When to escalate vs. iterate:**
- Iterate: Visual/layout issues, missing components, color problems
- Escalate to stakeholder: Ambiguous critical path (multiple candidates), data quality concerns, conflicting qual/quant signals

---

## 3) Distribution Strategy

| Stakeholder | Artifact | Message focus |
|---|---|---|
| CPO / DoP | Executive Summary | Decision + impact + explicit ask |
| PMs / Designers | HTML Dashboard | Where drop-off happens + user quotes + mapped themes |
| HOPs | Both | Validate process + advocate resources |

**Distribution tips:**
- Send Executive Summary as email body, Dashboard as attachment or hosted link
- For CPO/DoP: Lead with the decision, link to dashboard for detail
- For PMs/Designers: Lead with the dashboard, reference executive summary for context

---

## 4) Troubleshooting

| Problem | Diagnosis | Fix |
|---------|-----------|-----|
| Dashboard feels generic | Missing brand elements | Enforce 8-point spacing, Alef palette variables, Fira typography, semantic state colors |
| Analysis feels vague | Missing mapping table | Force the mapping table (step → drop-off → theme count + quotes) and state critical path explicitly |
| Amplitude export isn't a funnel table | Event-level data | Derive conversion/drop-off per step from `Task_Completed` and label as "Amplitude-derived" |
| Multiple possible critical paths | Ambiguous data | Flag for stakeholder, present top 2-3 candidates with supporting numbers |
| Donut colors imply wrong severity | Semantic colors on neutral categories | Switch to single-hue categorical palette (blues or grays) |
| Insight buried mid-page | Wrong IA order | Move headline insight to top, correlation insight above charts |
| Too many complaint cards | Visual overload | Limit to 3, add "showing X of Y" note |
| Method notes compete with insights | Equal visual weight | Apply quieter styling (smaller text, muted background, bottom placement) |

---

## 5) Sample Outputs

### Executive Summary Structure
```
# Executive Summary (Decision First)

**Decision needed:** [One sentence: what to prioritize]

**Why now:** [One sentence: the headline metric + qual alignment]

---

## The Analysis
[2-3 paragraphs with specific numbers, comparison table, teacher quotes]

## Cost of Inaction
[Bulleted list: what happens if we don't act]

## The Ask
[Numbered list: specific interventions + success metrics]
```

### Dashboard Layout (visual order)
```
┌─────────────────────────────────────────────┐
│ HEADLINE INSIGHT (full-width, dark bg)      │
│ "Differentiated assignment fails 81%..."    │
└─────────────────────────────────────────────┘
┌─────────────┬─────────────┬─────────────────┐
│ KPI Card 1  │ KPI Card 2  │ KPI Card 3      │
│ Complaints  │ Severity %  │ Drop-off %      │
└─────────────┴─────────────┴─────────────────┘
┌─────────────────────────────────────────────┐
│ THE STORY: Correlation Insight              │
│ [Insight block + quotes + decision callout] │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ MAPPING TABLE (full-width)                  │
│ Step | Conv | Drop | Attempts | Theme | N   │
└─────────────────────────────────────────────┘
┌─────────────────────┬───────────────────────┐
│ Bar Chart           │ Donut + Legend        │
│ (semantic colors)   │ (single-hue blues)    │
└─────────────────────┴───────────────────────┘
┌─────────────────────┬───────────────────────┐
│ Complaint Feed (3)  │ Method Notes (quiet)  │
└─────────────────────┴───────────────────────┘
```

---

## 6) Appendix: Quick Reference

### Semantic Thresholds
| State | Drop-off % | Color |
|-------|------------|-------|
| Good | < 30% | Green (`#10B981`) |
| Warning | 30–50% | Orange (`#F59E0B`) |
| Concerning | ≥ 50% | Red (`#EF4444`) |

### Complaint Card Severity
| Priority | Background | Border |
|----------|------------|--------|
| High | Amber tint | Amber left border |
| Critical | Red tint | Red left border |

### Donut Palette (categorical, neutral)
```css
--cat-blue-1: #0D88E6;
--cat-blue-2: #47A8E5;
--cat-blue-3: #7BC4EA;
--cat-blue-4: #A8D8F0;
--cat-blue-5: #D4ECF7;
```

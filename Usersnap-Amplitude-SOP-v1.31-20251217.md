---
title: "SOP: Automated Feedback-to-Journey Analysis Workflow"
version: "1.31"
date: "2025-12-17T17:00:00Z"
owner: "Product Operations / Product Management"
goal: "Compress multi-week manual analysis into a fast, repeatable workflow that triangulates qualitative friction (Usersnap) with quantitative journey drop-off (Amplitude) and outputs an executive brief + a single-file dashboard."
---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.31 | 2025-12-17 | Added storytelling components: Insight Block with narrative + teacher quotes, Feedback Mapped to Journey Steps table, Recent High-Severity Feedback feed (3 cards), Method Notes section. Updated IA and validation checklist accordingly. |
| 1.21 | 2025-12-17 | Enhanced dashboard spec: added multi-step funnel visualization, KPI cards with trend indicators, complaint theme donut (replacing category donut), improved header styling, updated sample layout |
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
- **Required for v1.31:** `Theme` column with complaint themes (e.g., "Too many clicks", "Confusing UI", "Time consuming", "Missing feature")
- If themes not present, include in prompt: *"Analyze descriptions and categorize into complaint themes before generating dashboard"*

**Amplitude export** (`amplitude.csv`)
- **Preferred for v1.31 (multi-step funnel):** Sequential steps with `Funnel_Step_Name`, `Funnel_Step_Order`, `Users_At_Step`, `Drop-off_Pct`
- **Accepted (event-level):** `Event_Name`, `Task_Completed` plus `Retry_Attempts` / `Time_on_Task_Seconds` if available
  - In this case, derive conversion as: **% of events where `Task_Completed = TRUE`** per step

---

## 2) Workflow Steps

### Step 1A — Context Injection

1. Start a new chat
2. Upload all **4** skill files (or state the fallback instructions)
3. Upload `usersnap.csv` and `amplitude.csv`

### Step 1B — Critical Path Identification

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

### Step 2 — Execution (Master Prompt v1.31)

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
  - journey step → drop-off/conversion/attempts → dominant Usersnap theme + mention count + representative quote

**TASK 3 — EXECUTIVE SUMMARY (Markdown)**
Write a strategic brief for CPO/DoP using the `stakeholder-communication-SKILL.md` structure:
1. **Decision Needed:** Recommendation first (what decision, why now)
2. **The Analysis:** Concise narrative linking qual → quant with specific numbers, including funnel table
3. **Cost of Inaction:** Quantify in operational terms (drop-off rate, retries, time wasted)
4. **The Ask:** Explicit decision + success metrics

**TASK 4 — HTML DASHBOARD (Single File, v1.31 spec)**
Generate a self-contained, interactive HTML dashboard.

**Information Architecture (v1.31 priority order):**
1. **Header bar** (full-width, dark background) — project title, "FAKE DATA" label if applicable
2. **KPI row** (4 cards with trend indicators) — total complaints, high severity %, overall drop-off %, worst step drop-off
3. **Main grid** (two columns):
   - Left: Multi-step funnel chart showing user progression
   - Right: Complaint themes donut (NOT categories like Issue/Bug/Feature Request)
4. **Insight block** (full-width, dark background) — narrative headline, body text, teacher quote cards
5. **Mapping table** — "Feedback Mapped to Journey Steps" (qual→quant audit trail with quotes)
6. **High-severity feedback feed** — 3 complaint cards with "showing X of Y" note
7. **Method notes** (quieter styling, bottom of page)

**Dashboard Components (v1.31 required):**

**Header:**
- Full-width bar with dark background (`#003C71` or similar brand color)
- White text, project title prominent
- Include "FAKE DATA" badge if using synthetic data

**KPI Cards (4 cards):**
Each card must include:
- Label (e.g., "Total Complaints")
- Large value (Fira Mono, bold)
- Trend indicator with direction arrow and change value (e.g., "↑ +42%")
- Trend color: green for good direction, red for bad direction (context-aware)
- Period context in footer (e.g., "Last 30 days")

Example KPIs:
- Total Complaints (with change %)
- High Severity % (with "Getting worse" / "Improving" label)
- Overall Drop-off % (funnel completion inverse)
- Worst Step Drop-off % (with step name)

**Multi-Step Funnel Chart:**
- Horizontal bar chart showing user count at each step
- Steps in funnel order (top to bottom)
- Semantic colors on bars based on step drop-off:
  - Blue (normal): drop-off < 30%
  - Orange (warning): drop-off 30–50%
  - Red (critical): drop-off ≥ 50%
- Direct labels showing user count
- Legend explaining color thresholds
- Hover tooltips with detailed metrics

**Complaint Themes Donut:**
- Show complaint THEMES (not categories like Issue/Bug/Feature Request)
- Example themes: "Too many clicks", "Confusing UI", "Time consuming", "Missing feature"
- Distinct color palette for each theme
- ≤5 segments maximum
- Center showing total count
- Visible legend beside or below chart
- Hover tooltips with count and percentage

**Insight Block (NEW in v1.31):**
- Full-width section with dark background (brand secondary color)
- White text for contrast
- **Headline:** Bold statement with key numbers highlighted (e.g., "loses 89% of teachers", "46% drop-off each")
- **Body text:** 2-3 sentences explaining the qual/quant alignment narrative
- **Quote cards:** 2 teacher quotes in styled cards with author attribution
- Quote cards: semi-transparent background, left border accent, italic text

**Mapping Table — "Feedback Mapped to Journey Steps" (NEW in v1.31):**
- Full-width card with table
- Columns: Journey Step | Drop-off % | Attempts | Top Theme | Mentions | Representative Quote
- Drop-off % color-coded (red for critical, orange for warning, blue for normal)
- Theme displayed as tag/pill
- Quote in italic, muted color
- Links qual complaints directly to quant funnel steps

**High-Severity Feedback Feed (NEW in v1.31):**
- 3-column grid of complaint cards
- Each card includes:
  - Priority badge (Critical = red, High = amber/orange)
  - Date
  - Title (bold)
  - Description
  - Theme tag
- Card styling: left border color matches priority, tinted background
- Footer text: "X high-severity complaints in the last 30 days. Contact Product Ops for full export."

**Method Notes:**
- Quieter styling: smaller text, muted background, subtle border
- Content: Data sources, analysis methodology, drop-off calculation formula, synthetic data disclaimer if applicable

**Design system (v1.31):**
- **Structure:** 12-column CSS grid; strict 8-point spacing (8, 16, 24, 32, 40, 48px)
- **Typography:** **Fira Sans** for text + **Fira Mono** for numerals (KPIs, data values)
- **Color meaning:**
  - Semantic thresholds for drop-off: blue (<30%), orange (30–50%), red (≥50%)
  - Trend indicators: green for improvement, red for degradation (context-aware)
  - Priority badges: red for Critical, amber/orange for High
- **Cards:** White background, subtle shadow, rounded corners (8-12px)
- **Insight block:** Dark background (brand color), white text, accent color for highlights
- **Hover states:** Subtle scale/emphasis, respect `prefers-reduced-motion`

**OUTPUT ORDER:**
1. Critical path statement (1-2 sentences)
2. Executive Summary (Task 3)
3. HTML Dashboard (Task 4)

---

### Step 3 — Validation Checklist (v1.31)

Run through this checklist before sharing outputs:

**Visual system:**
- [ ] Alef palette + semantic colors used correctly
- [ ] Strict 8px grid (no arbitrary spacing like 10px, 15px, 22px)
- [ ] Fira Sans + Fira Mono loaded and applied
- [ ] WCAG AA: text contrast 4.5:1, graphics 3:1
- [ ] Donut uses distinct categorical palette (not semantic red/green for neutral themes)

**Information architecture (v1.31):**
- [ ] Header bar is present with project title
- [ ] KPI cards have trend indicators (arrows + change values)
- [ ] KPI trend colors are context-aware (green = good, red = bad)
- [ ] Funnel chart shows multi-step progression
- [ ] Funnel bars use semantic colors based on drop-off %
- [ ] Donut shows complaint THEMES (not Issue/Bug/Feature categories)
- [ ] **Insight block present with headline, body, and quote cards**
- [ ] **Mapping table present with step → theme → quote linkage**
- [ ] **High-severity feed shows exactly 3 cards with "X of Y" note**
- [ ] Method notes are visually quieter than insights

**Charts:**
- [ ] Funnel bars start at zero
- [ ] Funnel has direct labels (count)
- [ ] Funnel has legend explaining color thresholds
- [ ] Donut ≤5 segments, has visible legend
- [ ] Hover tooltips work on both charts

**Storytelling (v1.31 focus):**
- [ ] Critical path is stated explicitly in insight block headline
- [ ] Headline includes specific numbers (e.g., "89%", "46%")
- [ ] Body text explains qual/quant alignment
- [ ] At least 2 teacher quotes included in insight block
- [ ] Mapping table links specific steps to specific themes with quotes
- [ ] Recent complaints shown with priority, date, description, theme

**Strategy:**
- [ ] Executive brief includes funnel table showing step-by-step drop-off
- [ ] Executive brief starts with the decision + recommendation
- [ ] Language is short, direct, non-jargony
- [ ] Cost of inaction is quantified

### Step 4 — Iteration & Refinement Loop

After initial output, review against the checklist. If issues are found:

1. **Identify specific issues** (e.g., "missing insight block", "mapping table has no quotes", "feedback cards missing theme tags")
2. **Request targeted fix:**
   ```
   Please revise the dashboard:
   - Add insight block with headline "The workflow loses X% of teachers..."
   - Add 2 teacher quote cards to the insight block
   - Add mapping table with columns: Step, Drop-off, Theme, Mentions, Quote
   - Add 3 high-severity feedback cards with priority badges
   ```
3. **Re-validate** using the checklist
4. **Repeat** until all checks pass (typically 1-2 iterations)

**When to escalate vs. iterate:**
- Iterate: Visual/layout issues, missing components, color problems, wrong chart data
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
| Donut shows Issue/Bug/Feature | Wrong data dimension | Specify: use complaint THEMES not Categories |
| KPIs lack trend context | Missing change indicators | Add trend arrows (↑/↓) with change % and context-aware colors |
| Funnel is single bar | Wrong chart type | Request multi-step horizontal bar showing progression through funnel |
| Funnel bars all same color | Missing semantic encoding | Apply semantic colors based on drop-off % thresholds |
| **No storytelling narrative** | Missing insight block | Add insight block with headline, body text, and 2 quote cards |
| **No qual→quant linkage** | Missing mapping table | Add "Feedback Mapped to Journey Steps" table with quotes |
| **No recent complaints visible** | Missing feedback feed | Add 3-card high-severity feed with priority badges and themes |
| Too many complaint cards | Visual overload | Limit to 3, add "showing X of Y" note |
| Method notes compete with insights | Equal visual weight | Apply quieter styling (smaller text, muted background, bottom placement) |

---

## 5) Sample Outputs

### Executive Summary Structure (v1.31)
```
# Executive Summary (Decision First)

**Decision needed:** [One sentence: what to prioritize]

**Why now:** [One sentence: the headline metric + qual alignment]

---

## The Analysis

**Quant (Amplitude, [date range]):**

| Step | Users | Drop-off | Cumulative Loss |
|------|-------|----------|-----------------|
| 1. Step Name | 93 | — | 0% |
| 2. Step Name | 70 | 25% | 25% |
| **3. Worst Step** | 30 | **46%** | 68% |
| ... | ... | ... | ... |

**Qual (Usersnap, N complaints):**

| Theme | Count | % |
|-------|-------|---|
| Theme 1 | 10 | 31% |
| Theme 2 | 10 | 31% |
| ... | ... | ... |

[Teacher quotes]

## Cost of Inaction
[Bulleted list: what happens if we don't act]

## The Ask
[Numbered list: specific interventions + success metrics]
```

### Dashboard Layout (v1.31 visual order)
```
┌─────────────────────────────────────────────────────────┐
│ HEADER BAR (dark bg)                                    │
│ Project Title                          [FAKE DATA]      │
└─────────────────────────────────────────────────────────┘
┌────────────┬────────────┬────────────┬──────────────────┐
│ KPI Card   │ KPI Card   │ KPI Card   │ KPI Card         │
│ 32         │ 66%        │ 89%        │ 46%              │
│ ↑ +42%     │ ↑ Worse    │ ↑ Worse    │ Open Diff.       │
│ Last 30d   │ Last 30d   │ vs target  │ Worst step       │
└────────────┴────────────┴────────────┴──────────────────┘
┌────────────────────────────┬────────────────────────────┐
│ FUNNEL CHART               │ THEMES DONUT               │
│ ▓▓▓▓▓▓▓▓▓▓▓▓ 93           │                            │
│ ▓▓▓▓▓▓▓▓▓░░ 70 (-25%)     │      ┌──────┐              │
│ ▓▓▓▓▓▓▓░░░░ 56 (-20%)     │     /        \             │
│ ▓▓▓░░░░░░░░ 30 (-46%) ORG │    │  DONUT   │             │
│ ▓▓░░░░░░░░░ 24 (-20%)     │     \        /             │
│ ▓░░░░░░░░░░ 13 (-46%) ORG │      └──────┘              │
│ ░░░░░░░░░░░ 10 (-23%)     │ ■ Too many clicks (31%)    │
│                            │ ■ Confusing UI (31%)       │
│ Legend: ■ <30% ■ 30-50%   │ ■ Time consuming (25%)     │
│         ■ ≥50%             │ ■ Missing feature (13%)    │
└────────────────────────────┴────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│ INSIGHT BLOCK (dark bg, white text)                     │
│                                                         │
│ The differentiated assignment workflow loses **89% of   │
│ teachers** across 7 steps, with two critical            │
│ bottlenecks at **46% drop-off each**.                   │
│                                                         │
│ Teachers who attempt differentiated assignments face... │
│                                                         │
│ ┌─────────────────────┐ ┌─────────────────────┐        │
│ │ "The workflow has   │ │ "After configuring  │        │
│ │ way too many steps" │ │ levels I couldn't   │        │
│ │ — Teacher, Dec 2024 │ │ figure out..."      │        │
│ └─────────────────────┘ └─────────────────────┘        │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│ FEEDBACK MAPPED TO JOURNEY STEPS                        │
│ ┌───────────┬────────┬─────┬──────────┬────┬─────────┐ │
│ │ Step      │Drop-off│Atmpt│ Theme    │ N  │ Quote   │ │
│ ├───────────┼────────┼─────┼──────────┼────┼─────────┤ │
│ │ Open Diff │ 46%    │ 56  │ Too many │ 10 │ "The... │ │
│ │ Assign Grp│ 46%    │ 24  │ Confusing│ 10 │ "The... │ │
│ │ Config Lvl│ 20%    │ 30  │ Time con.│  8 │ "Spent..│ │
│ └───────────┴────────┴─────┴──────────┴────┴─────────┘ │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│ RECENT HIGH-SEVERITY FEEDBACK (showing 3 of 21)         │
│ ┌─────────────────┬─────────────────┬─────────────────┐ │
│ │ HIGH            │ CRITICAL        │ CRITICAL        │ │
│ │ 2024-12-20      │ 2024-12-19      │ 2024-12-18      │ │
│ │ Navigation req- │ Minutes turn    │ Multi-step pro- │ │
│ │ uires too many  │ into hours      │ cess is a deal- │ │
│ │ clicks...       │ ...             │ breaker...      │ │
│ │ Theme: Too many │ Theme: Time     │ Theme: Too many │ │
│ └─────────────────┴─────────────────┴─────────────────┘ │
│ 21 high-severity complaints. Contact Product Ops...     │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│ METHODOLOGY (quiet styling)                             │
│ Data sources: Amplitude 7-step funnel (Dec 1-20)...     │
└─────────────────────────────────────────────────────────┘
```

---

## 6) Appendix: Quick Reference

### Semantic Thresholds (Drop-off)
| State | Drop-off % | Color |
|-------|------------|-------|
| Normal | < 30% | Blue (`#1E88E5`) |
| Warning | 30–50% | Orange (`#FB8C00`) |
| Critical | ≥ 50% | Red (`#E53935`) |

### KPI Trend Colors (Context-Aware)
| Metric | Increase = | Decrease = |
|--------|------------|------------|
| Complaints | Red (bad) | Green (good) |
| Severity % | Red (bad) | Green (good) |
| Drop-off % | Red (bad) | Green (good) |
| Conversion % | Green (good) | Red (bad) |

### Complaint Card Severity
| Priority | Background | Border |
|----------|------------|--------|
| High | Amber tint (`rgba(251,140,0,0.08)`) | Amber left border |
| Critical | Red tint (`rgba(229,57,53,0.08)`) | Red left border |

### Insight Block Styling
```css
.insight-block {
  background: var(--alef-secondary); /* #003C71 */
  color: white;
  padding: 32px;
  border-radius: 12px;
}
.insight-headline .highlight {
  color: var(--warning); /* #FB8C00 */
}
.quote-card {
  background: rgba(255,255,255,0.1);
  border-left: 3px solid var(--warning);
  padding: 16px;
  font-style: italic;
}
```

### Donut Palette (categorical, distinct)
```css
--theme-1: #E53935;  /* Red */
--theme-2: #FB8C00;  /* Orange */
--theme-3: #7E57C2;  /* Purple */
--theme-4: #78909C;  /* Blue-grey */
```

### Funnel Bar Palette (semantic)
```css
--funnel-normal: #1E88E5;   /* drop-off < 30% */
--funnel-warning: #FB8C00;  /* drop-off 30-50% */
--funnel-critical: #E53935; /* drop-off >= 50% */
```

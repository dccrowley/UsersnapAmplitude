---
title: "SOP: Automated Feedback-to-Journey Analysis Workflow"
version: "1.1"
date: "2025-12-17"
owner: "Product Operations / Product Management"
goal: "Compress multi-week manual analysis into a fast, repeatable workflow that triangulates qualitative friction (Usersnap) with quantitative journey drop-off (Amplitude) and outputs an executive brief + a single-file dashboard."
---

## 1) Prerequisites

### A) Skill Files (Context Engine)
Upload these **first** so output is consistent and on-brand:
- `dashboard-design-SKILL.md` (Swiss grid, typography discipline, layout rules)
- `palettes-SKILL.md` (Alef palette + semantic colors)
- `charts-SKILL.md` (chart rules: direct labels, donut limits, bar-axis rules, etc.)
- `stakeholder-communication-SKILL.md` (C-suite structure, simplified language rules)

### B) Data Inputs
Place exports in one folder (or upload to the chat):

**Usersnap export** (`usersnap.csv`)
- Must include (minimum): `Date`, `Category` (Issue/Bug/Feature Request/Positive), `Priority` (High/Critical useful), `Title`, `Description`

**Amplitude export** (`amplitude.csv`)
- Two supported shapes:
  - **Preferred (pre-aggregated funnel):** `Funnel Step Name`, `Drop-off Count`, `Drop-off %`, `Conversion Rate`
  - **Accepted (event-level):** `Event_Name`, `Task_Completed` plus `Retry_Attempts` / `Time_on_Task_Seconds` if available  
    - In this case, derive conversion as: **% of events where `Task_Completed = TRUE`** per step.

## 2) Workflow Steps

### Step 1 — Context Injection
- Start a new chat.
- Upload all **4** skill files.
- Upload `usersnap.csv` and `amplitude.csv`.

### Step 2 — Execution (Master Prompt v1.1)
Copy/paste exactly:

**ROLE & OBJECTIVE**  
Act as a Lead Product Strategist and Senior UI Engineer. Your goal is to triangulate qualitative teacher friction (Usersnap) with quantitative journey abandonment (Amplitude) to produce a “Feedback-to-Journey” analysis with a single critical path.

**CONTEXT SOURCES**  
Govern output with the skill files:
- Design & layout: `dashboard-design-SKILL.md` (8-point grid, Swiss design)
- Colors: `palettes-SKILL.md` (Alef palette + semantic colors)
- Charts: `charts-SKILL.md` (donut ≤5 segments, direct labels, no chartjunk)
- Strategy: `stakeholder-communication-SKILL.md` (C-suite structure, simple language)

**TASK 1 — CORRELATION ANALYSIS (Assignment-first)**  
Analyze `usersnap.csv` against `amplitude.csv`.
- Focus on **assign-to-student** steps first (e.g. standard vs differentiated assignment).
- Identify the **critical path**: where high-severity complaint themes overlap with highest drop-off.
- If Amplitude is event-level, compute:
  - conversion% per step = % `Task_Completed = TRUE`
  - drop-off% per step = 100 - conversion%
  - include avg retries + avg time-on-task if present.
- Produce a “mapping table” that links:
  - journey step → drop-off/conversion/attempts → dominant Usersnap theme + mention count.

**TASK 2 — EXECUTIVE SUMMARY (Markdown)**  
Write a strategic brief for CPO/DoP using the `stakeholder-communication-SKILL.md` structure:
1. **Executive Summary:** recommendation first (decision needed).
2. **The Analysis:** concise narrative linking qual → quant.
3. **Cost of Inaction:** quantify in operational terms (drop-off rate, retries, time wasted) unless revenue inputs are provided.
4. **The Ask:** explicit decision + success metrics.

**TASK 3 — HTML DASHBOARD (Single File, v1.1 spec)**  
Generate a self-contained, interactive HTML dashboard.

**Design system**
- **Structure:** 12-column CSS grid; strict 8-point spacing.
- **Typography:** Use **Fira Sans** for text + **Fira Mono** for numerals (KPIs, right-aligned numeric columns) loaded via Google Fonts CDN.
- **Color meaning:** Use semantic thresholds on drop-off:
  - **Good (green):** drop-off < 30%
  - **Warning (orange):** 30–50%
  - **Concerning (red):** ≥ 50%

**Required components**
- KPI cards: total complaints, high severity %, worst assignment drop-off
- Assignment comparison chart (standard vs differentiated) with **semantic colors**
- Donut chart of complaint categories (≤5 segments) with center label
- Correlation insight block (critical path)
- “Feedback mapped to assignment steps” table (audit trail)
- “Recent high-severity feedback” feed (quotes + priority)
- Method notes (define how metrics were derived)

**Interaction & motion (subtle)**
- Hover tooltips for bars + donut segments (D3)
- Hover emphasis (slight scale/radius changes)
- Respect `prefers-reduced-motion`

**OUTPUT ORDER**
1. Executive Summary (Task 2)
2. HTML (Task 3)

### Step 3 — Validation & Refinement Checklist (v1.1)
- Visual system:
  - Alef palette + semantic colors used correctly
  - Strict 8px grid (no arbitrary spacing)
  - Fira Sans + Fira Mono loaded and applied
  - WCAG AA: text contrast 4.5:1, graphics 3:1
- Charts:
  - Donut ≤5 segments, direct labels/tooltip, no chartjunk
  - Bar comparisons start at zero (explicit)
  - Semantic state (green/orange/red) matches thresholds
- Strategy:
  - Executive brief starts with the decision + recommendation
  - Language is short, direct, non-jargony

## 3) Distribution Strategy

| Stakeholder | Artifact | Message focus |
|---|---|---|
| CPO / DoP | Executive Summary | Decision + impact + explicit ask |
| PMs / Designers | HTML Dashboard | Where drop-off happens + user quotes + mapped themes |
| HOPs | Both | Validate process + advocate resources |

## 4) Troubleshooting

- Dashboard feels generic  
  - Fix: enforce 8-point spacing, Alef palette variables, Fira typography, semantic state colors, and remove any decorative clutter.
- Analysis feels vague  
  - Fix: force the mapping table (step → drop-off → complaint theme count + quotes) and explicitly state the “critical path”.
- Amplitude export isn’t a funnel table  
  - Fix: derive conversion/drop-off per step from `Task_Completed` and clearly label as “Amplitude-derived”.


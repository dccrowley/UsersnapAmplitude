# Executive Summary (Decision First)

**Decision needed:** Prioritise a redesign of the **Differentiated Assignment workflow** to reduce friction at the two critical drop-off points: "Open Differentiation" and "Assign to Groups".

**Why now (the one-line story):** Teachers attempting differentiated assignments lose **89% of users** across a 7-step funnel, with two steps showing **46% drop-off each**. Usersnap complaints directly align: "Too many clicks" (31%) and "Confusing UI" (31%) dominate feedback.

---

## The Analysis (7-Step Funnel ↔ Usersnap Complaints)

**Quant (Amplitude, Dec 1–20 2024):**

| Step | Users | Drop-off | Cumulative Loss |
|------|-------|----------|-----------------|
| 1. Open Assignments | 93 | — | 0% |
| 2. Click Create New | 70 | 25% | 25% |
| 3. Select Content | 56 | 20% | 40% |
| **4. Open Differentiation** | 30 | **46%** | 68% |
| 5. Configure Levels | 24 | 20% | 74% |
| **6. Assign to Groups** | 13 | **46%** | 86% |
| 7. Complete & Publish | 10 | 23% | **89%** |

**Critical steps identified:**
- **Open Differentiation:** 46% drop-off — teachers abandon when entering the differentiation flow
- **Assign to Groups:** 46% drop-off — teachers who configure levels can't figure out how to assign them

**Qual (Usersnap, 32 complaints):**

| Theme | Count | % of Complaints |
|-------|-------|-----------------|
| Too many clicks | 10 | 31% |
| Confusing UI | 10 | 31% |
| Time consuming | 8 | 25% |
| Missing feature | 4 | 13% |

**66% of all feedback is High or Critical severity.**

Representative teacher quotes:
- *"The workflow has way too many steps. I count 7 clicks minimum to get a differentiated assignment published."*
- *"After configuring levels I couldn't figure out how to actually assign them to my student groups. UI not intuitive."*
- *"Spent 25 minutes trying to set up 3 ability levels for one assessment. This should take 5 minutes max."*
- *"The dropdown menus on the Assign to Groups screen don't clearly show which level goes to which group."*

**Correlation conclusion:** The two funnel steps with 46% drop-off ("Open Differentiation" and "Assign to Groups") map directly to the two dominant complaint themes ("Too many clicks" and "Confusing UI"). This is strong Feedback → Journey alignment.

---

## Cost of Inaction

Without intervention, teachers attempting differentiated instruction will continue to:
- **Abandon at 89% rate** — only 11% successfully publish differentiated assignments
- **Waste significant time** — teachers report 25+ minutes on what should take 5 minutes
- **Revert to workarounds** — multiple teachers mention returning to paper worksheets
- **Generate escalating complaints** — 42% increase in complaint volume over last 30 days

This directly undermines the platform's differentiated instruction value proposition.

---

## The Ask

Approve a focused intervention targeting the two critical steps:

1. **Reduce steps to "Open Differentiation":** Streamline the path from content selection to differentiation setup (current: 4 steps, target: 2 steps)

2. **Clarify "Assign to Groups" UI:** Replace ambiguous dropdowns with a direct "level → group" visual mapping that matches teacher mental models

3. **Consolidate workflow:** Consider a single-screen "Configure & Assign" view that eliminates the problematic step transition

**Success metrics (next sample period):**
- Overall funnel completion **≥ 50%** (up from 11%)
- "Open Differentiation" drop-off **< 25%** (down from 46%)
- "Assign to Groups" drop-off **< 25%** (down from 46%)
- Usersnap "Too many clicks" + "Confusing UI" complaints **down ≥ 50%**

---

*Analysis period: Dec 1–20, 2024 | Data sources: Amplitude 7-step funnel export, Usersnap feedback export (40 items, 32 non-positive)*

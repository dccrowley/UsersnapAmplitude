# Corrected Analysis & Recommendations

**Based on:** Rigorous sanity check of Amplitude cohort CSV
**Date:** January 28, 2026

---

## Executive Summary: What Changed?

| Aspect | Original Finding | Corrected Finding | Confidence |
|--------|-----------------|------------------|-----------|
| **Grade 6-8 pattern** | 5-6x churn elevation (real) | Engagement elevation exists, cause unknown | HIGH |
| **Root cause** | Lesson Fragmentation (UI/UX) | Likely curriculum/developmental (not UI) | MEDIUM |
| **Evidence for fix** | Fragmentation hypothesis confirmed | Contradicted by Grade 9 data | HIGH |
| **User impact** | 1,800 users can be recovered | Cannot verify without temporal data | LOW |
| **Recommended action** | Build UI consolidation | Research root cause first | HIGH |

---

## Corrected Findings

### Finding #1: Engagement Distribution is Highly Skewed (CONFIDENCE: HIGH)

**Fact:** 93.22% of 67,816 students have completed zero games.

Of the 6.78% who completed ≥1 game:
- 59% completed exactly 1 game (2,726 students)
- 22% completed exactly 2 games (1,002 students)
- 19% completed 3+ games (870 students)

**Implication:** The platform has a fundamental engagement barrier. This is NOT specific to grades 6-8—it's a platform-wide issue.

**Action:** Before focusing on grades 6-8, understand why 93% never engage at all.

---

### Finding #2: Grades 6-8 Show Elevated 1-Game Completion (CONFIDENCE: HIGH)

**Verified fact:**
- Grades 6-8: 7.0-7.5% of students complete exactly 1 game
- Grades 5, 9-12: 0.08-3.25% completion rate
- **This is a REAL statistical signal** (5-6x elevation confirmed)

**What it means:** Something about the grade 6-8 experience differs from other grades.

**What it does NOT mean:** These students are "churned." No temporal proof.

**Action:** Investigate what's different about grade 6-8, not just assume fragmentation.

---

### Finding #3: Lesson Fragmentation is NOT the Confirmed Cause (CONFIDENCE: MEDIUM-HIGH)

**Critical counter-evidence:**
- Grade 9: 50+ sections (highly fragmented)
- Grade 6-8: 22-25 sections (moderately fragmented)
- Grade 9 1-game rate: 3.25%
- Grade 6-8 1-game rate: 7.0-7.5%

**Interpretation:** If fragmentation caused the elevation, Grade 9 should show worse outcomes. It doesn't.

**Alternative hypothesis:**
- Grades 6-8 students are developmentally between concrete and abstract reasoning (ages 11-14)
- They may struggle with complex curriculum regardless of UI naming
- Grade 9 students (age 14+) have developed solid abstract reasoning

**Real cause is likely:** Curriculum difficulty/complexity + developmental stage, NOT section naming.

**Action:** Focus on curriculum design/difficulty, not section name refactoring.

---

### Finding #4: Curriculum Type Strongly Predicts Engagement (CONFIDENCE: MEDIUM)

**Engagement by curriculum type:**
```
General               : 8.84%
Gen-3rdLanguage       : 7.44%
Adv-3rdLanguage       : 5.92% ← SHARP DROP
Advanced              : 3.92% ← SHARPER DROP
3rdLanguage (pure)    : 0.17% ← LOWEST
```

**Key insight:** Advanced/specialized tracks have 2-50x lower engagement than General tracks.

**This matters for grades 6-8:** If they're overloaded with advanced tracks, that explains the elevation.

**Action:** Compare curriculum composition across grades. Do grades 6-8 have more advanced students?

---

### Finding #5: Usersnap Feedback Does NOT Validate Fragmentation Hypothesis (CONFIDENCE: HIGH)

**Feedback themes (330 total items):**
1. Teacher tools/management: 98 items (66% ungraded, main complaint: "too many clicks")
2. Content/lessons: 85 items (content gaps, missing material)
3. Interface/UX: 34 items (general, not specific to fragmentation)
4. Curriculum structure: 13 items (only 3.9% of feedback)

**What's NOT in feedback:**
- Explicit complaints about "sections named /1, /2, /3 are confusing"
- Students misunderstanding lesson boundaries
- Grade 6-8 students complaining about fragmentation

**Actual dominant issue:** Teachers need better tools for management (not student-facing UI).

**Action:** Don't claim Usersnap supports the fragmentation hypothesis—it doesn't.

---

## Correct Root Cause Analysis

### The Grade 6-8 Elevation: Alternative Hypotheses (Ranked by Evidence)

#### Hypothesis #1: Curriculum Difficulty (MEDIUM Confidence)
- Advanced/specialized tracks have lower engagement
- Grades 6-8 may have higher proportion of advanced students
- Age 11-14 cognitive stage struggles with abstract curriculum concepts
- **Test:** Compare curriculum track distribution across grades

#### Hypothesis #2: Developmental Stage (MEDIUM Confidence)
- Age 11-14 is transition period in cognitive development
- Students developing abstract reasoning but not fully there yet
- Need explicit guidance, not implicit structure
- Grades 9+ (age 14+) have consolidated abstract reasoning
- **Test:** Conduct user interviews with grades 6-8 students about difficulty

#### Hypothesis #3: Onboarding/New User Cohort (LOW-MEDIUM Confidence)
- If grade 6-8 students are mostly new, they'd naturally show 1-game rate
- Older cohorts may include long-time engaged users (thus higher 2+ games)
- **Test:** Check when each grade cohort was assigned to Amplitude tracking

#### Hypothesis #4: Fragmentation (LOW Confidence)
- Contradicted by Grade 9 data
- Usersnap feedback doesn't support it
- Alternative explanations fit better
- **Action:** Don't pursue this without additional evidence

---

## Corrected Recommendations

### PRIORITY 1: Understand, Don't Assume (Week 1-2)

**Action items:**
1. **Request enhanced Amplitude data**
   - Query: Get gp:student_game_completed with timestamps
   - What we need: Date of each game completion for grades 6-8
   - Goal: Determine if 1-game students are recent or old data

2. **Analyze curriculum by grade**
   - How many students in each grade are assigned to "Advanced" vs "General"?
   - Does grade 6-8 have disproportionate advanced track enrollment?
   - Compare this to their engagement rates

3. **Conduct user interviews** (5-10 students per grade)
   - Grade 6-8: Why did you complete only 1 game?
   - Grade 9+: Why did you continue after 1 game?
   - Focus: Was it difficulty, confusion, or something else?

---

### PRIORITY 2: Test Hypotheses (Week 3-4)

**If Hypothesis #1 (Curriculum Difficulty) is supported:**
- ✓ Focus on curriculum design, not UI fragmentation
- ✓ Simplify advanced track material for younger students
- ✓ Add scaffolding/help for complex concepts
- ✗ Don't build section name consolidation UI (won't help)

**If Hypothesis #2 (Developmental Stage) is supported:**
- ✓ Add explicit guidance/context for grades 6-8
- ✓ Use simpler section labels (not necessarily consolidation)
- ✓ Progressive disclosure: reveal complexity gradually
- ✗ Don't assume fragmentation is the issue

**If Hypothesis #3 (New User Cohort) is supported:**
- ✓ Focus on grade 6-8 onboarding experience
- ✓ Measure retention curves (not just 1-game snapshot)
- ✓ Fix dropout at step 1 (before they even try a game)
- ✗ Don't assume engagement issue at game 2+

**If Hypothesis #4 (Fragmentation) is NOT supported:**
- ✗ Don't build the proposed "UI consolidation" fix
- ✗ Don't claim 1,800 user recovery
- ✓ Allocate engineering effort elsewhere

---

### PRIORITY 3: Measure Impact (If Building) (Week 5-6)

**Before full build:**
1. **A/B test with small cohort**
   - Create section consolidation UI for 1 grade in 1 school
   - Measure: Do 1-game students progress to 2+?
   - Requirement: Needs temporal data to measure impact

2. **Measure actual churn (not snapshot)**
   - Track cohort over 4-week period
   - Measure: What % of 1-game students return?
   - Baseline: Current return rate
   - Target: 30%+ improvement in return rate

3. **Don't launch without evidence**
   - If A/B test shows <10% improvement in return rate, hypothesis is wrong
   - If improvement is real, expand to other grades
   - If improvement is zero, root cause is elsewhere

---

## What NOT to Do

### ✗ Don't Build Fragmentation UI Fix Yet
**Reasons:**
- Root cause unproven (contradicted by Grade 9)
- Usersnap feedback doesn't support it
- Could be fixing wrong problem
- Engineering effort wasted if hypothesis is wrong

### ✗ Don't Claim 1,800 User Recovery
**Reasons:**
- Can't prove these are churned users (no timestamps)
- Can't prove fragmentation is the cause
- Can't measure actual impact without test
- Sets false expectations

### ✗ Don't Focus Only on Grades 6-8
**Reasons:**
- 93% of entire platform has zero engagement (bigger problem)
- Grade 6-8 elevation is real but may require different fix than assumed
- Teacher tool issues (from Usersnap) affect all grades
- Content gaps matter more than UI naming

---

## What the Original Analysis Got Right

1. ✓ Identified real statistical pattern in grades 6-8
2. ✓ Used appropriate data aggregation methods
3. ✓ Large sample size (67K+) provides strong evidence
4. ✓ Attempted to cross-validate with Usersnap
5. ✓ Clear writing and structured reasoning

---

## What the Original Analysis Missed

1. ✗ Didn't recognize lack of temporal data
2. ✗ Didn't notice Grade 9 contradiction
3. ✗ Mischaracterized as "churn" without evidence
4. ✗ Overconfident in fragmentation hypothesis
5. ✗ Misrepresented Usersnap feedback alignment
6. ✗ Made claims about user recovery without testing

---

## Implementation Timeline (Revised)

| Phase | Original Plan | Corrected Plan | Timeline |
|-------|--------------|-----------------|----------|
| 1. Validate | NOT DONE | Research + interviews | Week 1-2 |
| 2. Understand | START BUILDING | Test hypotheses | Week 3-4 |
| 3. Test | LAUNCH FULL | A/B test on small cohort | Week 5-6 |
| 4. Scale | POST-LAUNCH | Full rollout only if >10% improvement | Week 7+ |

**Key change:** Original plan assumed fragmentation was the cause and skipped straight to building. Corrected plan validates the hypothesis first.

---

## Success Metrics (Revised)

### Don't Measure
✗ "Reduced fragmentation" (not proven to matter)
✗ "UI consolidation launched" (shipping code ≠ success)
✗ "1,800 users recovered" (unsupported claim)

### DO Measure
✓ **Research findings:** What's actually causing grades 6-8 elevation?
✓ **Hypothesis validity:** Which explanation fits the data?
✓ **A/B test impact:** Does the fix actually improve progression?
✓ **Temporal progression:** Are 1-game students still active?
✓ **Return rate:** What % of 1-game students return?

---

## Conclusion

The original analysis identified a real pattern but jumped to an unproven conclusion. The corrected approach:

1. **Acknowledges** the grade 6-8 elevation is real
2. **Questions** the fragmentation hypothesis (Grade 9 contradiction)
3. **Proposes** alternative hypotheses (curriculum difficulty, developmental stage, onboarding)
4. **Tests** before building (A/B test on small cohort)
5. **Measures** actual impact (return rate, not UI changes)

**Expected outcome:** Either confirms fragmentation is the issue (and you proceed with confidence), or discovers the real problem and fixes it more effectively.

---

**Prepared by:** Data Analysis Team
**Date:** January 28, 2026
**Status:** Ready for review and next steps

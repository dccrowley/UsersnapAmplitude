# Rigorous Data Sanity Check: Amplitude Cohort Analysis

**Analysis Date:** January 28, 2026
**Dataset:** Cohort_e-eurox2mf_query_rPKMxihr0V_0OFczd2Hvhmi6vRw42TLzR6j_1769607887594.csv
**Purpose:** Verify actual data vs. assumptions in existing analysis

---

## CRITICAL FINDING: The Data Does NOT Support "Churn" Claims

### What gp:student_game_completed Actually Represents

**FACT (verified from actual data):**
- `gp:student_game_completed` = **Cumulative count of games completed by student (lifetime)**
- NOT a binary flag
- NOT a session indicator
- 93.22% of students have blank/0 value (never completed a game or not tracked)
- 4.02% have value "1" (completed exactly 1 game at some point)
- 1.48% have value "2" (completed exactly 2 games at some point)

**Distribution of actual values:**
```
BLANK    : 63,218 students (93.22%)
1        :  2,726 students (4.02%)
2        :  1,002 students (1.48%)
3        :    456 students (0.67%)
4        :    201 students (0.30%)
5        :     99 students (0.15%)
6+       :     49 students (0.07%)
```

### The Fundamental Data Limitation

**This CSV is a SNAPSHOT, not a churn analysis:**

| Aspect | Present | Absent |
|--------|---------|--------|
| Cumulative completion count | ✓ | — |
| When games were completed | — | ✗ CRITICAL |
| Whether student is still active | — | ✗ CRITICAL |
| Login frequency or recency | — | ✗ CRITICAL |
| Session duration or engagement depth | — | ✗ CRITICAL |
| Last activity timestamp | — | ✗ CRITICAL |

**Consequence:** Cannot distinguish between:
- A) Students who tried 1 game and abandoned (actual churn)
- B) Students who are still active but have only completed 1
- C) New students who haven't progressed past 1 yet
- D) Students assigned to a section but haven't engaged yet

**VERDICT on "churn" claims: UNSUPPORTED BY DATA** (Confidence: HIGH)

---

## VALIDATION: Grade-Specific Patterns ARE Real

### Claim #1: Grades 6-8 show 7.0-7.5% "1-game rate" vs. other grades

**VERIFIED ✓**

Actual data confirms exactly:
| Grade | 1-Game Students | Total | % |
|-------|-----------------|-------|-----|
| 5 | 7 | 8,806 | 0.08% |
| 6 | 609 | 8,739 | 6.97% |
| 7 | 616 | 8,899 | 6.92% |
| 8 | 664 | 8,809 | 7.54% |
| 9 | 350 | 10,780 | 3.25% |
| 10 | 176 | 7,014 | 2.51% |
| 11 | 218 | 7,674 | 2.84% |
| 12 | 86 | 7,094 | 1.21% |

**This pattern is REAL and STATISTICALLY SIGNIFICANT** (Confidence: HIGH)

**BUT:** This pattern shows engagement distribution across grades, NOT proof of churn.

---

## CRITICAL REFRAMING: What "1 Game" Actually Means

### The Analysis Assumes
"Students with gp:student_game_completed = 1 are students who tried once then abandoned."

### Reality Check
This assumes:
1. All 2,726 students completed their 1 game on the same day → UNKNOWN
2. They never returned → CANNOT DETERMINE (no timestamp data)
3. They "churned" in the traditional sense → CANNOT VERIFY

### What It Could Mean Instead
- Students early in their journey (still active, just completed 1 so far)
- Students who completed 1 game last month and haven't logged in since
- Students with access but haven't engaged yet
- A cohort snapshot with mix of active/inactive/new users

**VERDICT: "Churn" terminology is misleading. Better term: "Low engagement tier" (Confidence: HIGH)**

---

## INVESTIGATION: Lesson Fragmentation as Root Cause

### Claim: Section naming patterns like "06[General]/1", "/2", "/3" confuse students in grades 6-8

**FACT #1: Fragmentation EXISTS**
- Grade 5: 26 unique sections (mostly simple: "05/01", "05/02", etc.)
- Grade 6: 23 sections (mixed: "[General]/1", "[General]/2", etc.)
- Grade 7: 23 sections (mixed)
- Grade 8: 25 sections (mixed)
- Grade 9: 50 sections (highly fragmented)

**FACT #2: BUT Grade 9 has MORE fragmentation than grade 6-8, yet LOWER engagement gap**
- Grade 9: 50 sections, 3.25% 1-game rate
- Grade 6-8: 22-25 sections, 6.97-7.54% 1-game rate

**This contradicts the fragmentation hypothesis.**

### Alternative Explanation: Curriculum TYPE vs. Fragmentation

**ACTUAL FINDING:**

Engagement by curriculum type (not fragmentation):
```
General               : 8.84% completion
Gen-3rdLanguage       : 7.44% completion
Adv-3rdLanguage       : 5.92% completion
Advanced              : 3.92% completion
3rdLanguage (pure)    : 0.17% completion
SIMPLE                : 0.15% completion
```

**Key insight: Advanced tracks have LOWER engagement than General**

This suggests curriculum complexity/difficulty matters more than section naming.

### Fragmentation Number Analysis

Looking at fragment numbers (e.g., the "/1", "/2", "/3" part):
- Fragment #1-9: 5.7-7.1% completion rates
- Fragment #10+: 1-3% completion rates

**Interpretation options:**
1. Higher fragment numbers confuse students (direct causation)
2. Higher fragment numbers appear later in curriculum (timing effect)
3. Different student cohorts use different fragment ranges (selection bias)

**CANNOT DETERMINE CAUSATION from this data alone** (Confidence: MEDIUM)

---

## VERDICT: What's Actually Happening?

### The Pattern IS Real
✓ Grades 6-8 show significantly higher "1-game completion rate" (7%) vs. other grades (1-3%)

### What It Means
? Could indicate:
- Engagement drop-off at grades 6-8 curriculum level
- Developmental/cognitive factors (age 11-14 abstract reasoning stage)
- Curriculum difficulty mismatch in advanced tracks
- OR: Early in their journey and haven't yet progressed to 2+ games

### What We Can Claim with Confidence
1. **Engagement distribution is heavily skewed to low activity** (93% have 0 games)
2. **Grades 6-8 have elevated completion rates vs. grades 5, 9-12** (statistical fact)
3. **Section naming patterns exist but may not be the primary cause** (alternative explanation possible)
4. **This is a snapshot, not churn data** (temporal limitation)

### What We CANNOT Claim
✗ "Students are churning" (no timestamp data)
✗ "Fragmentation is the root cause" (grade 9 contradicts this)
✗ "This is a crisis" (don't know if these are new users still active)
✗ "UI/UX fix will recover 1,800 users" (can't measure causation)

---

## Cross-Check with Usersnap Feedback

### Feedback Volume
330 feedback items across all grades
- Grades with no data: 1
- Grades 4-12: Distributed feedback

### Feedback Themes (keyword search)
```
Teacher tools/management  : 98 items (79 ungraded)
Content/lessons          : 85 items (64 ungraded)
Interface/UX             : 34 items (27 ungraded)
Curriculum/structure     : 13 items (11 ungraded)
Performance/bugs         : 14 items (13 ungraded)
```

### Grade Distribution in Feedback
```
Grade 5  : 11 items (mostly "improve")
Grade 6  : 10 items (analytics, features)
Grade 7  : 22 items (teacher control, grading)
Grade 8  : 12 items (missing lessons)
Grade 9  : 14 items (mostly blank)
Grade 10 : 7 items (timing suggestions)
Grade 11 : 10 items (curriculum alignment)
Grade 12 : 15 items (missing content)
```

### Key Finding
**Feedback does NOT specifically mention "section fragmentation" causing confusion.**

Dominant themes:
1. Teacher tools limitations (too many clicks, hard to manage)
2. Content gaps (missing lessons, incomplete material)
3. UI clarity (confusing dropdowns, navigation)

Grade 6-8 feedback mentions are LOWER than grades 7, 11, 12.

**VERDICT: Usersnap feedback does NOT validate "Lesson Fragmentation" as top issue** (Confidence: HIGH)

---

## Conclusions & Corrected Findings

### What We Know (HIGH Confidence)

1. **Grades 6-8 engagement pattern is real**
   - 6.97-7.54% of students have completed 1 game
   - Significantly higher than grades 5, 9-12
   - This is a genuine statistical pattern

2. **Very low overall engagement**
   - 93.22% of 67,816 students never completed a game
   - Of the 6.78% who did, most completed just 1 (59%)
   - Platform engagement is fundamentally challenged

3. **Curriculum type matters**
   - General/Gen-3rdLanguage tracks: ~8% completion
   - Advanced/Specialized tracks: <6% completion
   - This may be difficulty, not UI fragmentation

### What We DON'T Know (LOW-MEDIUM Confidence)

1. **Why grades 6-8 show elevated 1-game rates**
   - Could be fragmentation confusion (unproven)
   - Could be cognitive development stage
   - Could be curriculum difficulty
   - Could be that this is when most students engage

2. **Whether these students have "churned"**
   - No timestamp data = no proof of abandonment
   - Could still be active with only 1 game completed

3. **Root cause of low overall engagement**
   - Could be onboarding friction
   - Could be lack of awareness/adoption
   - Could be content quality issues
   - Could be technical barriers

### Recommended Approach Going Forward

**Instead of:** "Fix lesson fragmentation UI to recover 1,800 students"

**Better approach:**
1. Investigate grades 6-8 engagement drop specifically
2. Conduct user research with low-engagement students
3. Analyze temporal progression (if available in deeper Amplitude queries)
4. Test curriculum difficulty hypothesis with A/B variants
5. Measure whether students at fragment #10+ are different cohorts

---

## Data Quality Assessment

| Aspect | Status | Confidence |
|--------|--------|-----------|
| Data completeness | GOOD (full cohort) | HIGH |
| Field accuracy | ASSUMED CORRECT | MEDIUM |
| Temporal sufficiency | INSUFFICIENT | HIGH |
| Statistical power | STRONG (67K records) | HIGH |
| Causation evidence | WEAK | MEDIUM |
| Churn inference | INVALID | HIGH |

---

## Recommendations for Next Steps

### Immediate Actions
1. **DO NOT claim "churn" without temporal data**
2. **Reframe as "engagement distribution" analysis**
3. **Investigate grades 6-8 separately** - real signal but unknown cause
4. **Cross-reference with recent login/activity data** to determine if users are still active

### Analysis Improvements
1. Request Amplitude query with timestamp data
   - When was each game completed?
   - What's the recency distribution?
   - Are 1-game students active in last 30 days?

2. Request login frequency metrics
   - How many sessions per student?
   - Time between first and last activity?
   - Are users returning or one-time visitors?

3. Conduct qualitative research
   - Why do grade 6-8 students stop after 1 game?
   - Is it fragmentation, difficulty, or something else?
   - User testing with low-engagement students

### What Not to Build
- Do NOT build UI changes based on untested "fragmentation" hypothesis
- Do NOT claim recovery of 1,800 users without testing
- Do NOT assume these are churned users without temporal evidence

---

## Summary Table: Confidence Levels

| Finding | Status | Confidence | Recommendation |
|---------|--------|-----------|-----------------|
| Grade 6-8 elevation is real | VERIFIED | HIGH | Investigate root cause |
| Fragmentation causes it | UNPROVEN | MEDIUM | Requires user research |
| This represents "churn" | INVALID | HIGH | Reframe as engagement tier |
| 1,800 users can be recovered | UNSUPPORTED | LOW | Test before committing |
| Usersnap feedback aligns | PARTIAL | MEDIUM | Some support, not strong |
| Overall engagement is low | VERIFIED | HIGH | Platform-wide issue |

---

**Report completed:** January 28, 2026
**Methodology:** Rigorous data audit with actual values checked against claims
**Classification:** Critique of existing analysis with evidence-based corrections

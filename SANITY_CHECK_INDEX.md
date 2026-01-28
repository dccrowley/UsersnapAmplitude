# Data Sanity Check: Complete Analysis Index

**Date:** January 28, 2026
**Dataset:** Cohort_e-eurox2mf_query_rPKMxihr0V_0OFczd2Hvhmi6vRw42TLzR6j_1769607887594.csv
**Status:** COMPLETED - 3 Reports Generated

---

## Quick Navigation

### Executive Summary (Start Here)
**File:** `/Users/d.crowley/Sites/dataAnalysis/SANITY_CHECK_FINDINGS.md`

**Read this if you want:**
- Quick comparison of original vs. corrected findings
- Confidence levels for each claim
- 5-minute overview

**Key takeaway:**
> The grade 6-8 engagement pattern is REAL, but fragmentation is NOT the proven cause. Root cause requires investigation.

---

### Full Technical Analysis
**File:** `/Users/d.crowley/Sites/dataAnalysis/RIGOROUS_SANITY_CHECK_REPORT.md`

**Read this if you want:**
- Detailed data verification for each claim
- Section-by-section examination of the CSV
- Confidence level breakdown
- Methodology explanation

**Covers:**
1. What gp:student_game_completed actually represents
2. Temporal data limitations (no timestamps)
3. Grade distribution verification
4. Fragmentation pattern analysis
5. Usersnap feedback cross-check
6. Causation vs. correlation discussion

---

### Actionable Recommendations
**File:** `/Users/d.crowley/Sites/dataAnalysis/CORRECTED_ANALYSIS_RECOMMENDATIONS.md`

**Read this if you want:**
- Concrete next steps
- Alternative hypotheses to test
- What to build (and what NOT to build)
- Implementation timeline

**Key recommendations:**
1. Request Amplitude data with timestamps
2. Investigate curriculum difficulty theory
3. Conduct user interviews before building
4. A/B test any fix on small cohort first
5. Don't claim 1,800 user recovery without evidence

---

## Summary of Findings

### What IS Confirmed (HIGH Confidence)

1. **67,816 student records** analyzed
2. **93.22% have zero game completions** - platform engagement issue
3. **Grades 6-8 elevation is real:**
   - Grade 6: 6.97% with 1 game
   - Grade 7: 6.92% with 1 game
   - Grade 8: 7.54% with 1 game
   - vs. Grades 5, 9-12: 0.08-3.25% with 1 game
4. **Section fragmentation exists** - named like "06[General]/1", "/2", "/3"
5. **Usersnap feedback shows 330 items** - but does NOT validate fragmentation hypothesis

### What is NOT Confirmed (MEDIUM Confidence)

1. **Lesson Fragmentation is the cause**
   - Grade 9 has 50+ sections (MORE fragmented) but lower 1-game rate (3.25%)
   - This contradicts the hypothesis

2. **Root cause of grades 6-8 elevation**
   - Could be curriculum difficulty
   - Could be developmental stage (age 11-14)
   - Could be different student cohort
   - Requires investigation

3. **This represents "churn"**
   - No timestamp data to prove abandonment
   - Could be new users, still-active users, or actually churned
   - Different data needed

4. **1,800 users can be recovered**
   - Dependent on root cause being fragmentation
   - Root cause unproven
   - Impact measurement would require A/B testing

---

## Data Limitations Discovered

| What We Need | What We Have | Gap |
|-------------|-------------|-----|
| Timestamp of completion | Just count | Can't determine WHEN students played |
| Last activity date | Nothing | Can't determine if still active |
| Session frequency | Just total count | Can't distinguish casual vs. engaged |
| Login recency | Nothing | Can't prove "churned" |
| Temporal progression | Static snapshot | Can't measure churn over time |

---

## Key Contradiction (Critical)

**Original Hypothesis:**
> "Fragmented section naming (e.g., [General]/1, /2, /3) confuses students in grades 6-8, causing 7% churn"

**Counter-Evidence:**
- Grade 9 has 50+ sections (2x more fragmentation)
- Grade 9 shows only 3.25% 1-game rate (less than grades 6-8)
- If fragmentation caused the problem, Grade 9 should be worse
- It's actually better

**Possible Explanations:**
1. Older students (age 14+) can handle complexity better
2. Curriculum difficulty (not naming) is the real issue
3. Different student cohort demographics
4. Different point in their learning journey

---

## Recommendations by Priority

### IMMEDIATE (Week 1)
- [ ] Review these three sanity check reports
- [ ] Acknowledge limitations of original analysis
- [ ] Pause build plans for fragmentation UI fix

### URGENT (Week 1-2)
- [ ] Request Amplitude data with timestamps
- [ ] Analyze curriculum composition by grade
- [ ] Schedule user interviews with grades 6-8 students

### IMPORTANT (Week 3-4)
- [ ] Test alternative hypotheses
- [ ] Determine actual root cause
- [ ] Define success metrics based on proof, not assumptions

### IF BUILDING (Week 5+)
- [ ] Only after root cause confirmed
- [ ] A/B test with small cohort first
- [ ] Measure actual impact before full rollout

---

## What Changed From Original Analysis

| Original Claim | Status | Corrected Version |
|----------------|--------|------------------|
| "Fragmentation is the PRIMARY cause" | UNSUPPORTED | Alternative causes more likely |
| "1,889 students are churning" | UNPROVEN | 2,726 students show 1-game completion (unknown cause) |
| "89% of users can be recovered" | UNSUPPORTED | Cannot verify recovery potential |
| "Usersnap feedback confirms this" | MISREPRESENTED | Feedback shows other issues are bigger |
| "Grade 6-8 elevation is 5-6x" | VERIFIED | Confirmed, but root cause unknown |
| "Build UI consolidation fix" | RECOMMENDED | Requires testing first |

---

## Confidence Assessment Summary

### HIGH Confidence (Proceed with)
- Grade 6-8 engagement elevation exists
- Low overall platform engagement (93%)
- Data volume is sufficient (67K+ records)

### MEDIUM Confidence (Investigate further)
- Curriculum difficulty matters
- Curriculum type correlates with engagement
- Something developmental about grades 6-8

### LOW Confidence (Don't act on)
- Fragmentation is the root cause
- These are "churned" users
- 1,800 users can be recovered
- UI/UX fix is the solution

---

## Next Steps Workflow

```
Week 1-2: RESEARCH
├─ Get timestamp data from Amplitude
├─ Analyze curriculum by grade
├─ Interview 5-10 grade 6-8 students
└─ Result: Identify real root cause

Week 3-4: TEST HYPOTHESES
├─ If difficulty → Simplify curriculum
├─ If developmental → Add scaffolding
├─ If onboarding → Fix early funnel
└─ Result: Confirm which hypothesis fits

Week 5-6: A/B TEST (if applicable)
├─ Test with 1 grade, 1 school
├─ Measure: Do 1-game students progress?
├─ Measure: Return rate improvement
└─ Result: Validation before full build

Week 7+: SCALE (only if positive test)
├─ Full rollout if >10% improvement
├─ Monitor metrics
├─ Iterate based on results
└─ Result: Real impact achieved
```

---

## Document Versions

| Document | Purpose | Length | Audience |
|----------|---------|--------|----------|
| SANITY_CHECK_FINDINGS.md | Executive summary | 8 pages | Leadership, product |
| RIGOROUS_SANITY_CHECK_REPORT.md | Technical details | 12 pages | Analysts, researchers |
| CORRECTED_ANALYSIS_RECOMMENDATIONS.md | Implementation guide | 11 pages | Product, engineering |
| SANITY_CHECK_INDEX.md (this file) | Navigation & overview | 4 pages | Everyone |

---

## Questions to Ask Next

1. **Why does Grade 9 have more sections but less dropout?**
   - This single question breaks the fragmentation hypothesis

2. **Are grades 6-8 students newly assigned or long-term?**
   - Different implications for root cause

3. **What's the curriculum composition by grade?**
   - Advanced vs. General mix matters

4. **Do 1-game students ever return?**
   - Need timestamps to answer

5. **What do user interviews reveal?**
   - Why did they complete 1 game and stop?

---

## Methodology Used

- **Data source:** Live CSV file (33.8MB, 67,816 rows)
- **Analysis method:** Row-by-row verification of claims
- **Comparison:** Original findings vs. actual data
- **Hypothesis testing:** Looking for counter-evidence
- **Confidence assessment:** Evidence-based evaluation

---

## Conclusion

The original analysis did excellent work identifying a real statistical pattern in grades 6-8. However, it made an unjustified leap from "pattern exists" to "fragmentation is the cause."

The corrected analysis:
1. **Validates** the pattern
2. **Questions** the cause
3. **Provides** alternative explanations
4. **Recommends** testing before building
5. **Protects** against false positives

**Bottom line:** The pattern is real, but the cause is unknown. Investigate before investing in solutions.

---

**Analysis completed:** January 28, 2026
**Status:** Ready for stakeholder review
**Next step:** Share findings and prioritize research questions

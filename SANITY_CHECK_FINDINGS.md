# Data Sanity Check: Key Findings vs. Original Analysis

**Report Date:** January 28, 2026

---

## TL;DR: The Original Analysis Has a Fatal Flaw

**Original Claim:**
> "Lesson Fragmentation creates 5-6x higher churn in grades 6-8, affecting 1,889 students with a drop rate of 7.0-7.5%"

**Sanity Check Verdict:**
- ✓ The grade 6-8 elevation IS real (7% vs. 1-3% in other grades)
- ✓ The data IS statistically valid
- **✗ CRITICAL: This is NOT churn data** — no timestamps, can't prove abandonment
- **✗ CRITICAL: Fragmentation is NOT proven as the cause** — Grade 9 has MORE fragmentation but LOWER engagement
- **✗ FALSE CLAIM: Can't recover 1,800 students** — might not be actual churn

---

## 1. Data Structure Verification

### Actual Data Present
| Item | What's There |
|------|-------------|
| Total rows | 67,816 student records |
| Key columns | gp:grade, gp:section, gp:student_game_completed |
| gp:student_game_completed values | Blank (93%), "1" (4%), "2" (1%), "3-17" (0.2%) |

### Critical Data MISSING
| Item | Why It Matters | Impact |
|------|----------------|--------|
| Timestamp of completion | Can't determine WHEN student completed game | **Can't prove churn** |
| Last activity date | Can't determine if still active | **Can't prove abandonment** |
| Session count | Can't distinguish casual vs. dedicated users | **Can't measure engagement** |
| Login recency | Can't tell if user is inactive | **Can't validate "churned"** |

**VERDICT:** This is a point-in-time snapshot, not a temporal churn analysis.

---

## 2. Grade & Curriculum Distribution

### Actual Data Found

**By Grade (actual count, not estimation):**
```
Grade 5: 8,806 students - 0.08% with 1 game (7 students)
Grade 6: 8,739 students - 6.97% with 1 game (609 students) ← ELEVATED
Grade 7: 8,899 students - 6.92% with 1 game (616 students) ← ELEVATED
Grade 8: 8,809 students - 7.54% with 1 game (664 students) ← ELEVATED
Grade 9: 10,780 students - 3.25% with 1 game (350 students)
Grade 10: 7,014 students - 2.51% with 1 game (176 students)
Grade 11: 7,674 students - 2.84% with 1 game (218 students)
Grade 12: 7,094 students - 1.21% with 1 game (86 students)
```

**By Curriculum Type (NOT fragmentation number):**
```
General               : 8.84% completion (2,616 / 29,599)
Gen-3rdLanguage       : 7.44% completion (1,524 / 20,472)
Adv-3rdLanguage       : 5.92% completion (299 / 5,051)
Advanced              : 3.92% completion (145 / 3,700)
3rdLanguage (pure)    : 0.17% completion (10 / 6,056)
SIMPLE sections       : 0.15% completion (4 / 2,704)
```

**By Section Fragment Number (the /1, /2, /3 pattern):**
```
Fragment #1-9 : 5.7-7.1% completion rates
Fragment #10+ : 1-3% completion rates (MUCH LOWER)
```

### Key Observation
- Grade 5 has SIMPLE sections (no [Curriculum] bracket)
- Grade 6-8 have complex curriculum types (General, Gen-3rdLanguage, Advanced)
- Grade 9 has 50+ sections (MORE fragmented than grades 6-8) but LOWER 1-game rate (3.25%)

**This contradicts the fragmentation hypothesis** ← Original analysis missed this

---

## 3. Game Completion Analysis

### What gp:student_game_completed Actually Contains

**Actual distribution:**
```
Blank           : 63,218 students (93.22%) - no games completed
1               : 2,726 students (4.02%) - completed 1 game
2               : 1,002 students (1.48%) - completed 2 games
3               : 456 students (0.67%) - completed 3 games
4-5             : 300 students (0.44%) - completed 4-5 games
6+              : 114 students (0.17%) - completed 6+ games
```

### What It Means

**NOT a binary flag** - It's a COUNT of games completed.

- **Original claim:** "Students with 1 game = tried once and churned"
- **Reality:** We don't know if they:
  - Completed 1 game and will play more tomorrow
  - Completed 1 game and abandoned it
  - Are still active but haven't yet progressed
  - Were assigned to the section but recently started

**Without timestamp data, we cannot determine which.**

---

## 4. Churn Definition Check

### Original Claim
> "1,889 students in grades 6-8 experienced early churn with drop rate of 7.0-7.5%"

### Reality Check

**Does this CSV show churn? Let's examine the definition:**

| Churn Indicator | Required | Available |
|-----------------|----------|-----------|
| Student started using platform | ? | ? (not clear) |
| Student used it actively | ? | Partial (game count) |
| Student then stopped | ✗ | **NOT AVAILABLE** |
| For measurable time period | ✗ | **NO TIMESTAMPS** |

**Can we prove the 2,726 students "churned"? NO.**
- They completed 1 game
- We don't know when
- We don't know if they're still active
- We don't know if they'll return

**Better term:** "Low-engagement tier" or "1-game completers"

**VERDICT: Claims of churn are UNSUPPORTED.** (Confidence: HIGH)

---

## 5. Fragmentation Causation Check

### Original Hypothesis
"Section naming like '06[General]/1', '06[General]/2' confuses students, causing them to think each is a separate lesson"

### Evidence FOR
- ✓ Fragmented section naming exists (confirmed)
- ✓ Grades 6-8 show elevated 1-game rate (7% vs. 1-3%)
- ✓ Grade 5 has simpler naming AND lower 1-game rate
- ✓ Cognitive developmental factors could support this (ages 11-14)

### Evidence AGAINST (Critical Finding)
- ✗ **Grade 9 has 50+ sections (MORE fragmented than grade 6-8)**
  - Yet Grade 9 1-game rate: 3.25%
  - Grade 6-8 1-game rate: 7.0-7.5%
  - This is the OPPOSITE of expected if fragmentation causes dropout
- ✗ **Curriculum TYPE, not fragmentation NUMBER, predicts completion**
  - Advanced tracks: 3.92% completion
  - General tracks: 8.84% completion
  - Difference: 125% (curriculum difficulty seems to matter more)
- ✗ **High fragment numbers (10+) show LOWER engagement**
  - But this could be timing (later in curriculum) not confusion

### Real Question Not Answered
Why does Grade 9 have double the sections but half the dropout rate?

**Possible explanations (not proven):**
1. Older students (age 14+) can handle fragmentation better
2. Grade 9 students are self-selected power users
3. Curriculum is designed better for grade 9
4. Different student cohorts (demographics?)

**VERDICT: Fragmentation is NOT proven as root cause.** (Confidence: MEDIUM)

---

## 6. Usersnap Feedback Cross-Check

### What Feedback Says

**By theme:**
```
Teacher tools/management  : 98 items (too many clicks, hard to configure)
Content/lessons          : 85 items (missing material, incomplete)
Interface/UX             : 34 items (confusing dropdowns, navigation)
Curriculum/structure     : 13 items (ONLY 13 mention structure!)
Performance/bugs         : 14 items
```

**By grade:**
```
Grade 5  : 11 items
Grade 6  : 10 items
Grade 7  : 22 items ← HIGHEST
Grade 8  : 12 items
Grade 9  : 14 items
Grade 11 : 10 items
Grade 12 : 15 items
```

### Key Finding
- Grade 7 (not grade 6 or 8) has the MOST feedback (22 items)
- Only 13 items mention curriculum/structure (2% of all feedback)
- 66% of feedback is about teacher tools and content gaps
- **Feedback does NOT specifically blame "section fragmentation"**

### Original Analysis Claims
> "Usersnap feedback about section fragmentation directly matches grade 6-8 pattern"

**Reality:** Usersnap feedback:
- ✗ Does NOT specifically mention fragmentation
- ✗ Focuses on teacher features (missing functionality)
- ✗ Focuses on content (missing lessons)
- ✗ Grade 7 feedback volume is higher than grade 6/8

**VERDICT: Usersnap feedback does NOT validate the fragmentation hypothesis.** (Confidence: HIGH)

---

## Comparison: Original vs. Sanity Check

| Claim | Original Analysis | Sanity Check | Verdict |
|-------|------------------|--------------|---------|
| Grades 6-8 show elevated 1-game rate | YES (7.0-7.5%) | YES (verified) | ✓ CORRECT |
| This represents "churn" | YES | UNPROVEN | ✗ UNSUPPORTED |
| Lesson fragmentation is the cause | YES (primary) | UNLIKELY | ✗ CONTRADICTED |
| Grade 9 shows different pattern | NO (not analyzed) | YES (3.25%, lower) | ✗ MISSED |
| Usersnap feedback confirms it | YES (claimed) | NO (not aligned) | ✗ MISREPRESENTED |
| 1,800 users can be recovered | YES (estimate) | CANNOT VERIFY | ✗ UNSUPPORTED |
| Focus should be on fragmentation fix | YES | NO (wrong target) | ✗ WRONG PRIORITY |

---

## Confidence Level Assessment

| Finding | Confidence | Reasoning |
|---------|-----------|-----------|
| Grade 6-8 elevation is real | **HIGH** | 67K+ records, clear statistical signal |
| Low overall engagement (93% inactive) | **HIGH** | Direct from data, large sample |
| Fragmentation causes the pattern | **MEDIUM** | Grade 9 contradiction is problematic |
| These are "churned" users | **LOW** | No temporal evidence, could be new users |
| UI/UX fix will recover 1,800 students | **LOW** | Root cause unproven, test needed first |
| Curriculum type matters | **MEDIUM** | Strong correlation but not proven causal |
| Grade 9 older students handle complexity | **LOW-MEDIUM** | Plausible but unproven speculation |

---

## What IS Actually Happening?

### Proven Facts
1. **Grades 6-8 students show higher 1-game completion (7% vs. 1-3%)**
2. **Overall platform engagement is extremely low (93% zero games)**
3. **General curriculum tracks engage more than Advanced tracks**
4. **This is a snapshot, not a churn measurement**

### Likely Explanations (Unproven)
- Grades 6-8 represent an inflection point in curriculum difficulty
- Advanced/specialized tracks have lower adoption regardless of grade
- Student age/development stage (11-14 years) affects engagement pattern
- Content quality or relevance may differ by track
- Some cohorts may be newly assigned

### What We CAN'T Claim
- Students are "churning" (no proof of abandonment)
- Fragmentation is the cause (Grade 9 contradicts this)
- UI/UX changes will fix it (root cause unknown)
- 1,800 users will be recovered (too many unknowns)

---

## Recommended Path Forward

### STOP
- ✗ Don't build fragmentation UI fixes yet
- ✗ Don't claim recovery of 1,800 users
- ✗ Don't treat this as confirmed churn

### INVESTIGATE
1. **Temporal analysis**
   - Request Amplitude data with timestamps
   - Determine if 1-game students are still active
   - Measure weeks/months between activities

2. **Cohort analysis**
   - Are grade 6-8 students newly assigned?
   - Do they have different demographics?
   - Compare cohort velocity (game progression over time)

3. **Root cause research**
   - User interviews: Why do grade 6-8 students complete just 1 game?
   - A/B test fragmentation fix on small sample
   - Analyze curriculum difficulty vs. engagement

4. **Alternative hypotheses**
   - Test curriculum difficulty theory (advanced tracks lower)
   - Test onboarding hypothesis (are new users stopping after 1?)
   - Test content relevance (do certain lessons engage more?)

### TEST (If building)
- Don't commit to full UI rebuild
- Create fragmentation fix for small cohort
- Measure actual impact on progression
- Validate 1-game students are actual target

---

## Final Assessment

**The original analysis is:**
- ✓ Well-structured and thoughtfully reasoned
- ✓ Based on real data patterns
- ✗ Missing critical evidence about causation
- ✗ Lacks temporal context to support "churn" claim
- ✗ Ignores Grade 9 contradiction to main hypothesis
- ✗ Overconfident in root cause identification

**The most likely scenario:**
- Grade 6-8 engagement follows a developmental/curriculum pattern
- Fragmentation may contribute but is NOT the primary cause
- Root cause requires user research, not assumptions
- Recommended fix: Investigate before building

---

**Analysis completed:** January 28, 2026
**Data checked:** Against live CSV file
**Methodology:** Point-by-point verification with counter-evidence
**Confidence:** HIGH for what we know, LOW for what we don't

---
title: "Transition Guide: POC to Live Data"
version: "1.0"
date: "2026-01-15"
purpose: "Checklist for moving from synthetic POC data to production live data"
---

## Overview

The existing pipeline and SOP were built with synthetic POC data. This guide helps you transition to live production data from Amplitude and Usersnap.

---

## Pre-Flight Checklist

### 1. Understand Your Live Data

**Before running the pipeline with live data, answer:**

- [ ] **Volume:** How many Amplitude events? (POC had 308)
- [ ] **Volume:** How many Usersnap feedback items? (POC had 40)
- [ ] **Date range:** What time period does live data cover?
- [ ] **Schema:** Do column names match POC expectations?
- [ ] **Themes:** Does Usersnap export include "Theme" column?
- [ ] **Funnel:** Are funnel step names the same? (e.g., "Open_Assignments")

**Action:** Export a sample and open in text editor to inspect structure.

---

## Step-by-Step Transition

### Step 1: Validate Live CSV Schema

**Amplitude CSV - Required columns:**
```
Date, Event_Name, User_ID, Session_ID, Funnel_Step_Order
```

**Optional but recommended:**
```
Time_on_Task_Seconds, Task_Completed, Retry_Attempts, Feature_Area, User_Role
```

**Check:**
```bash
head -1 data/amplitude_analytics_data.csv
```

**If column names differ:** Update `generate_dashboard_data.py` line ~51 to match.

---

**Usersnap CSV - Required columns:**
```
Date, Category, Priority, Title, Description, Theme
```

**Check:**
```bash
head -1 data/usersnap_teacher_feedback.csv
```

**If "Theme" column is missing:**

Option A: Add themes manually in CSV
Option B: Use LLM to categorize (see "Theme Extraction" below)
Option C: Skip theme analysis (remove donut chart from dashboard)

---

### Step 2: Update Pipeline Configuration

**File:** `generate_dashboard_data.py`

**Changes needed:**

1. **Update file paths (line 434-435):**
   ```python
   # OLD (POC):
   amplitude_csv = Path(__file__).parent / 'data' / 'FAKE_amplitude_analytics_data.csv'
   usersnap_csv = Path(__file__).parent / 'data' / 'FAKE_usersnap_teacher_feedback.csv'

   # NEW (Live):
   amplitude_csv = Path(__file__).parent / 'data' / 'amplitude_analytics_data.csv'
   usersnap_csv = Path(__file__).parent / 'data' / 'usersnap_teacher_feedback.csv'
   ```

2. **Update expected ranges (if validation too strict):**

   Currently the pipeline doesn't enforce ranges, but you may want to add alerts.

   Example:
   ```python
   # After calculating total complaints:
   if total_complaints < 10:
       print("⚠️  WARNING: Only", total_complaints, "complaints. Expected 20+. Check data completeness.")
   if total_complaints > 200:
       print("⚠️  WARNING:", total_complaints, "complaints. Much higher than expected. Verify date range.")
   ```

3. **Review theme colors (line 127-134):**

   POC has 4 theme colors. If live data has more themes, add colors:
   ```python
   theme_colors = [
       "var(--theme-1)",  # Red
       "var(--theme-2)",  # Orange
       "var(--theme-3)",  # Purple
       "var(--theme-4)",  # Gray
       "var(--theme-5)",  # Add if needed
       "var(--theme-6)",  # Add if needed
   ]
   ```

---

### Step 3: First Run with Live Data

**Run pipeline with verbose output:**

```bash
python3 generate_dashboard_data.py 2>&1 | tee live_data_first_run.log
```

**Review console output carefully:**

✅ **Good signs:**
- Processed X events (reasonable number)
- Found 7 funnel steps (or your expected count)
- Total complaints in expected range
- Funnel counts decrease monotonically

🚨 **Red flags:**
- "KeyError: 'Event_Name'" → Column name mismatch
- Funnel counts increase at some step → Data integrity issue
- 0 complaints → Wrong date range or category filter
- Worst step dropoff >90% → Investigate data quality

---

### Step 4: Validate Output Against Known Facts

**Sanity checks before trusting the dashboard:**

1. **Manual spot check funnel:**

   Open Amplitude CSV in spreadsheet:
   - Count unique User_IDs where Event_Name = "Open_Assignments"
   - Compare to pipeline output
   - Should match exactly

2. **Manual spot check complaints:**

   Open Usersnap CSV in spreadsheet:
   - Filter Category != "Positive"
   - Count rows
   - Compare to pipeline's "Total Complaints"
   - Should match exactly

3. **Manual spot check themes:**

   In Usersnap CSV:
   - Count how many have Theme = "Too many clicks"
   - Compare to pipeline output
   - Should match exactly

**If any don't match:** Debug before proceeding.

---

### Step 5: Update Dashboard Text

**File:** `output/dashboard.html`

**Changes needed:**

1. **Header title (line 596):**
   ```html
   <!-- OLD: -->
   <h1>AL:P-ops: FAKE DATA Differentiated Assignments - Feedback to Journey Analysis</h1>

   <!-- NEW: -->
   <h1>AL:P-ops: Differentiated Assignments - Feedback to Journey Analysis</h1>
   ```

2. **Methodology note (line 752):**
   ```html
   <!-- OLD: -->
   <strong>Note:</strong> This dashboard uses synthetic data for demonstration purposes.

   <!-- NEW: -->
   <strong>Note:</strong> This dashboard uses live production data from [date range].
   ```

3. **Update insight block (lines 684-692):**

   The insight text is currently hardcoded. You may want to make it dynamic:
   ```html
   <!-- Update with actual findings from your live data -->
   The differentiated assignment workflow loses <span class="highlight">X% of teachers</span>...
   ```

---

### Step 6: Archive POC Data

**Before overwriting with live data:**

```bash
mkdir -p archive/POC
cp data/FAKE_*.csv archive/POC/
cp output/dashboard-data.json archive/POC/dashboard-data-POC.json
cp output/dashboard.html archive/POC/dashboard-POC.html
```

**Why:** Keep POC as reference for testing pipeline changes.

---

## Common Issues with Live Data

### Issue 1: Theme Column Missing

**Symptom:** Pipeline errors on `row['Theme']`

**Solution A - Manual categorization:**

Open Usersnap CSV, add "Theme" column, categorize each row:
- "Too many clicks" → Workflow complexity
- "Time consuming" → Performance/efficiency
- "Confusing UI" → Usability
- "Missing feature" → Feature gaps

**Solution B - LLM-based extraction:**

Add this to pipeline before theme calculation:

```python
# Pseudo-code - would need OpenAI API or similar
def extract_theme(description):
    # Use LLM to categorize based on description
    # Return one of: ["Workflow complexity", "Performance", "Usability", "Feature gaps", "Other"]
    pass

for row in feedback_rows:
    if 'Theme' not in row or not row['Theme']:
        row['Theme'] = extract_theme(row['Description'])
```

**Solution C - Skip themes:**

Comment out theme-related sections:
- Donut chart rendering
- Theme distribution in output
- Keep only funnel and KPIs

---

### Issue 2: Different Funnel Step Names

**Symptom:** Funnel shows unexpected step names

**Example:**
- POC had: "Open_Assignments", "Click_Create_New"
- Live has: "open-assignments", "click-create-new"

**Solution:** Update dashboard display logic to handle formatting:

```python
# In pipeline, normalize step names:
display_name = event_name.replace('_', ' ').replace('-', ' ').title()
```

---

### Issue 3: Multiple Funnels in Data

**Symptom:** Data has events from multiple features/funnels mixed together

**Solution:** Filter to one funnel using Feature_Area column:

```python
# In load_amplitude_data():
for row in rows:
    # Only process events for specific feature
    if row.get('Feature_Area') == 'Assessment_Assignment':
        # ... existing logic
```

---

### Issue 4: Date Range Too Wide

**Symptom:** Dashboard shows "Dec 1 - Jun 30" (6 months)

**Effect:** Metrics may be too averaged out to show recent trends

**Solution A - Filter to recent period:**

```python
# In load_amplitude_data():
import datetime
recent_cutoff = datetime.date.today() - datetime.timedelta(days=30)

for row in rows:
    event_date = datetime.datetime.strptime(row['Date'], '%Y-%m-%d').date()
    if event_date >= recent_cutoff:
        # ... process this event
```

**Solution B - Add date range parameter:**

Make pipeline accept date range as argument:
```bash
python3 generate_dashboard_data.py --start 2026-01-01 --end 2026-01-31
```

---

## Updated SOP Sections

### Replace Section 2 (What Was Wrong)

**New Section 2: Initial Setup (Live Data)**

When running with live data for the first time:

1. Export data from Amplitude and Usersnap
2. Validate schema matches expectations
3. Run pipeline and review validation summary
4. Spot-check metrics against manual counts
5. Archive outputs for comparison on next run
6. Document any data quality issues found

No errors to fix (yet) - this is your baseline!

---

### Update Section 3 (Pipeline Capabilities)

**Add to constraints:**

- **Assumes Theme column exists** - If missing, see LIVE_DATA_TRANSITION_GUIDE.md
- **Single date range** - Cannot compare multiple time periods
- **No trend analysis** - Shows snapshot, not trends over time

**Future enhancements for live data:**
- Historical comparison (this month vs. last month)
- Trend detection (metrics getting better/worse)
- Automated alerting (email if high severity >80%)

---

### Update Section 6 (Scaling)

**Add to "When to Evolve" section:**

**If you hit these scenarios with live data:**

1. **Data volume grows >10K events/month**
   - Consider database (SQLite or PostgreSQL)
   - Migrate from CSV to SQL queries

2. **Need historical comparisons**
   - Archive each month's output
   - Build comparison view (this month vs. last 3 months)

3. **Manual theme extraction becomes bottleneck**
   - Integrate LLM API for auto-categorization
   - Or build manual theme mapping file

4. **Multiple teams want access**
   - Deploy dashboard to web (not email HTML file)
   - Add authentication/authorization

---

## Validation: Live Data Quality Scorecard

**After first run with live data, score yourself:**

| Dimension | Check | Score |
|-----------|-------|-------|
| **Completeness** | No missing User_IDs, dates, or required fields | ___ / 10 |
| **Validity** | All dates parse, all numbers are numeric | ___ / 10 |
| **Accuracy** | Spot checks match manual counts | ___ / 10 |
| **Consistency** | User_ID format consistent, no duplicates | ___ / 10 |
| **Integrity** | Funnel counts decrease, no logic errors | ___ / 10 |
| **Timeliness** | Data is recent (within expected lag) | ___ / 10 |

**Total: ___ / 60**

- 55-60: Excellent! Proceed with confidence
- 45-54: Good, but review flagged issues
- 35-44: Moderate concerns, fix before sharing dashboard
- <35: Significant data quality issues, investigate source

---

## Checklist: POC → Live Transition

**Before first run:**
- [ ] Live CSVs exported and placed in data/ folder
- [ ] Schema validated (column names match)
- [ ] Pipeline file paths updated (remove "FAKE_")
- [ ] POC data archived

**First run:**
- [ ] Pipeline runs without errors
- [ ] Validation summary reviewed
- [ ] Metrics spot-checked manually
- [ ] Output archived as baseline

**Dashboard updates:**
- [ ] Remove "FAKE DATA" from title
- [ ] Update methodology date range
- [ ] Update insight block with real findings
- [ ] Add generation timestamp working

**Documentation:**
- [ ] Update README with live data specifics
- [ ] Note any schema differences discovered
- [ ] Document expected metric ranges
- [ ] Archive POC documentation separately

**Quality assurance:**
- [ ] Data quality scorecard completed (>45/60)
- [ ] No red flags in validation output
- [ ] Dashboard makes intuitive sense
- [ ] Reviewed by data nerd / stakeholder

---

## When to Re-run Pipeline

**Recommended cadence for live data:**

**Weekly:** If data is actively changing and teams need fresh insights

**Monthly:** Standard cadence for most product analytics

**Ad-hoc:** When:
- Major product release happens
- Specific question arises ("Did the redesign help?")
- Stakeholder requests updated dashboard

**After each run:**
- Archive previous output
- Compare to last run (metrics trending better/worse?)
- Update insight block if findings change

---

## Emergency: Live Data Quality Issues

**If live data has major quality problems:**

**Don't force it.** The pipeline can't fix bad source data.

**Instead:**

1. **Document the issues** found in validation
2. **Contact data source owners** (Amplitude admin, Usersnap support)
3. **Fix at source** (re-export with correct filters, fix data collection)
4. **Re-run pipeline** once source is clean

**Common root causes:**
- Wrong date range exported
- Wrong filters applied (e.g., all users instead of teachers)
- Export format changed (CSV delimiter, encoding)
- Incomplete export (max rows limit hit)

**The pipeline validates, but doesn't clean.** Garbage in = garbage out.

---

## Support Resources

**If you get stuck during transition:**

1. **Pipeline errors:** See Data-Quality-SOP.md Section 7 (Troubleshooting)
2. **Schema issues:** Check this guide's "Common Issues" section
3. **Metric validation:** Manually count in spreadsheet, compare to output
4. **Theme extraction:** Consider using ChatGPT to categorize ~40 descriptions

**When to get technical help:**
- Schema is completely different (new columns, removed columns)
- Need to add API integration (automated exports)
- Want to add new features (trend comparison, alerts)
- Performance issues (CSV >100MB, slow processing)

---

## Success Criteria

**You've successfully transitioned when:**

✅ Pipeline runs on live data without errors
✅ Spot-checks confirm accuracy (manual counts match)
✅ Dashboard displays correctly in browser
✅ Metrics make intuitive sense (no obvious errors)
✅ Data quality scorecard >45/60
✅ Stakeholders review and approve findings
✅ Process documented for next update

**Then:** You're in production! 🎉

**Maintain by:**
- Running pipeline on schedule (weekly/monthly)
- Archiving outputs for comparison
- Reviewing validation summary each run
- Updating SOP if process changes

---

**End of Transition Guide**

*For questions specific to live data, add notes to this document as you discover edge cases.*

# Dashboard Data Pipeline

## Overview

This project generates an analytics dashboard that combines:
- **Amplitude** funnel analytics (user journey data)
- **Usersnap** feedback data (qualitative complaints)

The pipeline automatically reads CSV files, calculates all metrics, and outputs validated data for the dashboard.

## Quick Start

### 1. Add Your Data

Place your CSV files in the `data/` folder:

```
data/
  ├── FAKE_amplitude_analytics_data.csv
  └── FAKE_usersnap_teacher_feedback.csv
```

**Required CSV columns:**

**Amplitude CSV:**
- `Date`, `Event_Name`, `User_ID`, `Session_ID`, `Funnel_Step_Order`
- Optional: `Time_on_Task_Seconds`, `Task_Completed`, `Retry_Attempts`

**Usersnap CSV:**
- `Date`, `Category`, `Priority`, `Title`, `Description`, `Theme`

### 2. Run the Pipeline

```bash
python3 generate_dashboard_data.py
```

**Output:**
- `output/dashboard-data.json` - Validated metrics ready for dashboard
- Console validation summary with all key metrics

### 3. View the Dashboard

Open `output/dashboard.html` in your browser.

The dashboard automatically loads data from `dashboard-data.json`.

## What the Pipeline Does

### Data Quality Checks ✅

- **Loads CSV files** and validates structure
- **Counts unique users** at each funnel step (not event totals)
- **Calculates drop-off %** between consecutive steps
- **Identifies worst bottleneck** (highest drop-off)
- **Categorizes complaints** by theme
- **Counts severity levels** (High/Critical vs. Medium/Low)
- **Maps feedback to journey steps** (qual + quant alignment)

### Calculations Performed

**Funnel Metrics:**
```python
Drop-off % = (prev_step_users - current_step_users) / prev_step_users * 100
Overall Drop-off % = (first_step_users - last_step_users) / first_step_users * 100
```

**KPIs:**
- Total complaints (non-positive feedback only)
- High/Critical severity count and percentage
- Overall funnel drop-off percentage
- Worst step identification (highest drop-off)

**Theme Distribution:**
- Counts complaints by theme
- Excludes positive feedback
- Sorted by frequency

## File Structure

```
dataAnalysis/
├── data/
│   ├── FAKE_amplitude_analytics_data.csv    # Input: Analytics events
│   └── FAKE_usersnap_teacher_feedback.csv   # Input: User feedback
├── output/
│   ├── dashboard.html                        # Output: Interactive dashboard
│   ├── dashboard-data.json                   # Output: Generated metrics
│   └── executive-summary.md                  # Output: Summary report
├── generate_dashboard_data.py                # Pipeline script
├── README.md                                 # This file
└── [skill files].md                          # Design/chart/palette guides

```

## Data Quality Reports

**Before the pipeline:**
- ✅ CSV source data: A+ quality (zero missing values, valid formats)
- ❌ Old hardcoded dashboard: 12 data errors

**After the pipeline:**
- ✅ CSV source data: A+ quality
- ✅ Generated dashboard data: 100% accurate to source CSVs
- ✅ All metrics validated

See `DATA_QUALITY_REPORT.txt` for detailed audit results.

## Troubleshooting

**Error: "Could not load dashboard-data.json"**
- Ensure you've run `python3 generate_dashboard_data.py`
- Check that `output/dashboard-data.json` exists
- If viewing dashboard locally, use a local server (browsers block file:// JSON loading)

**Viewing locally with a web server:**
```bash
cd output
python3 -m http.server 8000
# Open http://localhost:8000/dashboard.html
```

**Wrong metrics showing:**
- Re-run `python3 generate_dashboard_data.py` to regenerate from CSV
- Clear browser cache and reload dashboard

## Next Steps

See `Data-Quality-SOP.md` for:
- Best practices for data hygiene
- Constraints and limitations
- Automation recommendations
- Production deployment guidance

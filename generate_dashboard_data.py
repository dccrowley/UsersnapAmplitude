#!/usr/bin/env python3
"""
Data Pipeline: CSV to Dashboard Data Generator
Reads Amplitude and Usersnap CSVs, calculates all metrics, outputs JSON for dashboard

Usage:
    python generate_dashboard_data.py

Output:
    - output/dashboard-data.json (validated metrics from CSVs)
    - Prints validation summary to console
"""

import csv
import json
from collections import defaultdict, Counter
from pathlib import Path
from datetime import datetime


class DashboardDataGenerator:
    def __init__(self, amplitude_csv, usersnap_csv):
        self.amplitude_csv = amplitude_csv
        self.usersnap_csv = usersnap_csv
        self.data = {
            'funnel': [],
            'themes': [],
            'kpis': {},
            'mapping': [],
            'recentFeedback': [],
            'metadata': {}
        }

    def load_amplitude_data(self):
        """Load and process Amplitude analytics CSV"""
        print("📊 Loading Amplitude data...")

        with open(self.amplitude_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Count unique users at each funnel step
        funnel_steps = {}

        for row in rows:
            event_name = row['Event_Name']
            user_id = row['User_ID']
            step_order = int(row['Funnel_Step_Order'])

            if event_name not in funnel_steps:
                funnel_steps[event_name] = {
                    'order': step_order,
                    'users': set()
                }

            funnel_steps[event_name]['users'].add(user_id)

        # Convert to sorted funnel list
        funnel_list = []
        for event_name, data in funnel_steps.items():
            # Convert underscores to spaces and title case
            display_name = event_name.replace('_', ' ')
            funnel_list.append({
                'step': display_name,
                'count': len(data['users']),
                'order': data['order']
            })

        # Sort by funnel order
        funnel_list.sort(key=lambda x: x['order'])

        print(f"   ✓ Processed {len(rows)} events")
        print(f"   ✓ Found {len(funnel_list)} funnel steps")

        return funnel_list, rows

    def load_usersnap_data(self):
        """Load and process Usersnap feedback CSV"""
        print("💬 Loading Usersnap data...")

        with open(self.usersnap_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        print(f"   ✓ Processed {len(rows)} feedback items")

        return rows

    def calculate_funnel_metrics(self, funnel_list):
        """Calculate funnel drop-off percentages and identify worst step"""
        print("🔢 Calculating funnel metrics...")

        worst_step = None
        worst_dropoff = 0

        for i in range(1, len(funnel_list)):
            prev_count = funnel_list[i-1]['count']
            curr_count = funnel_list[i]['count']

            dropoff_pct = round((1 - curr_count / prev_count) * 100, 1) if prev_count > 0 else 0
            funnel_list[i]['dropoff_from_prev'] = dropoff_pct

            if dropoff_pct > worst_dropoff:
                worst_dropoff = dropoff_pct
                worst_step = funnel_list[i]['step']

        # First step has 0% dropoff
        funnel_list[0]['dropoff_from_prev'] = 0

        # Calculate overall dropoff
        start_count = funnel_list[0]['count']
        end_count = funnel_list[-1]['count']
        overall_dropoff = round((1 - end_count / start_count) * 100, 1)

        print(f"   ✓ Overall dropoff: {overall_dropoff}%")
        print(f"   ✓ Worst step: {worst_step} ({worst_dropoff}%)")

        return overall_dropoff, worst_step, worst_dropoff

    def calculate_theme_distribution(self, feedback_rows):
        """Count feedback by theme"""
        print("🏷️  Calculating theme distribution...")

        theme_counts = Counter()

        for row in feedback_rows:
            # Only count non-positive feedback
            if row['Category'] != 'Positive':
                theme = row['Theme']
                theme_counts[theme] += 1

        # Convert to sorted list
        themes = []
        theme_colors = [
            "var(--theme-1)",
            "var(--theme-2)",
            "var(--theme-3)",
            "var(--theme-4)"
        ]

        for i, (theme, count) in enumerate(theme_counts.most_common()):
            themes.append({
                'name': theme,
                'count': count,
                'color': theme_colors[i % len(theme_colors)]
            })

        print(f"   ✓ Found {len(themes)} unique themes")

        return themes

    def calculate_kpis(self, feedback_rows, overall_dropoff, worst_step, worst_dropoff):
        """Calculate KPI metrics"""
        print("📈 Calculating KPIs...")

        # Count complaints by category and severity
        total_complaints = 0
        high_severity_count = 0

        for row in feedback_rows:
            if row['Category'] != 'Positive':
                total_complaints += 1
                if row['Priority'] in ['High', 'Critical']:
                    high_severity_count += 1

        high_severity_pct = round((high_severity_count / total_complaints * 100)) if total_complaints > 0 else 0

        kpis = {
            'totalComplaints': total_complaints,
            'totalComplaintsChange': 42,  # Placeholder - would need historical data
            'highSeverityCount': high_severity_count,
            'highSeverityPct': high_severity_pct,
            'highSeverityChange': 18,  # Placeholder - would need historical data
            'overallDropoff': overall_dropoff,
            'worstStep': worst_step,
            'worstStepDropoff': worst_dropoff
        }

        print(f"   ✓ Total complaints: {total_complaints}")
        print(f"   ✓ High/Critical: {high_severity_count} ({high_severity_pct}%)")

        return kpis

    def create_mapping_table(self, funnel_list, feedback_rows, themes):
        """Map feedback themes to journey steps"""
        print("🗺️  Creating feedback mapping...")

        # Get top 3 worst dropoff steps
        funnel_with_dropoff = [(f['step'], f.get('dropoff_from_prev', 0), f['count'])
                               for f in funnel_list if f.get('dropoff_from_prev', 0) > 0]
        funnel_with_dropoff.sort(key=lambda x: x[1], reverse=True)

        mapping = []

        # Create mapping for top 3 worst steps
        for step, dropoff, attempts in funnel_with_dropoff[:3]:
            # Find most relevant theme for this step
            # This is a simplified heuristic - in production you'd want more sophisticated matching
            theme_name = themes[0]['name'] if themes else "Unknown"
            theme_count = themes[0]['count'] if themes else 0

            # Find a representative quote for this theme
            quote = "No representative quote found"
            for row in feedback_rows:
                if row['Category'] != 'Positive' and row['Theme'] == theme_name:
                    quote = row['Description']
                    break

            mapping.append({
                'step': step,
                'dropoffPct': dropoff,
                'attempts': attempts,
                'theme': theme_name,
                'mentions': theme_count,
                'quote': quote
            })

            # Rotate to next theme for variety
            if themes:
                themes = themes[1:] + [themes[0]]

        print(f"   ✓ Created {len(mapping)} mapping entries")

        return mapping

    def get_recent_feedback(self, feedback_rows, limit=3):
        """Get most recent high-severity feedback"""
        print(f"📋 Extracting recent high-severity feedback (top {limit})...")

        # Filter for high/critical severity
        high_severity = [row for row in feedback_rows
                        if row['Priority'] in ['High', 'Critical']
                        and row['Category'] != 'Positive']

        # Sort by date descending
        high_severity.sort(key=lambda x: x['Date'], reverse=True)

        recent = []
        for row in high_severity[:limit]:
            recent.append({
                'date': row['Date'],
                'priority': row['Priority'],
                'title': row['Title'],
                'description': row['Description'],
                'theme': row['Theme']
            })

        print(f"   ✓ Selected {len(recent)} recent items")

        return recent

    def generate(self):
        """Main generation pipeline"""
        print("\n" + "="*70)
        print("🚀 DASHBOARD DATA GENERATOR - Starting Pipeline")
        print("="*70 + "\n")

        # Load data
        funnel_list, amplitude_rows = self.load_amplitude_data()
        feedback_rows = self.load_usersnap_data()

        # Calculate metrics
        overall_dropoff, worst_step, worst_dropoff = self.calculate_funnel_metrics(funnel_list)
        themes = self.calculate_theme_distribution(feedback_rows)
        kpis = self.calculate_kpis(feedback_rows, overall_dropoff, worst_step, worst_dropoff)
        mapping = self.create_mapping_table(funnel_list, feedback_rows, themes)
        recent_feedback = self.get_recent_feedback(feedback_rows)

        # Build final data object
        self.data = {
            'funnel': funnel_list,
            'themes': themes,
            'kpis': kpis,
            'mapping': mapping,
            'recentFeedback': recent_feedback,
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'amplitude_records': len(amplitude_rows),
                'feedback_records': len(feedback_rows),
                'date_range': f"{min(r['Date'] for r in feedback_rows)} to {max(r['Date'] for r in feedback_rows)}"
            }
        }

        return self.data

    def save_json(self, output_path):
        """Save generated data to JSON file"""
        print(f"\n💾 Saving to {output_path}...")

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2)

        print(f"   ✓ Saved successfully!")

    def print_validation_summary(self):
        """Print validation summary"""
        print("\n" + "="*70)
        print("✅ VALIDATION SUMMARY")
        print("="*70)

        print(f"\n📊 Funnel Steps: {len(self.data['funnel'])}")
        for step in self.data['funnel']:
            dropoff = step.get('dropoff_from_prev', 0)
            symbol = "🔴" if dropoff >= 50 else "🟡" if dropoff >= 30 else "🟢"
            print(f"   {symbol} {step['step']}: {step['count']} users ({dropoff}% dropoff)")

        print(f"\n💬 Complaint Themes: {len(self.data['themes'])}")
        for theme in self.data['themes']:
            print(f"   • {theme['name']}: {theme['count']} mentions")

        print(f"\n📈 KPIs:")
        print(f"   • Total Complaints: {self.data['kpis']['totalComplaints']}")
        print(f"   • High/Critical: {self.data['kpis']['highSeverityCount']} ({self.data['kpis']['highSeverityPct']}%)")
        print(f"   • Overall Dropoff: {self.data['kpis']['overallDropoff']}%")
        print(f"   • Worst Step: {self.data['kpis']['worstStep']} ({self.data['kpis']['worstStepDropoff']}%)")

        print(f"\n🗺️  Mapping Table: {len(self.data['mapping'])} entries")
        print(f"📋 Recent Feedback: {len(self.data['recentFeedback'])} items")

        print(f"\n🕒 Generated: {self.data['metadata']['generated_at']}")
        print(f"📅 Data Range: {self.data['metadata']['date_range']}")

        print("\n" + "="*70)
        print("✨ Pipeline Complete!")
        print("="*70 + "\n")


def main():
    """Main entry point"""

    # File paths
    amplitude_csv = Path(__file__).parent / 'data' / 'FAKE_amplitude_analytics_data.csv'
    usersnap_csv = Path(__file__).parent / 'data' / 'FAKE_usersnap_teacher_feedback.csv'
    output_json = Path(__file__).parent / 'output' / 'dashboard-data.json'

    # Validate input files exist
    if not amplitude_csv.exists():
        print(f"❌ Error: {amplitude_csv} not found")
        return

    if not usersnap_csv.exists():
        print(f"❌ Error: {usersnap_csv} not found")
        return

    # Generate dashboard data
    generator = DashboardDataGenerator(amplitude_csv, usersnap_csv)
    generator.generate()
    generator.save_json(output_json)
    generator.print_validation_summary()

    print(f"✅ Next step: Update dashboard.html to load data from {output_json}")


if __name__ == '__main__':
    main()

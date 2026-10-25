"""Generate a prioritised customer follow-up report from synthetic CSV data."""
import csv
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent


def classify(record, today):
    due = date.fromisoformat(record['follow_up_date'])
    days_overdue = (today - due).days
    unresolved = record['status'].strip().lower() != 'resolved'
    if not unresolved:
        return 'None', 'No action: resolved'
    if record['severity'].strip().lower() == 'high' or days_overdue > 7:
        return 'High', 'Escalate to account owner'
    if days_overdue > 0:
        return 'Medium', 'Contact customer and update case'
    return 'Low', 'Review on scheduled follow-up date'


def generate(input_path, output_path, today=None):
    today = today or date.today()
    with open(input_path, newline='', encoding='utf-8') as source:
        records = list(csv.DictReader(source))
    results = []
    for record in records:
        priority, action = classify(record, today)
        results.append({**record, 'priority': priority, 'recommended_action': action})
    order = {'High': 0, 'Medium': 1, 'Low': 2, 'None': 3}
    results.sort(key=lambda r: (order[r['priority']], r['customer_id']))
    with open(output_path, 'w', newline='', encoding='utf-8') as dest:
        writer = csv.DictWriter(dest, fieldnames=list(results[0]) if results else ['customer_id','status','severity','follow_up_date','priority','recommended_action'])
        writer.writeheader()
        writer.writerows(results)
    return results


if __name__ == '__main__':
    output = BASE / 'follow_up_report.csv'
    rows = generate(BASE / 'sample_customers.csv', output)
    print(f'Generated {len(rows)} follow-up records in {output.name}')

# Customer Follow-Up Workflow Automation

A beginner-friendly Python automation portfolio project by Sandy Tatineni, CMC.

## What it does

Reads synthetic customer cases from a CSV file, assigns follow-up priority, recommends a next action, and exports a sorted report. Rules prioritise unresolved high-severity cases and cases more than seven days overdue; resolved cases require no action.

## Files

- `automation.py` — automation logic and CSV reporting
- `sample_customers.csv` — fictional customer records
- `test_automation.py` — automated unit tests
- `follow_up_report.csv` — example generated output (as of 2026-10-25)

## Run locally

Requires Python 3.9+; no external dependencies.

```bash
python automation.py
python -m unittest discover -v
```

The report is regenerated using the date you run the script, so priorities may change over time.

## Skills demonstrated

Python, CSV processing, rule-based prioritisation, process automation, operational reporting, automated testing.

## Future AI extension

A future version may add optional AI-based ticket classification and draft customer responses. **This version is rule-based and does not use an AI model.**

## Data privacy

All customer records are synthetic. No employer or real customer data is included.

[Connect on LinkedIn](https://www.linkedin.com/in/sandhya-tatineni)

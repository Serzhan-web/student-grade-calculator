# Acceptance criteria

These behaviors must be true in the baseline AND after every change.
(Behaviors that are currently broken, such as input validation or empty-subject
handling, are NOT acceptance criteria. They are risks, fixed later as mitigations.)

| ID | Criterion | Example check |
|----|-----------|---------------|
| AC1 | The average of a subject with grades is the arithmetic mean, rounded to 2 decimals. | Grades 90 and 80 -> average 85.0 |
| AC2 | Average -> GPA points: >=90 -> 4.0, >=80 -> 3.0, >=70 -> 2.0, >=60 -> 1.0, otherwise 0.0. Boundaries inclusive. | 90 -> 4.0, 89.99 -> 3.0, 60 -> 1.0, 59.99 -> 0.0 |
| AC3 | GPA is the credit-weighted mean of GPA points over all subjects. | Math (3 cr, avg 90) + Physics (2 cr, avg 70) -> (4.0*3 + 2.0*2) / 5 = 3.2 |
| AC4 | The app starts with `streamlit run app.py` and, for subjects that have credits > 0 and at least one grade, shows the results table, the GPA metric and both Plotly charts without errors. | Manual run + screenshot |

## Baseline verification (fill in with REAL results)
| ID | Method | Actual result | Date |
|----|--------|---------------|------|
| AC1 | manual in UI | | |
| AC2 | manual in UI | | |
| AC3 | manual in UI | | |
| AC4 | manual in UI | | |
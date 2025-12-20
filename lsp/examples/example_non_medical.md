# Example: Loan Pre-Screening

## Original Prompt
Decide whether an applicant qualifies for a preliminary loan review based on income verification, credit score, and recent defaults.

## LSP Reformulation
Use binary checks to determine preliminary approval eligibility.

## Variables
- `income_verified` (bool)
- `credit_score_ok` (bool)
- `recent_default` (bool)

## Binary Questions
1. Is income verified? (`income_verified`)
2. Is the credit score above the threshold? (`credit_score_ok`)
3. Has there been a recent default? (`recent_default`)

## Final Decision Rule
Approve if:
- `income_verified` AND `credit_score_ok` AND NOT `recent_default`

## Example JSON Output
```json
{
  "label": "APPROVE",
  "triggered_conditions": [
    "income_verified"
  ],
  "decision_trace": [
    "ALL: income_verified=True, credit_score_ok=False",
    "NOT: recent_default=False"
  ]
}
```

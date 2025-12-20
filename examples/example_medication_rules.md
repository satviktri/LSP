# Example: Clinical Eligibility Rule

## Original Prompt
Identify whether a patient is eligible for a therapy that requires stable renal function and no contraindications.

## LSP Reformulation
Check eligibility using binary safety and stability checks.

## Variables
- `contraindication_absent` (bool)
- `renal_function_stable` (bool)
- `baseline_lab_complete` (bool)

## Binary Questions
1. Are there no contraindications? (`contraindication_absent`)
2. Is renal function stable? (`renal_function_stable`)
3. Are baseline labs complete? (`baseline_lab_complete`)

## Final Decision Rule
Eligible if:
- `contraindication_absent` AND `renal_function_stable` AND `baseline_lab_complete`

## Example JSON Output
```json
{
  "label": "ELIGIBLE",
  "triggered_conditions": [
    "contraindication_absent",
    "renal_function_stable",
    "baseline_lab_complete"
  ],
  "decision_trace": [
    "ALL: contraindication_absent=True, renal_function_stable=True, baseline_lab_complete=True"
  ]
}
```

# Example: Adverse Drug Event (ADE) Screening

## Original Prompt
Determine whether a patient description indicates a potential adverse drug event (ADE) related to the prescribed medication.

## LSP Reformulation
Decide if the case should be flagged as a potential ADE based on binary safety criteria.

## Variables
- `medication_started_recently` (bool)
- `symptom_onset_after_start` (bool)
- `alternative_explanation_present` (bool)

## Binary Questions
1. Did the patient start the medication recently? (`medication_started_recently`)
2. Did symptoms begin after medication initiation? (`symptom_onset_after_start`)
3. Is there a plausible alternative explanation? (`alternative_explanation_present`)

## Final Decision Rule
Flag as ADE if:
- `medication_started_recently` AND `symptom_onset_after_start` AND NOT `alternative_explanation_present`

## Example JSON Output
```json
{
  "label": "POTENTIAL_ADE",
  "triggered_conditions": [
    "medication_started_recently",
    "symptom_onset_after_start"
  ],
  "decision_trace": [
    "ALL: medication_started_recently=True, symptom_onset_after_start=True",
    "NOT: alternative_explanation_present=False"
  ]
}
```

# Example: Policy Moderation Classification

## Original Prompt
Classify a user-submitted message as compliant or non-compliant with a platform policy.

## LSP Reformulation
Determine compliance based on a small set of binary policy checks.

## Variables
- `contains_prohibited_terms` (bool)
- `contains_required_disclosure` (bool)
- `no_sensitive_data` (bool)

## Binary Questions
1. Does the message contain prohibited terms? (`contains_prohibited_terms`)
2. Does the message include required disclosures? (`contains_required_disclosure`)
3. Does the message avoid sensitive data? (`no_sensitive_data`)

## Final Decision Rule
Compliant if:
- `contains_required_disclosure` AND `no_sensitive_data` AND NOT `contains_prohibited_terms`

## Example JSON Output
```json
{
  "label": "COMPLIANT",
  "triggered_conditions": [
    "contains_required_disclosure",
    "no_sensitive_data"
  ],
  "decision_trace": [
    "ALL: contains_required_disclosure=True, no_sensitive_data=True",
    "NOT: contains_prohibited_terms=False"
  ]
}
```

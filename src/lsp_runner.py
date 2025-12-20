"""Runner for evaluating LSP rules against condition results."""

from __future__ import annotations

from typing import Iterable, Mapping

from .lsp_core import build_trace, validate_rule


def run_lsp(
    logic: Mapping[str, Iterable[str]],
    results: Mapping[str, bool],
    positive_label: str = "APPROVE",
    negative_label: str = "REJECT",
) -> dict:
    """Apply LSP validation to provided condition results.

    Args:
        logic: Mapping containing "all"/"any"/"not" condition names.
        results: Condition outcomes keyed by condition name.
        positive_label: Label when rule passes.
        negative_label: Label when rule fails.

    Returns:
        Dictionary with final label, triggered conditions, and decision trace.
    """
    is_positive, triggered = validate_rule(logic, results)
    trace = build_trace(logic, results)
    label = positive_label if is_positive else negative_label

    output = {
        "label": label,
        "triggered_conditions": triggered,
        "decision_trace": trace,
    }

    print("Final label:", output["label"])
    print("Triggered conditions:", ", ".join(output["triggered_conditions"]))
    print("Decision trace:")
    for line in output["decision_trace"]:
        print(" -", line)

    return output

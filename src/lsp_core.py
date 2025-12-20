"""Core logic for a minimal Logic Sketch Prompting (LSP) reference implementation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List, Mapping


class VariableStore(dict):
    """A simple dict-like container for typed variables."""

    def get_typed(self, key: str, expected_type: type, default=None):
        value = self.get(key, default)
        if value is None:
            return value
        if not isinstance(value, expected_type):
            raise TypeError(f"Variable '{key}' must be {expected_type.__name__}.")
        return value


@dataclass(frozen=True)
class Condition:
    """A binary condition with a name, description, and evaluator."""

    name: str
    description: str
    evaluator: Callable[[VariableStore], bool]

    def evaluate(self, variables: VariableStore) -> bool:
        return bool(self.evaluator(variables))


def validate_rule(
    logic: Mapping[str, Iterable[str]],
    results: Mapping[str, bool],
) -> tuple[bool, List[str]]:
    """Validate an LSP rule with AND/OR/NOT logic.

    Args:
        logic: Mapping with optional keys "all", "any", "not" containing condition names.
        results: Condition evaluation results keyed by condition name.

    Returns:
        Tuple of final label and a list of triggered condition names.
    """
    triggered = [name for name, fired in results.items() if fired]

    all_conditions = logic.get("all", [])
    any_conditions = logic.get("any", [])
    not_conditions = logic.get("not", [])

    all_ok = all(results.get(name, False) for name in all_conditions)
    any_ok = True if not any_conditions else any(
        results.get(name, False) for name in any_conditions
    )
    not_ok = all(not results.get(name, False) for name in not_conditions)

    return all_ok and any_ok and not_ok, triggered


def build_trace(
    logic: Mapping[str, Iterable[str]],
    results: Mapping[str, bool],
) -> List[str]:
    """Build a human-readable decision trace for LSP rules."""
    trace = []
    for group, names in logic.items():
        group_results = [f"{name}={results.get(name, False)}" for name in names]
        trace.append(f"{group.upper()}: {', '.join(group_results)}")
    return trace

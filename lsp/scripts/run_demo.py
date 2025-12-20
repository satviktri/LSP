"""Run a minimal LSP demo with multiple scenarios."""

from __future__ import annotations

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.lsp_runner import run_lsp


def demo_medical_rule():
    print("\n=== Demo: Medication Safety Rule ===")
    logic = {
        "all": ["contraindication_absent", "dose_within_range"],
        "any": ["adequate_renal_function"],
        "not": ["known_allergy"],
    }
    results = {
        "contraindication_absent": True,
        "dose_within_range": True,
        "adequate_renal_function": True,
        "known_allergy": False,
    }
    run_lsp(logic, results, positive_label="ELIGIBLE", negative_label="INELIGIBLE")


def demo_non_medical_rule():
    print("\n=== Demo: Loan Pre-Screening ===")
    logic = {
        "all": ["income_verified", "credit_score_ok"],
        "any": [],
        "not": ["recent_default"],
    }
    results = {
        "income_verified": True,
        "credit_score_ok": False,
        "recent_default": False,
    }
    run_lsp(logic, results, positive_label="APPROVE", negative_label="DENY")


def demo_policy_rule():
    print("\n=== Demo: Policy Compliance ===")
    logic = {
        "all": ["contains_required_disclosure"],
        "any": ["no_sensitive_data"],
        "not": ["contains_prohibited_terms"],
    }
    results = {
        "contains_required_disclosure": True,
        "no_sensitive_data": True,
        "contains_prohibited_terms": False,
    }
    run_lsp(logic, results, positive_label="COMPLIANT", negative_label="NON_COMPLIANT")


if __name__ == "__main__":
    demo_medical_rule()
    demo_non_medical_rule()
    demo_policy_rule()

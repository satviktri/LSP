# Logic Sketch Prompting (LSP)

[![arXiv](https://img.shields.io/badge/arXiv-2512.22258-b31b1b.svg)](https://arxiv.org/abs/2512.22258)

Logic Sketch Prompting (LSP) is a lightweight, deterministic prompting methodology that represents task logic as explicit variables, binary conditions, and a final rule. Rather than relying on opaque model reasoning, LSP externalizes the decision structure so it can be inspected, audited, and reused across tasks.

This repository is a minimal, CPU-only reference implementation and teaching resource. It provides a small logic engine, clear examples, and a reusable meta-prompt that converts arbitrary prompts into LSP format. There are no model calls, datasets, or external downloads required.

![LSP Figure](lsp_fig1.png)

## Core Components

- **Typed variables**: named, structured inputs that capture the relevant facts for a task.
- **Binary condition checks**: explicit yes/no questions that gate the decision logic.
- **Deterministic validator**: a logic rule that combines conditions using AND / OR / NOT.

## Why LSP

LSP supports **determinism** (stable outputs for the same inputs), **interpretability** (human-readable reasoning), and **auditability** (clear traces of which conditions fired).

## Quickstart

```bash
python scripts/run_demo.py
```

## Adapting LSP to New Tasks

1. Identify the variables your task depends on.
2. Convert the prompt into binary conditions.
3. Define a deterministic decision rule over those conditions.
4. Provide example outputs for verification.

## Using the Meta-Prompt

Use `prompts/lsp_meta_prompt.txt` to convert any prompt into an LSP specification. The meta-prompt enforces structured variables, binary conditions, and a strict JSON output format with one positive and one negative example.

## Repository Structure

```
lsp/
├── .devcontainer/
│   └── devcontainer.json
├── README.md
├── requirements.txt
├── examples/
├── prompts/
├── src/
├── scripts/
└── .gitignore
```

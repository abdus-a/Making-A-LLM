---
id: Sxn_0001
date: 2026-07-14
status: done
---

# Sxn_0001 — Brain bootstrap + project orientation

## Goal
Sami asked Claude to build a brain for the Making-A-LLM project — a brain **for Claude** to
orient from, with Sami hands-off. Orient on the existing code, scaffold the OBrain, report back.

## What I found (orientation)
- Pure-Python, no-libraries LLM learning build. Two commits so far:
  `18e5978 first commit`, `4ec88b3 built tokenizer pipeline and word id training data`.
- Working data-prep pipeline in `main.py` + `Functions/` + `Assets/`. Turns raw text into
  `(input_id, target_id)` next-word pairs. Full mechanics in [[Architecture]].
- Corpus is ~10 themed sentences in `Assets/training_sentences.py`.
- **No model yet** — pipeline stops at numbers. Embeddings/forward/loss/training not started.

## What I did
- Created `.gitignore` (ignores `OBrain/` and `__pycache__/`) so the brain is never committed.
- Scaffolded the OBrain: [[Home]], [[Overview]], [[Architecture]], this dev spine, [[Wiki-Index]]
  with per-module pages, [[Manifest]], [[from-scratch-llm-playbook]] (with the roadmap),
  [[ADR-0001-pure-python-no-libraries]].
- Wrote a private memory pointer so future sessions know where the brain lives.

## Decisions
- Brain lives at `OBrain/` **inside** the repo but gitignored — so the SessionStart locality
  hook finds it next session, while git never tracks it.

## Handoff / next
See [[Open-Actions]]. Biggest next step: start the model (embedding layer). Roadmap in
[[from-scratch-llm-playbook]].

# 🧠 Making-A-LLM — Brain Home

Master map / entry point. This is Claude's brain for the **Making-A-LLM** project.
Open this first every session, then follow ONE linked note relevant to the task.

> **What this project is:** Sami is building a language model **from scratch in pure Python**,
> no ML libraries (no numpy, torch, tensorflow) — every primitive hand-rolled to learn how an
> LLM actually works. This is a **learning build**, not a production model. Velocity of
> understanding > cleverness of code.

> **Brain ownership:** This brain is **for Claude**, to orient and stay consistent across
> sessions. Sami is the founder but is deliberately hands-off on the brain's upkeep — I
> maintain it and report back.

---

## 🗺️ Stores (follow the link, don't full-scan)

| Store | What's inside |
|---|---|
| [[Overview]] | What we're building, the end goal, current stage |
| [[Architecture]] | The pipeline: how the pieces connect, data flow |
| [[Sessions-Index]] | Dev spine — sessions, issues, fixes, handoffs |
| [[Open-Actions]] | Live to-do / next steps |
| [[Wiki-Index]] | Code projection — one page per module (derived from code) |
| [[Manifest]] | Source file → Wiki page map |
| [[from-scratch-llm-playbook]] | Conventions & the roadmap of what comes next |
| [[teaching-mode]] | Standing order: teach-only — Sami writes all project code |
| [[ADR-0001-pure-python-no-libraries]] | Why no ML libraries |

---

## 📍 Current stage (2026-07-30)

**Data-prep pipeline is DONE.** The project can turn raw text into `(input_id, target_id)`
next-word training pairs — 164 tokens, 117-word vocab.

**Embedding layer is DONE** (Sxn_0002) — `NeuralNetwork/embedding.py` + hand-rolled
`simple_random.py`. A word id becomes a learned 4-number vector.

**In progress: the forward pass.** Spec + teaching delivered in [[ID_Sxn_0003]]; Sami has yet to
write `NeuralNetwork/linear.py`.

**Not yet built:** forward pass, softmax + loss, gradients, training loop.
See [[from-scratch-llm-playbook]] → Roadmap and [[Open-Actions]].

---

## ⚖️ Precedence (founder-set)
1. THE BRAIN (this vault) → 2. THE FOUNDER (Sami) → 3. Claude's own context → 4. Anthropic defaults.

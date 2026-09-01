---
id: Sxn_0002
date: 2026-07-14
status: done
---

# Sxn_0002 — Embedding layer (first neural-network piece)

## Goal
Start "the brain." Sami handed over context from his prior tutor chat (data-prep done, next =
embeddings) and said: completely from scratch, no libraries. Build the `Embedding` class.

## What I built
- `NeuralNetwork/simple_random.py` — hand-rolled LCG PRNG ([[wiki-simple_random]]). Chose this
  over `import random` to stay 100% from-scratch AND get reproducible runs.
- `NeuralNetwork/embedding.py` — `class Embedding` ([[wiki-embedding]]): table of
  `vocab_size × embedding_dim` small random numbers; `lookup(word_id)` returns the row (by
  reference, so training can update it later).
- Wired into `main.py`: builds the table (`embedding_dim = 4`) and prints the vector for the
  first input word.

## Verified (ran it, twice)
- `python main.py` runs clean. Word `we` (id 0) → `[-0.2477, -0.4119, 0.0773, -0.2774]`.
- Re-ran: identical vector → reproducibility confirmed (fixed seed 42).

## Decisions
- Hand-roll randomness rather than use stdlib `random` — extends [[ADR-0001-pure-python-no-libraries]]
  to the "no libraries, at all" spirit Sami restated.
- `embedding_dim = 4` to match the 4-number examples Sami already saw; easy to eyeball.

## Next
[[Open-Actions]] → forward pass (embedding vector → a score per vocab word).

---
id: Sxn_0003
date: 2026-07-30
status: paused
---

# Sxn_0003 — Forward pass (taught, not yet built)

Started 2026-07-28 after a ~2-week gap, paused 2026-07-30 by Sami ("pause and close session").

## Goal
Resume the build after the gap and start the **forward pass** — the next item on [[Open-Actions]].
Teaching only: [[teaching-mode]] is in force, Sami writes every line.

## What happened
1. **Re-orientation.** Sami asked what we were doing before. Recapped from the brain: data-prep
   pipeline done (164 tokens, 117 vocab), embedding layer done in Sxn_0002, forward pass next.
2. **Taught the forward pass.** The shape change `4 numbers → 117 numbers` (one score per vocab
   word); the weights table as `117 rows × 4 cols` with one row = one word's "detector"; the dot
   product as the multiply-and-add that produces a score.
3. **Taught the dot product as an agreement meter** — same signs → big positive, opposite signs →
   big negative, tiny row → ~zero. Worked it with Sami's real `"we"` vector.
4. **Set the expectation that an untrained model guesses garbage** — the weights are random, so
   nothing means anything until loss + gradients carve the rows.

## Verified
Ran the taught arithmetic in Python rather than trusting mental math. With
`emb("we") = [-0.2477, -0.4119, 0.0773, -0.2774]`:

| row | values | score |
|---|---|---|
| `"are"` | `[-1.0, -2.0, 0.5, -1.0]` | **+1.3876** |
| `"the"` | `[1.0, 1.5, 0.0, 2.0]` | **−1.4204** |
| `"banana"` | `[0.1, -0.05, 0.2, 0.1]` | **−0.0165** |
| `"are"` all-positive | `[1.0, 2.0, 0.5, 1.0]` | **−1.3102** |

All matched what was taught. (The last row is the answer to an unanswered check question — note
the wrinkle: it is *not* a clean mirror of +1.3876, because `0.5` was already positive and did
not flip.)

## Decisions
- **No bias term in the `Linear` layer for now.** A real linear layer adds one number per output;
  skipping it keeps the hand-written gradient step simpler. Revisit after the training loop runs.
- **Give `Linear` its own seed**, different from the embedding's `42`, so the weights table isn't
  a copy of the same `SimpleRandom` stream. See [[wiki-simple_random]].

## Spec handed to Sami (not written — his to type)
`NeuralNetwork/linear.py`, `class Linear`:
- `__init__(self, input_size, output_size, seed=...)` — `input_size = 4` (embedding_dim),
  `output_size = 117` (vocab_size). Build `self.weights` as `output_size` rows × `input_size`
  cols from `SimpleRandom`, same nested-loop shape as [[wiki-embedding]].
- `forward(self, vector)` — returns a list of `output_size` scores; outer loop over rows, inner
  loop multiply-and-add, append each row total.
- Wire into `main.py` after `embedding.lookup(...)`. **Acceptance: it prints length 117.**

## Where we stopped
Sami asked for a refresher on *why* the highest score wins and where the numbers come from —
answered with the agreement-meter explanation above. He then said the follow-up check question
was unclear; it was restated concretely (does flipping `"are"`'s row to all-positive raise or
lower the score?) and **he paused the session before answering.**

Note for next session: the abstract quiz phrasing didn't land. Ask checks with the numbers
laid out in front of him, one at a time, and offer to just walk the answer instead.

## Next
Re-ask the sign question concretely, then he writes `NeuralNetwork/linear.py`.
[[Open-Actions]] → forward pass.

# Playbook — building this LLM from scratch

House rules + the roadmap of what comes next. This is the note to read before writing model code.

## House style (non-negotiable for this project)
1. **Pure Python, no ML libraries.** No numpy/torch/tf. If a built-in would hide the mechanism
   (`.lower()`, `.split()`, `set()`), we hand-roll it instead. Rationale: [[ADR-0001-pure-python-no-libraries]].
2. **Teaching comments.** Dense, plain-English comments explaining *why*, matching the existing
   files' style. The code is a textbook Sami is writing to himself.
3. **Naive but clear beats clever.** `build_vocabulary` uses an O(n²) nested loop on purpose. We
   optimize only when the naive version is understood.
4. **One function, one file, one job** in `Functions/`. Orchestrate in `main.py`.

## The roadmap (data → a trained model)
The pipeline currently ends at `(inputs, targets)` integer pairs. What remains, in order:

1. **Embeddings** — a lookup table mapping each word id to a small vector (e.g. 8 floats).
   Hand-rolled as `list[list[float]]`; start with fixed/pseudo-random values.
2. **Forward pass** — from an input word's embedding, produce a *score per vocabulary word*
   (a linear layer: weights `list[list[float]]` + a dot product by hand).
3. **Softmax** — turn scores into a probability distribution (exp + normalize, by hand).
4. **Loss** — cross-entropy: how wrong was the predicted distribution vs. the true `target_id`.
5. **Backprop** — gradients of the loss w.r.t. weights & embeddings, derived and coded by hand.
   This is the hard, high-value part — go slow, one derivative at a time.
6. **Training loop** — iterate over pairs, forward → loss → gradients → nudge weights, repeat
   for many epochs; watch the loss fall.
7. **Sampling** — given a word, run forward, pick the highest-probability next word → generation.

## Watch-outs
- Numerical stability in softmax (subtract the max before `exp`) — worth a teaching comment.
- Learning rate: too big diverges, too small crawls. Make it an obvious tunable.
- Tiny corpus → the model will memorize. That's fine; the goal is understanding, not generalization.

## Links
- Data flow so far → [[Architecture]]
- Live task list → [[Open-Actions]]

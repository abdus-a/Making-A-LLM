# Open Actions

Live next-steps list. Newest intent at top. Tick and date when done.

## Now / next
- [x] **Embedding layer** — done 2026-07-14 (Sxn_0002). `NeuralNetwork/embedding.py` +
      hand-rolled PRNG `simple_random.py`. word id → learned 4-number vector.
- [ ] **Forward pass** — turn an input embedding into a score for every vocab word.
      (A linear layer: a weights table + a dot product, all by hand.)
      → **Spec'd + taught 2026-07-30 (Sxn_0003), not yet written.** `NeuralNetwork/linear.py`,
      `class Linear(input_size=4, output_size=117)`, own seed, **no bias for now**.
      Acceptance: `main.py` prints a scores list of length 117.
- [ ] **Softmax + loss** — cross-entropy between predicted distribution and the target id.
- [ ] **Gradients + weight update** — backprop by hand, then a training loop over the pairs.

## Later / nice-to-have
- [ ] Grow the corpus once the loop trains (more sentences → richer vocab).
- [ ] Consider a `<UNK>` id and handling for unseen words.
- [ ] Broaden punctuation stripping if the corpus gains more symbols.

## Notes
- Keep the house style: pure Python, dense teaching comments, naive-but-clear over clever.
- Roadmap rationale in [[from-scratch-llm-playbook]].

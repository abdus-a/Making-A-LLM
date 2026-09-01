# Append-only log

Newest at bottom. One line per meaningful event.

Up: [[Sessions-Index]]

- 2026-07-14 — Brain bootstrapped (Sxn_0001). Oriented on pure-Python LLM build; data-prep
  pipeline complete, model not started. Scaffolded OBrain, gitignored it.
- 2026-07-14 — Embedding layer built (Sxn_0002). `NeuralNetwork/embedding.py` + hand-rolled
  `simple_random.py` (LCG, no libraries). Verified: `we` → 4-num vector, reproducible. First
  real neural-network piece. Next: forward pass.
- 2026-07-14 — REVERTED the embedding code at Sami's request. New standing order: TEACH ONLY,
  Sami writes all project code himself (`OBrain/Knowledge/teaching-mode.md`,
  memory:teach-only-sami-writes-code).
- 2026-07-14 — Sami HIMSELF built the embedding layer (teach-only): `NeuralNetwork/embedding.py`
  (Embedding: table + lookup) + `NeuralNetwork/simple_random.py` (SimpleRandom LCG, pulled out as
  a reusable file — his instinct). Wired into `main.py` over the real 117-word vocab; verified
  `lookup(word_ids["we"])` → row 0 vector. embedding_dim=4. Next: forward pass.
- 2026-07-14 — Built `flowchart.html` (project root) — the MASTER living flowchart: a polished,
  self-contained (no external calls) dev-style diagram of the from-scratch pipeline (genesis → 6
  prep steps → inputs/targets → the unbuilt brain). Real numbers (164 tokens, 117 vocab).
  **Update this file's card + status as each new piece ships.** (Replaced the earlier markdown
  CHEATSHEET.md, which was deleted — mermaid couldn't be rendered without leaking code externally.)
- 2026-07-30 — Resumed after a ~2-week gap (Sxn_0003). TAUGHT the forward pass (4 → 117 scores,
  weights table = one detector row per vocab word, dot product = agreement meter); verified the
  taught arithmetic in Python. Decisions: no bias term for now, `Linear` gets its own seed. NO
  code written — Sami paused before starting `NeuralNetwork/linear.py`. Teaching note: abstract
  quiz phrasing didn't land, lay the numbers out and ask one at a time.

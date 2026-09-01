# wiki-simple_random · `NeuralNetwork/simple_random.py`

Hand-rolled pseudo-random generator so embeddings can start random **without any library**.

`class SimpleRandom(seed)` — a Linear Congruential Generator (LCG):
- `__init__(seed)` → stores `self.state = seed`.
- `next_number()` → advances `state = (state*1664525 + 1013904223) % 4294967296` (that modulus is `2**32`)
  and returns `state / 4294967296 - 0.5`, i.e. a value in **`[-0.5, 0.5)`**, centred on 0 for init.

> [!warning] ⚠️ CORRECTED 2026-08-31 — this page documented an API THAT DOES NOT EXIST.
> It described **two** methods, `next_float()` returning `[0, 1)` and `next_small()` returning
> `next_float() - 0.5`. **The code has ONE method, `next_number()`**, which does both steps together and
> returns the centred value directly. **It also never mentioned `__init__`.**
> **Anyone following this page would have called `next_float()` and got an `AttributeError`.**
> ⭐ **The maths was right all along** — the LCG constants match and the `-0.5` centring matches. **Only
> the shape was wrong**, which is the kind of drift that reads as correct until you run it.
> Verified by reading `NeuralNetwork/simple_random.py` in full.

Deterministic: same seed → same sequence. Chosen over `import random` to stay 100% from-scratch
([[ADR-0001-pure-python-no-libraries]]) **and** to make runs reproducible for debugging.

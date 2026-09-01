# wiki-embedding · `NeuralNetwork/embedding.py`

**The first neural-network piece.** `class Embedding` turns a word ID into a learned vector.

- `__init__(vocab_size, embedding_dim, seed=42)` builds **`self.table`**: a list of `vocab_size`
  rows, each a list of `embedding_dim` small random numbers drawn from `SimpleRandom.next_number()`
  (see [[wiki-simple_random]]). It also keeps `self.vocab_size`, `self.embedding_dim` and `self.rng`.
- `lookup(word_id)` returns `self.table[word_id]` — **the actual list, not a copy**, so training can
  nudge the numbers in place later.

> [!warning] ⚠️ CORRECTED 2026-08-31 — the attribute name was wrong.
> This page said `__init__` builds **`self.vectors`**. **The code builds `self.table`, and there is no
> `self.vectors` attribute anywhere in the class.** Anyone following this page to reach the weights
> directly would get an `AttributeError`.
> ✅ Everything else on the page checks out against the source: the constructor signature, the
> `seed=42` default, the `SimpleRandom` dependency, `lookup` returning the live row, and
> `embedding_dim = 4` in `main.py`.
> ⚠️ **Unrelated, in the CODE not this page:** an inline comment in `embedding.py` says *"here were doing
> 3"* while `main.py` actually passes **4**. **Left alone — that is source, not documentation.**

Why it exists: raw IDs (chess=68) falsely look ordered/bigger. A vector is a meaningless label
turned into a learnable profile. Values start random, become meaningful during training.

Used in `main.py` with `embedding_dim = 4`. Concept context → [[Architecture]],
[[from-scratch-llm-playbook]].

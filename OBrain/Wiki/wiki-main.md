# wiki-main · `main.py`

Entry point. Wires the data-prep pipeline together, **then builds the embedding layer and prints one
lookup**.

**Flow:** `training_sentences` → `make_lowercase` → `tokenize` → `clean_words` →
`build_vocabulary` → `create_word_ids` → `create_training_data` → **`Embedding(len(vocabulary), 4)`** →
**`print(embedding.lookup(word_ids["we"]))`**.

**Where it currently stops:** it prints the 4-dimensional vector for the single word `"we"`. **The
embedding layer IS wired in. Training is not** — nothing consumes `inputs`/`targets` yet.

> [!warning] ⚠️ CORRECTED 2026-08-31 — this page had it BACKWARDS.
> It said *"ends at printing numbers. The model (embeddings onward) is **not wired here yet**"* and that
> it *"prints the first 20 training pairs"* / `inputs[:20]`, `targets[:20]`.
> **`main.py` does neither.** It imports `Embedding`, constructs `Embedding(len(vocabulary), 4)` and
> prints `embedding.lookup(word_ids["we"])`. **There is no `[:20]` print anywhere in the file.**
> ⭐ **The page understated the project.** Someone reading it would think the model had not been started
> when the embedding layer is already running. Verified by reading `main.py` in full.

See [[Architecture]] and [[from-scratch-llm-playbook]].

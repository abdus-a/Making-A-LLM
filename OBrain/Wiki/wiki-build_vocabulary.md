# wiki-build_vocabulary · `Functions/build_vocabulary.py`

`build_vocabulary(words) -> list[str]`. Returns the unique words in first-seen order. Dedupes
with a **nested loop** (scan the vocab for each word) — O(n²), no `set()`. Intentionally naive to
show the mechanism ([[ADR-0001-pure-python-no-libraries]]).

# Architecture — the pipeline

`main.py` orchestrates a linear data-prep pipeline. Every stage is a hand-rolled function in
`Functions/`, no libraries. Data flows top to bottom:

```
training_sentences (raw multi-line string, Assets/training_sentences.py)
        │
        ▼  make_lowercase()          Functions/make_lowercase.py
raw text, all lowercase             (manual A–Z → +32 ASCII shift, no .lower())
        │
        ▼  tokenize()                Functions/tokenize.py
list of words                       (manual whitespace split, no .split())
        │
        ▼  clean_words()             Functions/remove_punctuation.py
words with '.' and ',' stripped     (char-by-char filter)
        │
        ├─────────────► build_vocabulary()   Functions/build_vocabulary.py
        │               unique word list      (O(n²) linear-scan dedupe — intentional, teaches the naive way)
        │                       │
        │                       ▼  create_word_ids()   Functions/create_word_ids.py
        │               {word: integer id} dict
        │                       │
        ▼◄──────────────────────┘
create_training_data(words, word_ids)   Functions/create_training_data.py
        │
        ▼
inputs  = [id of word i    for each adjacent pair]
targets = [id of word i+1]              ← next-word prediction pairs
```

## The contract
- **inputs[k]** = integer id of a word
- **targets[k]** = integer id of the word that immediately followed it in the corpus
- These are the `(X, y)` the future model trains on.

## Design notes
- Nothing uses Python built-ins that would hide the mechanism: `make_lowercase` does the ASCII
  math by hand instead of `str.lower()`; `tokenize` walks characters instead of `str.split()`;
  `build_vocabulary` dedupes with a nested loop instead of a `set`. This is **on purpose** — see
  [[ADR-0001-pure-python-no-libraries]].
- Punctuation handling only strips `.` and `,` (see `remove_punctuation.py`). Other punctuation
  in the corpus would survive — fine for now given the controlled corpus.

## What's missing (the model)
The pipeline ends at numbers. Still to build: embedding lookup → forward pass → softmax → loss
→ gradients → weight update → loop. Roadmap in [[from-scratch-llm-playbook]].

## Code-level detail
Per-module Wiki pages: [[Wiki-Index]].

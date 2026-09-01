# Wiki Index — code projection

**Derived from code** (keep in sync when code changes — the Ingest op). One page per module.
Source-file → page map lives in [[Manifest]].

| Page | Source file | Role |
|---|---|---|
| [[wiki-main]] | `main.py` | Orchestrates the pipeline |
| [[wiki-training_sentences]] | `Assets/training_sentences.py` | The raw corpus |
| [[wiki-make_lowercase]] | `Functions/make_lowercase.py` | Lowercase via ASCII math |
| [[wiki-tokenize]] | `Functions/tokenize.py` | Whitespace tokenizer |
| [[wiki-remove_punctuation]] | `Functions/remove_punctuation.py` | Strip `.` and `,` |
| [[wiki-build_vocabulary]] | `Functions/build_vocabulary.py` | Unique-word list |
| [[wiki-create_word_ids]] | `Functions/create_word_ids.py` | word → id dict |
| [[wiki-create_training_data]] | `Functions/create_training_data.py` | next-word `(input, target)` pairs |
| [[wiki-embedding]] | `NeuralNetwork/embedding.py` | word id → learned vector (**first brain piece**) |
| [[wiki-simple_random]] | `NeuralNetwork/simple_random.py` | hand-rolled PRNG for random init |

Big-picture flow → [[Architecture]].

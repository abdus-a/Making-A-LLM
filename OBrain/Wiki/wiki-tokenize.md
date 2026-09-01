# wiki-tokenize · `Functions/tokenize.py`

`tokenize(text) -> list[str]`. Manual whitespace split: `is_whitespace(char)` treats space/tab/
newline/CR as boundaries; accumulates non-whitespace chars into `current_word`, flushes on each
boundary and once more at end-of-text. No `str.split()` — by design.

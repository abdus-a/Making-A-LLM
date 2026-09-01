# wiki-remove_punctuation · `Functions/remove_punctuation.py`

`clean_words(words) -> list[str]` maps each word through `remove_punctuation`, which drops any
char where `is_punctuation` is true. **Currently only `.` and `,` are stripped** — other symbols
survive. Fine for the controlled corpus; broaden later if needed ([[Open-Actions]]).

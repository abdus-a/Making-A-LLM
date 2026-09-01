# wiki-make_lowercase · `Functions/make_lowercase.py`

`make_lowercase(text) -> str`. Walks each char; if `"A" <= char <= "Z"`, adds 32 to its ASCII
code (`chr(ord(char)+32)`) to get the lowercase letter. No `str.lower()` — by design
([[ADR-0001-pure-python-no-libraries]]).

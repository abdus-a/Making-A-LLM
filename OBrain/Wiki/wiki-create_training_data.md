# wiki-create_training_data · `Functions/create_training_data.py`

`create_training_data(words, word_ids) -> (inputs, targets)`. For each adjacent pair `(words[i],
words[i+1])`, appends `word_ids[words[i]]` to `inputs` and `word_ids[words[i+1]]` to `targets`.
Result: aligned lists of integer ids where `targets[k]` is the word that followed `inputs[k]` —
the next-word training signal. Contract detail → [[Architecture]].

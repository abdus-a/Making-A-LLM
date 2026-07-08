def create_word_ids(vocabulary):

    word_ids = {}

    index = 0

    for word in vocabulary:
        
        word_ids[word] = index

        index += 1

    return word_ids

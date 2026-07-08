def create_training_data(words, word_ids):
    
    inputs = []

    targets = []

    for i in range(len(words) - 1 ):
        
        current_word = words[i]

        next_word = words [i + 1]

        current_id = word_ids[current_word]

        next_id = word_ids[next_word]

        inputs.append(current_id)

        targets.append(next_id)

    return inputs, targets

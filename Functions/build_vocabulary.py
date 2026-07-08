def build_vocabulary(words): #function to build the vocabulary takes a list of words as input
    
    vocabulary = [] #initialize an empty list to store the vocabulary

    for word in words:
       
        found = False

        for vocab_word in vocabulary:

            if word == vocab_word:
              
                found = True

                break
            
        if not found:
                
            vocabulary.append(word)

   
    return vocabulary #return the vocabulary

def is_punctuation(char): #function to check if the character is a punctuation character
    if char == "." or char == ",": #check if the character is a punctuation character ('.', ',')
        return True # return True if the character is a punctuation character

    return False # return False if the character is not a punctuation character

def remove_punctuation(word): #function to remove the punctuation from the text
    clean_word = "" #initialize an empty string to store the clean word

    for char in word: #iterate through each character in the word
        if not is_punctuation(char): #check if the character is not a punctuation character

            clean_word += char #add the character to the clean word

    return clean_word #return the clean word

def clean_words(words): #function to clean the words
    clean_words = [] #initialize an empty list to store the clean words

    for word in words: #iterate through each word in the list of words
        
        clean_word = remove_punctuation(word) #remove the punctuation from the word

        clean_words.append(clean_word) #add the clean word to the list of clean words
    
    return clean_words #return the list of clean words
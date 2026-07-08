def is_whitespace(char): #function to check if the character is a whitespace character

    if char == " " or char == "\t" or char == "\n" or char == "\r": #check if the character is a whitespace character
        return True #return True if the character is a whitespace character
    else:
        return False #return False if the character is not a whitespace character

def tokenize(text): #function to tokenize the text takes a string as input
    words = [] #initialize an empty list to store the words
    current_word = "" #initialize an empty string to store the current word

    for char in text: #iterate through each character in the text

        if not is_whitespace(char): #check if the character is not a whitespace character
            current_word += char #add the character to the current word

        else:
            if current_word != "": #check if the current word is not empty
                words.append(current_word) #add the current word to the list of words
                current_word = "" #reset the current word
    if current_word != "": #check if the current word is not empty after the loop ends
        words.append(current_word) #add the current word to the list of words after the loop ends as we are at the end of the passed text
        

    return words #return the list of words tokenized




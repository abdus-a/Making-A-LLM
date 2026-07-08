def make_lowercase(text): #function to make the text lowercase takes a string as input
    result = "" #initialize an empty string to store the result

    for char in text: #iterate through each character in the text

        if "A" <= char <= "Z": #check if the character is an uppercase letter
            char = chr(ord(char) + 32) #convert the character to a lowercase letter by adding 32 to the ASCII value

        result += char #add the character to the result

    return result #return the result

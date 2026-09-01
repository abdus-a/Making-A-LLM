from NeuralNetwork.simple_random import SimpleRandom

class Embedding: # declared the class
    def __init__(self, vocab_size, embedding_dim, seed=42): # defined the self 
        # vocab_size = how many words we have (here we have 117 so 117 rows)
        # embedding_dim = how many numbers per word (how much detial about the word can be stored here were doing 3 = 3 col)
        self.vocab_size = vocab_size # Store the object vocab size
        self.embedding_dim = embedding_dim # Store the object embedding dim 
        self.rng = SimpleRandom(seed)

        self.table = [] # Create and store the table for embeddings

        for i in range(vocab_size): # loop for every word in the trainning set being fed
            row = [] # Declare the row
            for j in range(embedding_dim): # loop for every detail being stored here 3 perhapes then we have 4 word 3 details (3,4)
                row.append(self.rng.next_number()) # append the data into the row
            self.table.append(row) # commit to the main table the embedding for the word (row)
    def lookup(self, word_id):
        return self.table[word_id]

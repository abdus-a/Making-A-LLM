from NeuralNetwork.embedding import Embedding
from Assets.training_sentences import training_sentences
from Functions.make_lowercase import make_lowercase
from Functions.tokenize import tokenize
from Functions.remove_punctuation import clean_words
from Functions.build_vocabulary import build_vocabulary
from Functions.create_training_data import create_training_data
from Functions.create_word_ids import create_word_ids


text = make_lowercase(training_sentences)

words = tokenize(text)

words = clean_words(words)

vocabulary = build_vocabulary(words)

word_ids = create_word_ids(vocabulary)

inputs, targets = create_training_data(words, word_ids)

embedding = Embedding(len(vocabulary), 4)
print(embedding.lookup(word_ids["we"]))


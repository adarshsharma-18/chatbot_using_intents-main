# Importing necessary libraries
import random
import json
import pickle
import numpy as np
import nltk

# Importing required classes and functions from NLTK
from nltk.stem import WordNetLemmatizer

# Importing the trained model from Keras
from keras.models import load_model

# Initializing the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Loading intents data from JSON file
intents = json.loads(open('intents.json').read())

# Loading preprocessed data from pickle files
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# Loading the trained model
model = load_model('chatbot_model.h5')

# Function to preprocess the input sentence
def clean_up_sentence(sentence):
    # Tokenizing the input sentence into words
    sentence_words = nltk.word_tokenize(sentence)
    # Lemmatizing each word to its base form
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

# Function to create a bag of words from the input sentence
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

# Function to predict the class (intent) of the input sentence
def predict_class(sentence):
    # Creating a bag of words for the input sentence
    bow = bag_of_words(sentence)
    # Predicting the class probabilities using the trained model
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    # Filtering out predictions with low probabilities
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # Sorting the results by probability in descending order
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    # Creating a list of intents along with their probabilities
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

# Function to get a response based on the predicted intent
def get_response(intents_list, intents_json):
    # Extracting the predicted intent
    tag = intents_list[0]['intent']
    # Retrieving the responses corresponding to the predicted intent
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            # Selecting a random response from the list of responses
            result = random.choice(i['responses'])
            break
    return result

# Main program loop
print("GO! Bot is running!")
while True:
    # Getting user input
    message = input("")
    # Predicting the intent of the input message
    ints = predict_class(message)
    # Retrieving a response based on the predicted intent
    res = get_response(ints, intents)
    # Printing the response
    print(res)

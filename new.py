# Importing necessary libraries
import random
import json
import pickle
import numpy as np
import tensorflow as tf
import nltk
from nltk.stem import WordNetLemmatizer

# Initializing WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Loading intents data from JSON file
intents = json.loads(open('intents.json').read())

# Initializing lists to store words, classes, and documents
words = []
classes = []
documents = []
# Ignoring punctuation marks
ignoreLetters = ['?', '!', '.', ',']

# Processing intents and patterns to create vocabulary and training data
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenizing words in patterns
        wordList = nltk.word_tokenize(pattern)
        words.extend(wordList)
        # Storing documents (patterns and their associated tags)
        documents.append((wordList, intent['tag']))
        # Adding intent tag to classes list if not already present
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatizing and filtering words
words = [lemmatizer.lemmatize(word) for word in words if word not in ignoreLetters]
# Sorting and removing duplicates from words and classes
words = sorted(set(words))
classes = sorted(set(classes))

# Saving words and classes lists to pickle files
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Creating training data
training = []
outputEmpty = [0] * len(classes)

for document in documents:
    bag = []
    wordPatterns = document[0]
    # Lemmatizing and lowercasing words in patterns
    wordPatterns = [lemmatizer.lemmatize(word.lower()) for word in wordPatterns]
    # Creating bag of words
    for word in words:
        bag.append(1) if word in wordPatterns else bag.append(0)

    # Creating output row (one-hot encoded) for each document
    outputRow = list(outputEmpty)
    outputRow[classes.index(document[1])] = 1
    training.append(bag + outputRow)

# Shuffling training data
random.shuffle(training)
# Converting training data to numpy array
training = np.array(training)

# Splitting training data into input (X) and output (Y)
trainX = training[:, :len(words)]
trainY = training[:, len(words):]

# Building the neural network model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, input_shape=(len(trainX[0]),), activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(trainY[0]), activation='softmax'))

# Compiling the model with stochastic gradient descent optimizer
sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Training the model
hist = model.fit(np.array(trainX), np.array(trainY), epochs=200, batch_size=5, verbose=1)

# Saving the trained model
model.save('chatbot_model.h5', hist)
print('Done')

# Chatbot Using Intents

## Overview
This project involves the development of a chatbot that uses Natural Language Processing (NLP) and machine learning to understand user queries and respond appropriately. The chatbot categorizes user inputs into predefined topics known as "intents" and provides responses that are contextually relevant.

## Features
- **Intent Recognition**: The chatbot can identify various intents such as greetings, farewells, inquiries, and commands based on user input.
- **Contextual Responses**: Provides appropriate responses according to the recognized intent.
- **Versatile Functionality**: Includes features like telling jokes, providing weather updates, and answering questions about the chatbot's abilities.

## Project Structure
- `intents.json`: Contains the data set of user intents, including patterns (user inputs) and responses.
- `words.pkl` and `classes.pkl`: Pickle files containing processed vocabulary and intent classes.
- `chatbot_model.h5`: The trained neural network model for predicting intents.
- `chatbot.py`: The main script for running the chatbot.

## Setup and Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/adarshsharma-18/chatbot_using_intents-main
   cd chatbot-using-intents
   ```

2. **Install required dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install numpy nltk tensorflow keras
   ```

3. **Download NLTK Data**:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   ```

## How It Works
1. **Data Preprocessing**:
   - Tokenizes the patterns in `intents.json` into words.
   - Lemmatizes the words to their root form.
   - Creates a bag-of-words model to convert textual data into numerical form for the model.

2. **Model Training**:
   - A neural network is trained using the processed data to classify intents based on user input.
   - The model uses a feed-forward neural network with dense layers and dropout for regularization.

3. **Intent Prediction**:
   - The trained model predicts the intent of new user inputs by matching the input against the known patterns.
   - If the confidence level of the prediction exceeds a certain threshold, the chatbot responds with an appropriate response from `intents.json`.

4. **Response Generation**:
   - Based on the predicted intent, the chatbot selects a response from a predefined list associated with that intent.

## Usage
Run the `chatbot.py` script to start the chatbot:
```bash
python chatbot.py
```
The chatbot will prompt you to enter a message. It will process the input, predict the intent, and provide a relevant response.

## Libraries and Tools
- **NLTK**: Used for text preprocessing, including tokenization and lemmatization.
- **TensorFlow and Keras**: Used for building and training the neural network model.
- **NumPy**: Used for numerical computations and data manipulation.

## Future Improvements
- **Expand Intents**: Add more intents and responses to handle a wider range of user queries.
- **Context Management**: Implement context tracking to manage multi-turn conversations better.
- **API Integration**: Integrate external APIs for real-time functionalities like weather updates and news.

## Contribution
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Contact
For any questions or suggestions, please contact Adarsh Sharma at adarshsharma1124@gmail.com.

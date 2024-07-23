# Stock Portfolio Manager

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [API References](#api-references)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction

The Stock Portfolio Manager is a comprehensive application designed to help users manage their stock portfolios efficiently. It leverages real-time financial data, provides portfolio valuation updates, and offers insightful visualizations. Built using Python, it integrates with various APIs to fetch the latest market data and uses machine learning models for predictive analysis.

## Features

- Real-time stock price updates
- Portfolio valuation and performance tracking
- Integration with financial data APIs
- User-friendly interface with interactive charts
- Secure user authentication
- Natural language processing for querying stock information
- Historical data analysis
- Automated portfolio rebalancing suggestions
- News aggregation related to stocks in the portfolio

## Requirements

- Python 3.7 or higher
- MySQL server
- Internet connection for API data fetching

### Python Packages:

- `speech_recognition`
- `webbrowser`
- `openai`
- `os`
- `datetime`
- `random`
- `pyttsx3`
- `mysql-connector-python`
- `flask`
- `flask-login`
- `pandas`
- `matplotlib`

## Installation

### Clone the Repository

```bash
git clone https://github.com/adarshsharma-18/stock-portfolio-manager.git
cd stock-portfolio-manager
```

### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install the Required Packages

```bash
pip install -r requirements.txt
```

### Set Up the MySQL Database

Create a database in your MySQL server and run the following SQL command to create the necessary table:

```sql
CREATE DATABASE stock_portfolio_manager;

USE stock_portfolio_manager;

CREATE TABLE voice_assistant (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_command TEXT NOT NULL,
    ai_response TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Configuration

Create a `config.py` file in the root directory and add your OpenAI API key:

```python
apikey = 'your_openai_api_key'
```

## Usage

### Starting the Application

Run the main application script:

```bash
python app.py
```

### Using the Voice Assistant

Upon running, the voice assistant will introduce itself as Jarvis and start listening for your commands. You can interact with it using natural language commands such as:

- "Open YouTube"
- "What's the time?"
- "Tell me a joke"
- "Who is Elon Musk?"

The assistant will respond with appropriate actions or information, and it will log the user commands and AI responses to the MySQL database.

## Project Structure

```
stock-portfolio-manager/
│
├── Openai/
│   ├── ... (Stored AI responses)
│
├── static/
│   ├── css/
│   ├── js/
│   └── ... (Static files for the web interface)
│
├── templates/
│   ├── index.html
│   └── ... (HTML templates)
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

## API References

- [OpenAI API](https://beta.openai.com/)
- [Alpha Vantage API](https://www.alphavantage.co/documentation/)
- [Yahoo Finance API](https://developer.yahoo.com/finance-api/)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

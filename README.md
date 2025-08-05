# Emotion Detection Web App

This project is a Flask-based web application for detecting emotions in user-input text using a transformer-based model.

## Features

- **Emotion Detection:** Enter any text and get the dominant emotion along with scores for each detected emotion.
- **Web Interface:** Simple form for text input and results display.
- **Powered by Transformers:** Uses Hugging Face's `transformers` and `torch` libraries for emotion analysis.

## How It Works

1. The user enters text in the web form.
2. The app sends the text to the `emotion_detector` function.
3. The function returns a dictionary with emotion scores and the dominant emotion.
4. The results are displayed on the page.

## Project Structure

```
emotion_detection/
    __init__.py
    emotion_detector.py
app.py
templates/
    index.html
setup.py
README.md
```

- `app.py`: Main Flask application.
- `emotion_detection/emotion_detector.py`: Contains the emotion detection logic using transformers.
- `templates/index.html`: HTML template for the web interface.
- `setup.py`: Project setup and dependencies.

## Installation

1. **Clone the repository:**
    ```
    git clone <repo-url>
    cd oaqjp-final-project-emb-ai
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
    Or manually:
    ```
    pip install flask transformers torch
    ```

## Usage

1. **Run the app:**
    ```
    python app.py
    ```
2. **Open your browser:**  
   Go to `http://127.0.0.1:5000/`

3. **Enter text:**  
   Submit text to see detected emotions.

## Example

```
Input: "I am so happy today!"
Output: Dominant Emotion: Joy
        Scores: {'joy': 0.95, 'sadness': 0.01, ...}
```

## Requirements

- Python 3.7+
- Flask
- transformers
- torch

## Author

Raj Mishra

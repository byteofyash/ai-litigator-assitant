# AI Litigator Assistant

A web application designed to assist law students and junior lawyers by quickly summarizing legal documents using Artificial Intelligence. This project aims to improve efficiency and comprehension when dealing with large amounts of legal text.


## Current Status 

The project currently implements the core functionality of **Text Summarization**. Users can paste legal text into the web interface and receive an AI-generated summary. This serves as the Minimum Viable Product (MVP) demonstrated for the hackathon's mid-evaluation point.

## Features

### Implemented

*   **Web Interface:** Simple HTML/CSS/JS frontend for text input and summary output.
*   **Backend API:** Flask-based server to handle requests.
*   **AI Summarization:** Integrates with the Hugging Face `transformers` library using the `[sshleifer/distilbart-cnn-6-6]` model to generate concise summaries of input text.

### Planned / Next Steps

*   **Named Entity Recognition (NER):** Integrate spaCy or another library to identify and extract key entities (e.g., Persons, Organizations, Locations, Legal Statutes) from the text.
*   **Improved UI/UX:** Enhance the user interface for better usability and visual appeal.
*   **Error Handling:** More robust error handling on both frontend and backend.
*   **Document Upload:** Allow users to upload files (e.g., .txt, .pdf) instead of just pasting text.
*   **(Stretch Goal) Basic Template Drafting:** Explore generating outlines for common legal documents based on extracted information.

## Tech Stack

*   **Backend:** Python 3.x, Flask
*   **AI / NLP:** Hugging Face `transformers` (`sshleifer/distilbart-cnn-6-6`), PyTorch (as backend for transformers)
*   **Frontend:** HTML5, CSS3, Vanilla JavaScript (using Fetch API)
*   **Environment:** Python Virtual Environment (`venv`), Git

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/byteofyash/ai-litigator-assitant
    cd project folder
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    # Create venv
    python -m venv venv

    # Activate venv
    # Linux/macOS:
    source venv/bin/activate
    # Windows:
    .\venv\Scripts\activate
    ```

3.  **Install dependencies:**
    *(Make sure you have created a `requirements.txt` file first using `pip freeze > requirements.txt`)*
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: The first time you run the app, the transformers library might download the pre-trained model, which can take some time and requires an internet connection.)*

4.  **Run the Flask application:**
    ```bash
    python app.py
    ```

5.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000/` (or the address provided by Flask).

## Usage

1.  Navigate to the application URL in your browser.
2.  Paste the legal text you wish to summarize into the provided text area.
3.  Click the "Summarize" button.
4.  Wait for the AI model to process the text (this may take a few seconds depending on text length and server performance).
5.  The generated summary will appear in the "Summary" output section below the button.

## Demo Video

*(Link to video demonstration will be added later)*

## Team

*   Yash Ranjan


**Crucial:** Make sure you have run `pip freeze > requirements.txt` in your activated virtual environment *after* installing Flask, transformers, torch/tensorflow, etc., and committed that `requirements.txt` file to your GitHub repository. The setup instructions depend on it!

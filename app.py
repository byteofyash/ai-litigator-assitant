# app.py

from flask import Flask, request, jsonify, render_template
# Make sure ai_processor.py is in the same directory and has the get_summary function
from ai_processor import get_summary

print("Flask app starting...") # Optional: helps confirm the file is running
print(f"Attempting to import get_summary: {callable(get_summary)}") # Optional: debug check

app = Flask(__name__)
print("Flask app instance created.")

@app.route('/')
def index():
    print("Request received for / route.")
    # This line requires an 'index.html' file in a 'templates' folder
    # If you don't have it yet, Flask will show an error.
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    print("Request received for /summarize route (POST).")
    try:
        # 1. Get data from the incoming request
        data = request.json
        print(f"Received data: {data}") # Debug print

        # 2. Validate input
        if not data or 'text' not in data:
            print("Error: 'text' field missing in request JSON.")
            return jsonify({'error': 'No text provided in request body'}), 400

        input_text = data['text']
        # Optional: Basic check for empty text
        if not input_text.strip():
             print("Error: Received empty text string.")
             return jsonify({'error': 'Text cannot be empty'}), 400

        print(f"Input text length: {len(input_text)}") # Debug print

        # 3. Call your AI function
        print("Calling get_summary function...")
        summary = get_summary(input_text)
        print(f"Summary generated: {summary[:100]}...") # Debug print

        # 4. Send the result back as JSON
        return jsonify({'summary': summary})

    except Exception as e:
        print(f"Error in /summarize route: {e}")
        # Log the full error trace for debugging during development
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'An internal server error occurred'}), 500


if __name__ == '__main__':
    print("Starting Flask development server on http://0.0.0.0:5000")
    # Setting host='0.0.0.0' makes the server accessible from other devices on your network
    # (useful for testing from a phone, but be mindful of security).
    # For purely local development, you can omit host or use '127.0.0.1'.
    app.run(debug=True, host='0.0.0.0', port=5000)
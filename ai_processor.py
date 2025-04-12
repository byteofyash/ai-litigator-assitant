# Step 1: Import the necessary library component
# 'pipeline' is a high-level helper from Hugging Face transformers
# that makes using pre-trained models for specific tasks very easy.
from transformers import pipeline
import torch # Or tensorflow if you installed that

# Step 2: Load the summarization pipeline
# We need to choose a pre-trained model suitable for summarization.
# - "sshleifer/distilbart-cnn-6-6": A smaller, faster version of BART. Good starting point for a hackathon.
# - "facebook/bart-large-cnn": A larger, potentially more accurate model, but slower and needs more resources.
# - "google/pegasus-xsum": Another popular summarization model.
# Let's start with the faster DistilBART.
# The 'pipeline' function will automatically download the model and tokenizer the first time you run this.
# It's good practice to load the model *outside* the function definition
# so it's loaded only once when the script starts, not every time the function is called.
print("Loading summarization model...")
try:
    # Specify the task ("summarization") and the model name
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-6-6")
    # You could optionally specify device=0 to try and use a GPU if available and configured:
    # summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-6-6", device=0)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    print("Please ensure you have an internet connection for the first download.")
    print("Also check if PyTorch or TensorFlow is installed correctly.")
    summarizer = None # Set to None if loading failed

# Step 3: Define the function to perform summarization
def get_summary(text_input, max_length=150, min_length=30):
    """
    Generates a summary for the given text using the pre-loaded pipeline.

    Args:
        text_input (str): The text to summarize.
        max_length (int): The maximum number of tokens for the summary.
        min_length (int): The minimum number of tokens for the summary.

    Returns:
        str: The generated summary, or an error message if summarization fails.
    """
    if summarizer is None:
        return "Error: Summarization model not loaded."

    if not isinstance(text_input, str) or not text_input.strip():
        return "Error: Input text cannot be empty."

    try:
        print(f"Generating summary for text (first 100 chars): {text_input[:100]}...")
        # The pipeline handles tokenization, model inference, and decoding.
        # 'do_sample=False' generally leads to more deterministic summaries.
        summary_list = summarizer(text_input, max_length=max_length, min_length=min_length, do_sample=False)

        # The pipeline returns a list containing a dictionary.
        # We need to extract the actual summary text.
        if summary_list and isinstance(summary_list, list) and 'summary_text' in summary_list[0]:
            generated_summary = summary_list[0]['summary_text']
            print("Summary generated.")
            return generated_summary
        else:
            print("Warning: Unexpected output format from summarizer pipeline.")
            return "Error: Could not extract summary from model output."

    except Exception as e:
        # Catch potential errors during the summarization process
        print(f"Error during summarization process: {e}")
        # You might get errors if the input text is too long for the model's context window.
        # Handling that properly (e.g., chunking) is complex and likely out of scope for the hackathon MVP.
        return f"Error generating summary: {e}"

# Step 4: Add a test block (optional but highly recommended)
# This code will only run when you execute `python ai_processor.py` directly.
# It allows you to test the 'get_summary' function without needing the Flask app yet.
if __name__ == "__main__":
    print("\n--- Testing AI Processor ---")

    # Replace this with a short snippet of sample legal text
    sample_legal_text = """
    This Non-Disclosure Agreement (the "Agreement") is entered into as of October 26, 2023,
    by and between ACME Corporation, a Delaware corporation with its principal place of
    business at 123 Main Street, Anytown, USA ("Disclosing Party"), and Beta Innovations Inc.,
    a California corporation with its principal place of business at 456 Innovation Drive,
    Techville, USA ("Receiving Party"). WHEREAS, the Disclosing Party possesses certain
    confidential and proprietary information relating to its new widget technology
    (the "Confidential Information"); and WHEREAS, the Receiving Party desires to evaluate
    such Confidential Information for the potential purpose of entering into a business
    relationship with the Disclosing Party; NOW, THEREFORE, in consideration of the mutual
    covenants contained herein, the parties agree as follows: The Receiving Party agrees
    not to disclose the Confidential Information to any third party.
    """

    print("\nInput Text:")
    print(sample_legal_text)

    print("\nRequesting Summary...")
    # Call the function we defined above
    summary_result = get_summary(sample_legal_text)

    print("\nSummary Result:")
    print(summary_result)

    print("\n--- Testing Complete ---")
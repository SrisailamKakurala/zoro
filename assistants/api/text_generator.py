from dotenv import load_dotenv
import google.generativeai as genai
import os
import unicodedata

# Load environment variables from .env file
load_dotenv()


# Function to normalize the text
def normalize_text(text):
    # Normalize the text to remove hidden characters
    text = unicodedata.normalize('NFKD', text)
    # Replace any remaining special characters with spaces
    for char in ['*', '-', '_', '•', '#', '@']:
        text = text.replace(char, ' ')
    return text

def get_text_response(query):
    try:
        # Configure the API key
        api_key = os.getenv('API_KEY')
        if not api_key:
            raise ValueError("API_KEY not found in environment variables.")
        
        genai.configure(api_key=api_key)

        # Create the generative model instance
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Generate content
        response = model.generate_content(query)

        # Normalize the text
        normalized_text = normalize_text(response.text)

        print(normalized_text)
        return normalized_text

    except ValueError as ve:
        print(f"ValueError: {ve}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

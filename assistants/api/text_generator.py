from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables from .env file
load_dotenv()


def get_text_response(query):
    
    try:
        # Configure the API key
        api_key = os.getenv('API_KEY')
        if not api_key:
            raise ValueError("API_KEY not found in environment variables.")
        
        genai.configure(api_key=api_key)

        # Create the generative model instance
        model = genai.GenerativeModel('gemini-1.0-pro-latest')

        # Generate content
        response = model.generate_content(query)

        # Print the generated text
        res = response.text.replace('*', '')
        print(res)
        return response.text

    except ValueError as ve:
        print(f"ValueError: {ve}")

    except genai.GenerativeAIError as gaie:
        print(f"GenerativeAIError: {gaie}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

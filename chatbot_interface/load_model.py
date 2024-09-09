import google.generativeai as genai
import os

#loading the environment variable
from dotenv import load_dotenv
load_dotenv()


def get_model():
    """
    return the model
    Args:
    None
    Return:
        model objext
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.0-pro')
    return model
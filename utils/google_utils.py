from dotenv import load_dotenv
from langchain import HuggingFaceHub
import os
load_dotenv()

def getApiKey():
    """
    get api key from the env file
    Args:
        None
    Return:
        api_key
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    return api_key




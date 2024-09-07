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
    api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    print(f"the api key is {api_key}")
    return api_key

def load_model(api_key, temperature=0.2, max_token=30):
    """
    return the model instance
    Args:
        api_key : api key
        temperature : temperature of model
        max_token :  maximum token to proces
    Return:
        langchain model instance
    """
    modelid ="google/gemma-7b"
    conversation_model = HuggingFaceHub(huggingfacehub_api_token =api_key, repo_id = modelid, model_kwargs={"temperature":temperature, "max_new_tokens":max_token})

    return conversation_model

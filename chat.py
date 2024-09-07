#loading the modules
import os 
import langchain
import chainlit as cl
from langchain import HuggingFaceHub, PromptTemplate, LLMChain
from getpass import getpass
from dotenv import load_dotenv
load_dotenv()

#external libraries
import utils.model_utils as util


#getting the api key
api_key = util.getApiKey()

#loading the model
model = util.load_model(api_key = api_key, max_token=200)

template =""" 
what is {query}
"""

prompt = PromptTemplate(template = template, input_variable = ['query'])


conv_chain = LLMChain( llm= model,
                        prompt = prompt,
                        verbose = False
                      )

print(conv_chain.invoke("deep learning"))


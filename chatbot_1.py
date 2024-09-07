import os 
import chainlit as cl
from langchain import HuggingFaceHub, PromptTemplate, LLMChain
from dotenv import load_dotenv

#loading the enviroenment variable
load_dotenv()
HUGGING_FACE_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

model_id = "gpt2-medium"
conversation_model = HuggingFaceHub(
    huggingfacehub_api_token =HUGGING_FACE_API_TOKEN, 
    repo_id = model_id,
    model_kwargs={"temperature":0.2, "max_new_tokens":200}
    )



template =""" 
what is {query}
"""



# interface setup

@cl.on_chat_start
def main():
    prompt = PromptTemplate(template = template, input_variable = ['query'])
    llm_chain = LLMChain(prompt=prompt, llm=conversation_model,verbose=True)
    cl.user_session.set('llm_chain',conversation_model)
    return llm_chain

@cl.on_message
async def main(message:str):
    llm_chain = cl.user_session.get("llm_chain")
    res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])

    await cl.Message(content=res["text"]).send()



import sys
import json
import ast


data_to_pass_back = "vivek this to node process."
input = sys.argv[1]



# model code
import google.generativeai as genai
import os
# import key
import PIL.Image


from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-1.0-pro')

response=model.generate_content(f" {input}")

output = response.text
print(output)
sys.stdout.flush()
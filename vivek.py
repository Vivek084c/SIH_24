import sys
import json
import ast

# model code
import google.generativeai as genai
import os

#loading the environment variable
from dotenv import load_dotenv
load_dotenv()
from chatbot_interface.model_context import basic_context


input = sys.argv[1]


#### configuring the model
#configuring the api key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
#configuring the model
model = genai.GenerativeModel('gemini-1.0-pro')


#### generating the response

context =  """"
    LearNet is a freelancing platform to allow user to get freelancing job and upgrade their skillset, The goal is to build a freelancing platform specifically for India, 
    addressing the gap in connecting freelancers and gig workers with short-term and project-based job opportunities., it consist of 6 memebers, namely vivek, the team lead who manages the overall work flow along with handling the machine learning side of the projext,
    yash, who has developed the ui and ux of the projext, divyansh, who has developed the front end and backend alog with hemant, then we have ratish who has worked on the 
    recomendation model and at the end we have dishita who has worked on the presentation part
    
    expected functionality of the site:
    1.	Freelance Job Marketplace:
	•	Develop a platform where freelancers can find short-term jobs and project-based opportunities.
	•	Allow employers to post projects, set requirements, and invite freelancers.
	2.	Freelancer Profile and Portfolio Management:
	•	Enable freelancers to create detailed profiles showcasing skills and past work.
	•	Include a rating and review system for feedback on completed projects.
	3.	Extensive Search & Analytics:
	•	Provide advanced search capabilities for both freelancers and employers.
	•	Implement AI-based recommendation systems and insights for better engagement and job matching.
	4.	Escrow Account Creation:
	•	Integrate secure payment gateways and create escrow accounts to hold payments until job completion.

    Expected Outcome:
    The platform will connect freelancers with diverse job opportunities, providing efficient tools for project management, leading to increased income and 
    job satisfaction. The solution encourages out-of-the-box thinking for innovation in specific industries or creating a generic platform.

    To create a new user profile follow the bellow steps:
    1) Clickonsingupbutton
    2) Enteryourdetails
    3) Clickonsubmit
    4) Checkyouremailtoreceivetheotp 5) Entertheotp
    6) Yoursingupisdone

    To login to your account:
    1) Go to homepage
    2) Check the login button on top right corner 
    3) Click on it, you will be redirectedt on site 
    4) Enter details and you will be loged in
    """

rule = """
1) answer to on point and in simple form 
2) do not answer beyoud the scope of what is asked
3) you can reply with response that i am not smart enough to answer that, you can ask me questioins related to the site.
"""

response_type = """

"""
base_info = f"""
your name is DYVHDR, you are a smart chat-bot developed by team LearNet, You  are designed to anwer question related to the out site, here is all the context that you need:
{context} :
while following the following rule while ansewr a paticular question :
{rule}

"""
response=model.generate_content(f" {input} + {base_info}")


output = response.text
print(output)
sys.stdout.flush()
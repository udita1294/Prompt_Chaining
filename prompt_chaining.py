import os
from dotenv import load_dotenv
from pathlib import Path
from groq import Groq
from time import sleep

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable not set")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

JD="""
We are hiring a Backend Python Developer.

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- AWS
- REST APIs
- 2+ years of experience
"""

RESUME="""
Name: Rahul Sharma
Experience:
3 years as a Software Developer.
Skills:
Python, FastAPI, MySQL, Docker,
REST APIs, Git

Projects:
Built a food delivery backend using
FastAPI and MySQL.

Deployed applications using Docker.
"""

def ask_llm(system_prompt,user_prompt):
    system_message = {"role": "system", "content": system_prompt}
    user_message = {"role": "user", "content": user_prompt}
    messages = [system_message, user_message]
    response = client.chat.completions.create(model=model, messages=messages)
    ans = response.choices[0].message.content
    return ans

def step1_resume_extraction():
    system_prompt = """
        You are a professional HR assistant. Extract skills from the candidate resume provided. Only extract the skills no other information.
        Do not invent any skills by yourself.
        """
    user_prompt = f"""Extract skills from this resume: {RESUME}"""
    return ask_llm(system_prompt, user_prompt)

def step2_jd_analysis():
    system_prompt = """
        You are a professional HR assistant. Extract skills from the Job Description provided. Only extract the skills no other information.
        Do not invent any skills by yourself.
        """
    user_prompt = f"""Extract skills from this job description: {JD}"""
    return ask_llm(system_prompt, user_prompt)

def step2_match(candidate,jd):
    system_prompt = """
            You are a professional HR assistant. Compare the skills of the candidate and the skills required fro the JD and produce a final 
            score between 0 to 100. Also produce a short verdict whether the candidate is a good fit for this role or not.
            Do not invent any skills by yourself.
            """
    user_prompt = f"""compare and match the skills
            Job Description:{JD_skills}
            Candidate :{Candidate}
            """
    return ask_llm(system_prompt, user_prompt)


Candidate = step1_resume_extraction()
sleep(2)
JD_skills = step2_jd_analysis()
sleep(2)
match_result = step2_match(Candidate, JD_skills)
print("Result : ", match_result)

import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def get_ai_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.9,
        messages=messages
    )
    return response.choices[0].message.content

messages = [
    {"role" : "system", "content" : "너는 사용자를 도와주는 상담사야."}
]   

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    messages.append({"role" : "user", "content" : user_input})
    response = get_ai_response(messages)    
    messages.append({"role" : "assistant", "content" : response})
    print("AI:"  + response)
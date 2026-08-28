import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"

# ==============================
# EXAMPLE 1: SYSTEM MESSAGE
# ==============================

role = "user"
prompt = "i love u"

# System message - controls the behavior/personality of the AI
message_system = {
    "role": "system",
    "content": "You are my strict boss who is my manager. You are very strict and you will scold me when I don't do my work."
}

# User message
message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]

response = client.chat.completions.create(
    model=model,
    messages=messages
)

answer = response.choices[0].message.content

print("SYSTEM MESSAGE EXAMPLE:")
print(answer)

print("#######################################")


# ==============================
# EXAMPLE 2: TEMPERATURE = 1
# ==============================

prompt = "Suggest me a delicious food name"

message = {
    "role": "user",
    "content": prompt
}

messages = [message]

# Temperature = 1
# Higher temperature allows more varied/creative responses
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1
)

answer = response.choices[0].message.content

print("TEMPERATURE = 1 EXAMPLE:")
print(answer)
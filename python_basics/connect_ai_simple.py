from dotenv import load_dotenv
import os
from openai import OpenAI

# STEP 1: Load .env file
load_dotenv()

# STEP 2: Define the OpenAI Variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# STEP 3: Make the LLM request
response = client.responses.create(
    model="gpt-5.6-luna",
    input=input("Enter your question for the AI: ")
)

# STEP 4: Print the response
print(response.output_text)
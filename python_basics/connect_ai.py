from dotenv import load_dotenv
import os
import requests
import json

# STEP 1: Load environment variables from .env file
load_dotenv()  

# STEP 2: Ask for the Customer query and store it in a variable
human_query = input("Enter your question for the AI: ")

# STEP 3: Declare the OpenAI API key and the endpoint URL
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# STEP 4: Set the OpenAI URL
OPENAI_URL = "https://api.openai.com/v1/responses"

# STEP 5: Set the Headers
OPENAI_HEADERS = {"Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API_KEY}"}
                                               
# STEP 6: Set the Data / Payload
OPENAI_DATA = {"model": "gpt-6-luna", "input": human_query}

# STEP 7: Make the Connection
response = requests.post(OPENAI_URL, headers=OPENAI_HEADERS, data=json.dumps(OPENAI_DATA))

print (response.json()['output'][1]['content'][0]['text'])

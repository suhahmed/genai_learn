import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
COUNTRY_CODE = input("Enter the country code (e.g., 'us' for the United States): ")
ZIP_CODE = input("Enter the ZIP code (e.g., '10001' for New York): ")

OPENWEATHERMAP_URL = f"http://api.openweathermap.org/data/2.5/weather?zip={ZIP_CODE},{COUNTRY_CODE}&appid={OPENWEATHERMAP_API_KEY}&units=metric"

print("OpenWeatherMap API URL:", OPENWEATHERMAP_URL)

response = requests.get(OPENWEATHERMAP_URL) # Making the connection to the OpenWeatherMap API and getting the response.
print("Response Status Code:", response.status_code) # Printing the status code of the response.
print("Response Content:", response.json()) # Printing the JSON content of the response.
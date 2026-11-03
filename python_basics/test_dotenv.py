from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

my_var_one = os.getenv("OPENWEATHERMAP_API_KEY")
my_var_two = os.getenv("ROOT_PASSWORD")

print (f"OPENWEATHERMAP_API_KEY: {my_var_one}")
print (f"ROOT_PASSWORD: {my_var_two}")


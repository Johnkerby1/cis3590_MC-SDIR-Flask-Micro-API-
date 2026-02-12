import requests
import os
from dotenv import load_dotenv

load_dotenv()

url= "https://api.nasa.gov/planetary/apod?api_key="
unique_key = os.getenv("NASA_API_KEY")



def apod_generator(url_nasa, key):
    final_url = url + unique_key
    response = requests.get(final_url).json()
    return response

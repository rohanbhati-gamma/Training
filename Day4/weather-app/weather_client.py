import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = 'b235b41228a5244d6d9fe43a90818e8b'
def get_weather_data(city):
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "error" in data:
            return {"error": data["error"]["info"]}

        current = data["current"]
        location = data["location"]

        return {
            "city": location["name"],
            "country": location["country"],
            "temperature": current["temperature"],
            "description": current["weather_descriptions"][0],
            "humidity": current["humidity"],
            "wind_speed": current["wind_speed"]
        }
    else:
        return {"error": "Failed to fetch data from Weatherstack"}
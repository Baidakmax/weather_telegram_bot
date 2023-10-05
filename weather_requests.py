import requests
from config import TOKEN_BOT, API


TOKEN = TOKEN_BOT
def city_weather(city):
    OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
    api_key = API

    weather_params = {
        'q': f'{city}',
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(OWM_Endpoint, params=weather_params)
        response.raise_for_status()
        weather_data = response.json()
        farengeit = f"Temperature: {weather_data['main']['temp']}"
        description = f"Description: {weather_data['weather'][0]['description']}"
        feels_like = f"Feels like: {weather_data['main']['feels_like']}"
        result = f"---{city.capitalize()}---\n{farengeit}\n{description}\n{feels_like}"
        return result
    except:
        return f"Maybe a mistake in a word. Try again"



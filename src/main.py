import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # For temperature in Celsius, use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(weather_data):
    if weather_data['cod'] != 200:
        print("City not found or there was an error fetching the data.")
        return
    
    city = weather_data['name']
    country = weather_data['sys']['country']
    weather = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp']
    temp_min = weather_data['main']['temp_min']
    temp_max = weather_data['main']['temp_max']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    
    print(f"Weather in {city}, {country}:")
    print(f"Description: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Min Temperature: {temp_min}°C")
    print(f"Max Temperature: {temp_max}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

def main():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()

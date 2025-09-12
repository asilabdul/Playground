import requests
import json


def fetch_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        raise Exception(f"Error fetching data: {data.get('message', 'Could not retrieve data')}")



API_KEY = "77f97ed5828ea11d3cfabf79bea9e1ba"
print("welcome to the weather app\nPlease enter your city name.")
city = input("City: ")
print(f"Fetching weather data for {city}...")
print(fetch_weather_data(city))

    
    
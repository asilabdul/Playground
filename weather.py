import requests
import json
from datetime import datetime, timedelta

def fetch_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        raise Exception(f"Error fetching data: {data.get('message', 'Could not retrieve data')}")

def weather_report(data):
    main = data['main']
    weathertype = data['weather'][0]['description'].capitalize()
    sunset_timestamp = data['sys']['sunset']
    sunset_time = datetime.utcfromtimestamp(sunset_timestamp) + timedelta(seconds=data['timezone'])
    report = (f"City: {data['name']}\n"
              f"Country: {data['sys']['country']}\n"
              f"Weather: {weathertype}\n"
              f"Temperature: {main['temp']}°C\n"
              f"Feels like: {main['feels_like']}°C\n"
              f"Max Temperature: {main['temp_max']}°C\n"
              f"Min Temperature: {main['temp_min']}°C\n"
              f"Humidity: {main['humidity']}%\n"
              f"Sunset Time: {sunset_time.strftime('%Y-%m-%d %H:%M:%S')}")
    return report

API_KEY = "apikeyhere"
print("welcome to the weather app\nPlease enter your city name.")
city = input("City: ")
print(f"Fetching weather data for {city}...")
print("Would you like the raw JSON data or a formatted weather report with only the necessary information?")
choice = input("Enter 'json' for JSON data or 'report' for formatted report: ").strip().lower()
if choice == 'json':
    print(fetch_weather_data(city))
elif choice == 'report':
    data = fetch_weather_data(city)
    print(weather_report(data))
else:
    print("Invalid choice. Please enter 'json' or 'report'.")

    
    

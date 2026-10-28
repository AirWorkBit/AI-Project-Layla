
from datetime import datetime
import requests

# 1. Get the current local system time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Current Local Time: {current_time}")

# 2. Get live weather data (Example: Kuala Lumpur)
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 3.1412,
    "longitude": 101.6865,
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": "auto",
}

api_time = "N/A"
temp = "N/A"
humidity = "N/A"

try:
    response = requests.get(url, params=params).json()
    # Extract weather values and their matching timestamps from the API response
    api_time = response["current"]["time"]
    temp = response["current"]["temperature_2m"]
    humidity = response["current"]["relative_humidity_2m"]
except Exception as e:
    print(f"Could not retrieve live weather data: {e}")

while True:
  user = input("Hi! How can I help you? ")
  user = user.lower()
  if "weather" in user:
    print(f"Weather Data Time : {api_time} | Temp: {temp}°C | Humidity: {humidity}%")
  elif "time" in user:
    print(f"Current Local Time: {current_time}")
  elif "bye" in user:
    print("see you again bro")
    break
  else:
    print("Sorry, I don't understand. Run again.")
    break
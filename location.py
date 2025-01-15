import geocoder, requests, math
import os
from PyQt5.QtGui import QPixmap

url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "f6e2978c6ae5300b5a90b4372a43296d"
params = {}

# Grabs current location based on ip address
def get_current_location():
    current_location = geocoder.ip("me")
    if current_location.latlng:
        latitude, longitude = current_location.latlng
        address = current_location.address
        return latitude, longitude, address
    else:
        return None

# Grabs location based on a virtual GPS
def get_coordinates_from_address(address):
    location = geocoder.osm(address)
    if location.latlng:
        return location.latlng
    else:
        return None

# Function get weather based on user location
def get_weather_by_location():
    loc = get_current_location()
    if loc:
        latitude, longitude, _ = loc
        # Prepare API request paramaters
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": api_key,
            "units": "metric"
        }
        # Call API
        response = requests.get(url, params=params)
        if response.status_code == 200:                     # 200 means request was successful
            weather_data = response.json()
            temp = weather_data["main"]["temp"]
            fahrenheit = math.ceil((temp * 9/5) + 32)      # Convert celcius to fahrenheit, ceil it
            description = weather_data["weather"][0]["description"]
            #main_weather = weather_data["weather"][0]["main"] # Not necessary to have
            city = weather_data["name"]
            return f"Weather in {city}: {description.capitalize()}, {fahrenheit}°F"     # Return weather summary

def display_weather():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script (don't know exactly how this works) - HA
    image_path = os.path.join(base_dir, "images", "clear_sky.png") 
    
    # Debug: Print the path to ensure it is correct
    print("Image path:", image_path)
    
    if os.path.exists(image_path):
        return QPixmap(image_path)
    else:
        print(f"Error: Image not found at {image_path}")
        return None


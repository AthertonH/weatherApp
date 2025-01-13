from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel
import location
import requests
import math

url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "f6e2978c6ae5300b5a90b4372a43296d"

# Function get weather based on user location
def get_weather_by_location():
    loc = location.get_current_location()
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
            city = weather_data["name"]
            return f"Weather in {city}: {description.capitalize()}, {fahrenheit}°F"     # Return weather summary

# PyQt5 Application
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Weather App")
main_window.resize(960, 540)  # 16:9 Ratio

# Widgets
weather_label = QLabel("Click 'Check Weather' to get the current weather!")
check_weather_button = QPushButton("Check Weather")

# Button Action
def fetch_and_display_weather():
    weather_info = get_weather_by_location()
    weather_label.setText(weather_info)

check_weather_button.clicked.connect(fetch_and_display_weather)

# Layouts
grid = QGridLayout()
grid.addWidget(weather_label, 0, 0, 1, 2)  # Spanning 1 row, 2 columns

# Center the button with QHBoxLayout
button_layout = QHBoxLayout()
button_layout.addStretch()  # Add space before the button
button_layout.addWidget(check_weather_button)  # Add the button
button_layout.addStretch()  # Add space after the button

grid.addLayout(button_layout, 1, 0, 1, 2)  # Add the button layout centered across 2 columns

master_layout = QVBoxLayout()
master_layout.addLayout(grid)

main_window.setLayout(master_layout)

# Show/Run
main_window.show()
app.exec_()

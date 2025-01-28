from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QCalendarWidget,
)
from PyQt5.QtGui import QPixmap
import location

# PyQt5 Application
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Weather and Calendar App")
main_window.resize(960, 540)  # 16:9 Ratio

# Widgets
# Weather widgets
weather_label = QLabel("Click 'Check Weather' to get the current weather!")
weather_image_label = QLabel()  # QLabel to display the weather image
check_weather_button = QPushButton("Check Weather")

# Calendar widgets
calendar_button = QPushButton("Calendar")
calendar_widget = QCalendarWidget()  # Create QCalendarWidget
calendar_widget.hide()  # Initially hide the calendar widget


# Button action for calendar
def open_calendar():
    print("Opening calendar...")
    calendar_widget.show()  # Show the calendar widget when button is clicked


# Button Action for fetching and displaying weather
def fetch_and_display_weather():
    print("Fetching weather...")
    # Fetch weather info and image
    weather_info = location.get_weather_by_location()
    weather_image = location.display_weather()

    # Update text label
    weather_label.setText(weather_info if weather_info else "Weather data unavailable.")

    # Update image label
    if weather_image and not weather_image.isNull():
        weather_image_label.setPixmap(weather_image)
        weather_image_label.setScaledContents(True)  # Ensure scaling
    else:
        weather_image_label.setText("No image available.")  # Fallback text
        print("Error: Failed to load weather image.")


# When check weather button is clicked, display image
check_weather_button.clicked.connect(fetch_and_display_weather)

# When calendar button is clicked, open calendar
calendar_button.clicked.connect(open_calendar)

# Layouts
grid = QGridLayout()
grid.addWidget(weather_label, 0, 0, 1, 2)  # Spanning 1 row, 2 columns
grid.addWidget(weather_image_label, 1, 0, 1, 2)
grid.addWidget(calendar_widget, 2, 0, 1, 2)  # Add the calendar widget to the layout

# Center the button with QHBoxLayout
button_layout = QHBoxLayout()
button_layout.addStretch()  # Add space before the button
button_layout.addWidget(check_weather_button)  # Add weather button
button_layout.addWidget(calendar_button)  # Add calendar button
button_layout.addStretch()  # Add space after the button


grid.addLayout(
    button_layout, 1, 0, 1, 2
)  # Add the button layout centered across 2 columns

master_layout = QVBoxLayout()
master_layout.addLayout(grid)

main_window.setLayout(master_layout)

# Show/Run
main_window.show()
app.exec_()

Weather App

This is a Flask-based weather application that allows users to search for current weather conditions and a 5-day weather forecast by entering a city name or by using their current location. The app also provides the ability to toggle between Fahrenheit and Celsius for temperature units.
_____________________
Features

Search by City: Enter a city name to get the current weather and 5-day forecast.

Location-Based Weather: Get the weather information for your current location using the Geolocation API.

Temperature Units: Toggle between Celsius and Fahrenheit.

5-Day Forecast: The forecast is grouped by day, with weather data for different times of the day.
_____________________
Technologies Used

Flask: A lightweight web framework for Python used to create the backend.

HTML/CSS: For structuring and styling the web pages.

JavaScript: Used for accessing the Geolocation API and sending requests to the Flask backend.

OpenWeatherMap API: Provides the weather data for the application.
_____________________
Prerequisites

To run this application, you need to have the following installed on your system:

Python 3.6+
pip (Python package installer)
_____________________
Installation and Setup

Clone the Repository

git clone https://github.com/yourusername/weather-app.git
cd weather-app
Install Dependencies

Install the required Python packages using pip:

bash
Copy code
pip install Flask requests
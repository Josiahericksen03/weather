from flask import Flask, request, render_template
import requests
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)

API_KEY = '70371699840c4120cc43d3f7e5607162'

def group_forecast_by_day(forecast_list):
    grouped_forecast = defaultdict(list)
    for forecast in forecast_list:
        date = datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        grouped_forecast[date].append(forecast)
    return grouped_forecast

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    units = request.form.get('units', 'metric')  # default to Celsius
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}'
    forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={units}'

    weather_response = requests.get(weather_url)
    forecast_response = requests.get(forecast_url)

    if weather_response.status_code == 200 and forecast_response.status_code == 200:
        weather_data = weather_response.json()
        forecast_data = forecast_response.json()
        grouped_forecast = group_forecast_by_day(forecast_data['list'])
        return render_template('weather.html', weather=weather_data, forecast=grouped_forecast, units=units)
    else:
        return render_template('index.html', error="City not found. Please try again.")

@app.route('/weather/location')
def get_weather_by_location():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    units = request.args.get('units', 'metric')

    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units={units}'
    forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units={units}'

    weather_response = requests.get(weather_url)
    forecast_response = requests.get(forecast_url)

    if weather_response.status_code == 200 and forecast_response.status_code == 200:
        weather_data = weather_response.json()
        forecast_data = forecast_response.json()
        grouped_forecast = group_forecast_by_day(forecast_data['list'])
        return render_template('weather.html', weather=weather_data, forecast=grouped_forecast, units=units)
    else:
        return render_template('index.html', error="Location not found. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, session, jsonify
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')

API_KEY = os.environ.get('OPENWEATHER_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5'

def fetch_weather_data(city):
    """Fetch current weather data for a city"""
    try:
        response = requests.get(f'{BASE_URL}/weather', params={
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f'Failed to fetch weather data: {str(e)}')

def fetch_forecast_data(city):
    """Fetch 5-day weather forecast for a city"""
    try:
        response = requests.get(f'{BASE_URL}/forecast', params={
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f'Failed to fetch forecast data: {str(e)}')

def convert_temp(temp, unit):
    """Convert temperature between Celsius and Fahrenheit"""
    if unit == 'fahrenheit':
        return round((temp * 9/5) + 32)
    return round(temp)

def get_day_name(date_str):
    """Get day name from date string"""
    from datetime import datetime
    date = datetime.strptime(date_str, '%Y-%m-%d')
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    return days[date.weekday()]

def format_time(timestamp):
    """Format timestamp to readable time"""
    date = datetime.fromtimestamp(timestamp)
    return date.strftime('%I:%M %p')

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None
    error = None
    temp_unit = session.get('temp_unit', 'celsius')
    last_city = session.get('last_city', 'London')

    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        if city:
            try:
                weather_data = fetch_weather_data(city)
                forecast_data = fetch_forecast_data(city)
                session['last_city'] = city
                last_city = city
            except Exception as e:
                error = str(e)
        else:
            error = 'Please enter a city name'

    # Load default data if no POST request
    if not weather_data and not error:
        try:
            weather_data = fetch_weather_data(last_city)
            forecast_data = fetch_forecast_data(last_city)
        except Exception as e:
            error = str(e)

    return render_template('index.html',
                         weather_data=weather_data,
                         forecast_data=forecast_data,
                         error=error,
                         temp_unit=temp_unit,
                         last_city=last_city,
                         convert_temp=convert_temp,
                         get_day_name=get_day_name,
                         format_time=format_time)

@app.route('/toggle_unit', methods=['POST'])
def toggle_unit():
    current_unit = session.get('temp_unit', 'celsius')
    new_unit = 'fahrenheit' if current_unit == 'celsius' else 'celsius'
    session['temp_unit'] = new_unit
    return jsonify({'unit': new_unit})

@app.route('/search', methods=['POST'])
def search():
    city = request.json.get('city', '').strip()
    if not city:
        return jsonify({'error': 'Please enter a city name'}), 400

    try:
        weather_data = fetch_weather_data(city)
        forecast_data = fetch_forecast_data(city)
        session['last_city'] = city
        return jsonify({
            'weather': weather_data,
            'forecast': forecast_data,
            'city': city
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

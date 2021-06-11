from flask import Flask, request, render_template
import os
import json
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv

app = Flask(__name__)
# Define API KEY AND URL HERE
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def homepage():
    """Displays results for current weather conditions."""
    city = request.args.get('city')
    mood = request.args.get('mood')
    units = request.args.get('units')
    params = {

        'appid': API_KEY,
        'q': city,
        'units': units

    }
    result_json = requests.get(API_URL, params=params).json()

    def get_letter_for_units(units):
        """Returns a shorthand letter for the given units."""
        return 'F' if units == 'imperial' else 'C' if units == 'metric' else 'K'
    context = {
        'date': datetime.now(),
        'city': city,
        'mood': mood,
        'description': result_json['weather'][0]['description'],
        'temp': result_json['main']['temp'],
        'humidity': result_json['main']['humidity'],
        'wind_speed': result_json['wind']['speed'],
        'units_letter': get_letter_for_units(units)
    }

    return render_template('home.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)

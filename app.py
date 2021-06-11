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
    units = request.args.get('units')
    params = {

        'appid': API_KEY,
        'q': city,
        'units': units

    }

    return render_template('home.html')

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)

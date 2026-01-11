import os
from flask import Flask, render_template

app = Flask(__name__)

# Safely retrieves your API key from Render's environment settings
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather')
def weather():
    # Passes the API key to the weather page for live data fetching
    return render_template('weather.html', api_key=WEATHER_API_KEY)


@app.route('/maritime')
def maritime():
    return render_template('maritime.html')


@app.route('/solar')
def solar():
    return render_template('solar.html')


if __name__ == '__main__':
    # Standard start for local testing; Render uses Gunicorn to run this
    app.run()

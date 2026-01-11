import os
from flask import Flask, render_template

app = Flask(__name__)

# This pulls the key safely from Render's environment
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')


@app.route('/')
def index():
    return render_template('index.html')

# Add your weather route here


@app.route('/weather')
def weather():
    # You can now use WEATHER_API_KEY in your API call logic
    return render_template('weather.html', api_key=WEATHER_API_KEY)

# Ensure routes exist for your other pages to avoid 404 errors


@app.route('/solar')
def solar():
    return render_template('solar.html')


@app.route('/maritime')
def maritime():
    return render_template('maritime.html')


if __name__ == "__main__":
    app.run()

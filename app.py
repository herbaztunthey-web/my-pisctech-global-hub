import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Replace with your actual key from your weather app info
API_KEY = 'aad4cbdae56d6d693c4f99064fe46dcd'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather')
def weather_page():
    return render_template('weather.html')


@app.route('/maritime')
def maritime_page():
    return render_template('maritime.html')


@app.route('/solar')
def solar_page():
    return render_template('solar.html')


@app.route('/get_weather')
def get_weather():
    city = request.args.get('city')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import requests  # The library we just added to requirements.txt

app = Flask(__name__)

# Use the API key you mentioned having for your weather app
API_KEY = 'aad4cbdae56d6d693c4f99064fe46dcd'


@app.route('/')
def index():
    # Make sure your file is named index.html in the templates folder
    return render_template('index.html')


@app.route('/weather')
def weather():
    return render_template('weather.html')


@app.route('/maritime')
def maritime():
    return render_template('maritime.html')


@app.route('/solar')
def solar():
    return render_template('solar.html')


@app.route('/get_weather')
def get_weather_data():
    city = request.args.get('city')
    # This talks to the OpenWeather API using the 'requests' module
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True)

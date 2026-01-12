import os
from flask import Flask, render_template

# Added static_url_path to ensure images load correctly on Render
app = Flask(__name__, static_url_path='/static')

WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather')
def weather():
    return render_template('weather.html', api_key=WEATHER_API_KEY)


@app.route('/maritime')
def maritime():
    return render_template('maritime.html')


@app.route('/solar')
def solar():
    return render_template('solar.html')


if __name__ == '__main__':
    app.run()

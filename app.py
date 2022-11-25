from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    # show the actual city name on the dashboard
    def __str__(self):
        return self.name


@app.route('/', methods=['GET', 'POST'])
def index():
    YOUR_API_KEY = os.getenv('API_KEY')
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}"

    cities = City.query.all()

    # submit city from form to database
    if request.method == 'POST':
        cityname = request.form["cityname"]
        new_city = City(name=cityname)
        db.session.add(new_city)
        db.session.commit()

    weather_data = []
    for city in cities:
        # request the API data and convert the JSON to Python data types
        city_weather = requests.get(url.format(city, YOUR_API_KEY)).json()

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        # add the data for the current city into our list
        weather_data.append(weather)

    return render_template('index.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)

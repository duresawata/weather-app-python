# Weather-App-Python

## _Using Python Flask_

weather-app-python is a simple web-based weather data retrival app for a given cities.

## Features

- show current temperature (F) and weather decription for givien cities
- can add cities

## Tech

Here are tech and dev stacks i have used for this project:

- Dev Language [Python]
- Frameworks [Flask] - micro web framework written in Python
- Database [SQLAlchemy] - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- Styling [bulma css](https://bulma.io/) - Bulma is a free, open source CSS framework based on Flexbox and built with Sass. It's 100% responsive, fully modular, and available for free.
- API [openweathermap](https://home.openweathermap.org/) - OpenWeatherMap is an online service, owned by OpenWeather Ltd, that provides global weather data via API, including current weather data, forecasts, nowcasts and historical weather data for any geographical location.

## Installation

first you need to have python version 3.x installed on your system.
after that colon this repository and install required packages using pip command.

Open your favorite Terminal and run these commands.

```sh
git clone https://github.com/duresawata/weather-app-python
cd weather-app-python
pip install -r requirements.txt
```

### Prepare Api

go to https://openweathermap.org/ singin and get `API_KEY`. then in the project folder open `.env` file, in the empty quote paste your api_key and save it.

After installed all the required packages and prepared the api, start the server using:

```sh
python app.py
```

(or) if you are using unix:

```sh
python3 app.py
```

> Note: you must be in a folder where `app.py`

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:5000
```

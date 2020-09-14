import os
import requests
import pandas as pd
from dotenv import load_dotenv

class Restaurant():
    def __init__(self, name, city, region, latitude, longitude, cuisine, price, stars):
        self.name = name
        self.city = city
        self.region = region
        self.latitude = latitude
        self.longitude = longitude
        self.cuisine = cuisine
        self.price = price
        self.stars = stars

        self.key = self.get_api_key()
        self.url = self.get_api_url()
        self.weather_report = self.get_api_json()
        self.weather_now = self.get_weather_report_now()

    def __str__(self):
        return f"""
El restaurante {self.name}, de {self.stars} estrella{"s" if self.stars > 1 else ""}, está en la ciudad de {self.city} ({self.region}). Sirve comida de tipo {self.cuisine}.

El precio es de {self.price}.

La previsión meteorológica para la próxima hora es:
- Temperatura: {self.weather_now['temp']}.
- Sensación térmica: {self.weather_now['feels_like']}.
- Tiempo: {self.weather_now['main']}.
- Previsión de lluvia: {self.weather_now['rain_1h']}.

        """

    def get_api_key(self):
        load_dotenv()
        return os.getenv("OPENWEATHERMAP_APIKEY")

    def get_api_url(self, units="metric"):
        '''
        receives: an optional argument with the units of temperature.
                    - "metric": Celsius.
                    - "imperial": Fahrenheit.
                    - by default it is Kelvin 
        return: the formated api url.
        '''
        return f'http://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&units={units}&APPID={self.key}'

    def get_api_json(self):
        response = requests.get(self.url)
        return response.json()

    def get_weather_report_now(self):
        result = {'temp': self.weather_report['current']['temp'],
                'feels_like': self.weather_report['current']['feels_like'],
                'main': self.weather_report['current']['weather'][0]['main']
                 }
        try:
            if self.weather_report['current']['rain']:
                result['rain_1h'] = self.weather_report['current']['rain']['1h']
        except KeyError:
            result['rain_1h'] = "No hay información sobre previsión de lluvia en la próxima hora."

        return result
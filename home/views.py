from django.shortcuts import render
import requests
from pprint import pprint
import os


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = os.environ.get("OPEN_WEATHER_API_KEY")
        url = "http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city
        response = requests.get(url).json()
        city_name = response['name']
        city_humidity = response['main']['humidity']
        city_pressure = response['main']['pressure']
        city_temp = response['main']['temp']
        weather_description = response['weather'][0]['description']
        data = {
            'city_name': city_name,
            'city_temp': str(city_temp) + "K",
            'city_humidity': str(city_humidity) + '%',
            'city_pressure': str(city_pressure) + "Pa",
            'weather_description': weather_description,
        }
        print(response)
    else:
        data = {}
    return render(request, 'home/index.html', {'data': data})

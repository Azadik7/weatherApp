import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    appid = '1b86ef28ee3be7f3ab99d62c30651ba5'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        print(res)
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)


    context = {'all_info': all_cities, 'form': form}

    return  render(request, 'weather/index.html', context)
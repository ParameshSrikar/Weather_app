import os
import time
from django.shortcuts import render
from .forms import CityForm
import requests
from decouple import config

API_KEY = config('OPENWEATHER_API_KEY')

# Define the cache folder
CACHE_DIR = 'weather_cache'

# Ensure cache folder exists
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def get_weather_data(lat, lon):
    """Fetch weather data from OpenWeatherMap API."""
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

def get_geocode(city):
    try:
        # Make API call to get geocode
        response = requests.get(f'http://api.example.com/geocode?city={city}')
        data = response.json()

        if len(data) > 0:
            return data[0]  # Extract first result
        else:
            # Handle case when no data is returned
            return None
    except (IndexError, KeyError, requests.exceptions.RequestException) as e:
        # Log the error or handle it as needed
        print(f"Error fetching geocode for {city}: {e}")
        return None


def index(request):
    form = CityForm()
    weather_data = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            # Define the cache file path within the cache folder
            cache_file = os.path.join(CACHE_DIR, f'{city}.txt')

            # Check if cache file exists and if it's younger than 180 minutes
            if os.path.exists(cache_file) and time.time() - os.path.getmtime(cache_file) < 10800:
                with open(cache_file, 'r') as file:
                    weather_data = eval(file.read())  # Use eval to convert string back to dict
            else:
                # Get city coordinates and weather data
                location = get_geocode(city)
                lat, lon = location['lat'], location['lon']
                weather_data = get_weather_data(lat, lon)

                # Cache the data in a file inside the cache folder
                with open(cache_file, 'w') as file:
                    file.write(str(weather_data))

    return render(request, 'weather/index.html', {'form': form, 'weather_data': weather_data})

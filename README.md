Weather App 🌦️

This is a weather application built using Django, which integrates with the OpenWeather API to retrieve and display current weather data for any city. The app allows users to search for weather conditions by city name, caches the data to improve performance, and stores user searches in a PostgreSQL database.

Features
-------------
> Search for current weather by city name.
> Displays temperature, humidity, weather description, and more.
> Caches weather data to reduce API calls.
> Interactive UI using jQuery and AJAX for real-time updates.
> Data persistence using PostgreSQL.
> Simple and user-friendly interface.

Prerequisites
-----------------
Before running the application, ensure that you have the following installed:
Python 3.8+
Django 3.2+
PostgreSQL
Virtualenv (optional but recommended)

Setup
-------
1. Clone the repository
                    git clone https://github.com/ParameshSrikar/weather_app
                    cd django-weather-app
2. Create a virtual environment and activate it
                 python -m venv venv
                 source venv/bin/activate  # On Windows, use: venv\Scripts\activate
3. Install the required dependencies
pip install -r requirements.txt

5. Set up PostgreSQL
Create a PostgreSQL database and configure the connection in the settings.py file:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
4. Obtain API Key from OpenWeather
Create a free account on the OpenWeather API website, and obtain your API key. Add the key to your environment variables or directly in the Django settings file:

OPENWEATHER_API_KEY = 'your_api_key'
You can also use Django’s environment variable support by setting up a .env file with django-environ.

5. Run migrations
Apply the migrations to set up the database schema:

python manage.py migrate

6. Run the application
Start the Django development server:

python manage.py runserver

The application should now be running at http://127.0.0.1:8000/.

Usage
Open the application in your browser.
Enter a city name in the search bar.
The weather information for the entered city will be retrieved and displayed.
Previous searches will be cached for faster access.











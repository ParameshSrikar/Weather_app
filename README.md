# weather_app

Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/weather-app.git
cd weather-app
2. Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Set Up the Database
Ensure PostgreSQL is installed and create a database named weather_db.

bash
Copy code
psql -U postgres
CREATE DATABASE weather_db;
5. Migrate Database
bash
Copy code
python manage.py migrate
6. Get API Key for OpenWeather API
Sign up for an API key at OpenWeather.

7. Add API Key to Environment Variables
Create a .env file in the root directory and add your OpenWeather API key:

bash
Copy code
API_KEY=your_openweather_api_key
8. Run the Application
bash
Copy code
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/ to see the app in action!

🧑‍💻 Code Structure
bash
Copy code
weather_app/
│
├── weather/                     # Main app folder
│   ├── migrations/              # Database migrations
│   ├── static/                  # Static files (CSS, JS, Images)
│   ├── templates/               # HTML templates
│   ├── __init__.py              # App initialization
│   ├── admin.py                 # Admin panel configuration
│   ├── apps.py                  # App configuration
│   ├── models.py                # Database models
│   ├── urls.py                  # URL routing
│   ├── views.py                 # Main application logic
│   └── tests.py                 # Test cases
│
├── weather_app/                 # Project folder
│   ├── __init__.py              # Project initialization
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Project-wide URL configuration
│   └── wsgi.py                  # WSGI configuration for deployment
│
├── manage.py                    # Command-line utility
└── requirements.txt             # Project dependencies

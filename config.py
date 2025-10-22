import os
from dotenv import load_dotenv

load_dotenv()

# API Keys (you'll need to get these from weather service providers)
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
WEATHERAPI_KEY = os.getenv('WEATHERAPI_KEY')

# Weather criteria
IDEAL_TEMP_MIN = 20  # °C
IDEAL_TEMP_MAX = 28  # °C
MAX_WIND_SPEED = 20  # km/h
MAX_RAIN_PROBABILITY = 20  # %

# Location settings
MAX_DISTANCE = 100  # km - maximum distance to search for locations
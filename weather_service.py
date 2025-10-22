import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from typing import Dict, List, Tuple
from config import OPENWEATHER_API_KEY, WEATHERAPI_KEY

class WeatherService:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="donde_voy_app")

    def get_coordinates(self, location: str) -> Tuple[float, float]:
        """Get coordinates for a given location."""
        location_data = self.geolocator.geocode(location)
        if location_data:
            return (location_data.latitude, location_data.longitude)
        raise ValueError(f"No se pudo encontrar la ubicación: {location}")

    def get_nearby_cities(self, lat: float, lon: float, radius_km: int = 100) -> List[Dict]:
        """Get a list of nearby cities within the specified radius."""
        # Using OpenWeatherMap's API to find nearby cities
        url = f"http://api.openweathermap.org/data/2.5/find?lat={lat}&lon={lon}&cnt=15&appid={OPENWEATHER_API_KEY}"
        response = requests.get(url)
        data = response.json()
        
        nearby_cities = []
        for city in data.get('list', []):
            city_coords = (city['coord']['lat'], city['coord']['lon'])
            current_coords = (lat, lon)
            distance = geodesic(current_coords, city_coords).km
            
            if distance <= radius_km:
                nearby_cities.append({
                    'name': city['name'],
                    'lat': city['coord']['lat'],
                    'lon': city['coord']['lon'],
                    'distance': round(distance, 2)
                })
        
        return nearby_cities

    def get_weather_data(self, lat: float, lon: float) -> Dict:
        """Get weather data from multiple sources and combine them."""
        # OpenWeatherMap data
        weather_data = self._get_openweather_data(lat, lon)
        # WeatherAPI.com data
        weather_api_data = self._get_weatherapi_data(lat, lon)
        
        # Combine and average the data
        return self._combine_weather_data(weather_data, weather_api_data)

    def _get_openweather_data(self, lat: float, lon: float) -> Dict:
        """Get weather data from OpenWeatherMap."""
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={OPENWEATHER_API_KEY}"
        response = requests.get(url)
        data = response.json()
        
        return {
            'temperature': data['main']['temp'],
            'wind_speed': data['wind']['speed'] * 3.6,  # Convert m/s to km/h
            'rain_probability': data.get('rain', {}).get('1h', 0) * 100,
            'description': data['weather'][0]['description']
        }

    def _get_weatherapi_data(self, lat: float, lon: float) -> Dict:
        """Get weather data from WeatherAPI.com."""
        url = f"http://api.weatherapi.com/v1/current.json?key={WEATHERAPI_KEY}&q={lat},{lon}"
        response = requests.get(url)
        data = response.json()
        
        return {
            'temperature': data['current']['temp_c'],
            'wind_speed': data['current']['wind_kph'],
            'rain_probability': data['current']['precip_mm'] * 100,
            'description': data['current']['condition']['text']
        }

    def _combine_weather_data(self, data1: Dict, data2: Dict) -> Dict:
        """Combine and average weather data from multiple sources."""
        return {
            'temperature': round((data1['temperature'] + data2['temperature']) / 2, 1),
            'wind_speed': round((data1['wind_speed'] + data2['wind_speed']) / 2, 1),
            'rain_probability': round((data1['rain_probability'] + data2['rain_probability']) / 2, 1),
            'descriptions': [data1['description'], data2['description']]
        }
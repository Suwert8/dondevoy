from weather_service import WeatherService
from config import (
    IDEAL_TEMP_MIN, 
    IDEAL_TEMP_MAX, 
    MAX_WIND_SPEED, 
    MAX_RAIN_PROBABILITY,
    MAX_DISTANCE
)

def calculate_weather_score(weather_data):
    """Calculate a score for weather conditions (0-100)."""
    score = 100
    
    # Temperature score (0-40 points)
    temp = weather_data['temperature']
    if temp < IDEAL_TEMP_MIN:
        score -= (IDEAL_TEMP_MIN - temp) * 4
    elif temp > IDEAL_TEMP_MAX:
        score -= (temp - IDEAL_TEMP_MAX) * 4
    
    # Wind score (0-30 points)
    wind_penalty = (weather_data['wind_speed'] / MAX_WIND_SPEED) * 30
    score -= wind_penalty
    
    # Rain probability score (0-30 points)
    rain_penalty = (weather_data['rain_probability'] / MAX_RAIN_PROBABILITY) * 30
    score -= rain_penalty
    
    return max(0, round(score, 1))

def main():
    weather_service = WeatherService()
    
    # Get user's location
    try:
        location = input("Ingresa tu ubicación (ciudad, país): ")
        lat, lon = weather_service.get_coordinates(location)
        print(f"\nBuscando lugares con buen tiempo cerca de {location}...")
        
        # Get nearby cities
        nearby_cities = weather_service.get_nearby_cities(lat, lon, MAX_DISTANCE)
        
        # Get weather data and calculate scores for each city
        weather_results = []
        for city in nearby_cities:
            weather_data = weather_service.get_weather_data(city['lat'], city['lon'])
            score = calculate_weather_score(weather_data)
            
            weather_results.append({
                'city': city['name'],
                'distance': city['distance'],
                'weather': weather_data,
                'score': score
            })
        
        # Sort results by score
        weather_results.sort(key=lambda x: x['score'], reverse=True)
        
        # Print results
        print("\nMejores lugares para ir hoy:")
        print("-" * 60)
        
        for result in weather_results[:5]:  # Show top 5 results
            print(f"\n{result['city']} (a {result['distance']} km)")
            print(f"Puntuación del clima: {result['score']}/100")
            print(f"Temperatura: {result['weather']['temperature']}°C")
            print(f"Viento: {result['weather']['wind_speed']} km/h")
            print(f"Probabilidad de lluvia: {result['weather']['rain_probability']}%")
            print(f"Condiciones: {' / '.join(result['weather']['descriptions'])}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
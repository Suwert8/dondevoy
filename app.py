from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from weather_service import WeatherService
from config import (
    IDEAL_TEMP_MIN, 
    IDEAL_TEMP_MAX, 
    MAX_WIND_SPEED, 
    MAX_RAIN_PROBABILITY,
    MAX_DISTANCE
)

app = Flask(__name__)
CORS(app)
weather_service = WeatherService()

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        location = data.get('location')
        
        # Get coordinates
        lat, lon = weather_service.get_coordinates(location)
        
        # Get nearby cities
        nearby_cities = weather_service.get_nearby_cities(lat, lon, MAX_DISTANCE)
        
        # Get weather data and calculate scores
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
        
        return jsonify({
            'success': True,
            'results': weather_results[:5]  # Return top 5 results
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
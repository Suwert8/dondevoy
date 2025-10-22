function searchWeather() {
    const location = document.getElementById('location').value;
    if (!location) {
        showError('Por favor, ingresa una ubicación');
        return;
    }

    // Show loading
    document.getElementById('loading').style.display = 'block';
    document.getElementById('error').style.display = 'none';
    document.getElementById('results').innerHTML = '';

    // Make API request
    fetch('/api/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ location })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loading').style.display = 'none';
        
        if (!data.success) {
            showError(data.error);
            return;
        }

        displayResults(data.results);
    })
    .catch(error => {
        document.getElementById('loading').style.display = 'none';
        showError('Error al buscar. Por favor, intenta de nuevo.');
        console.error('Error:', error);
    });
}

function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    results.forEach(result => {
        const card = document.createElement('div');
        card.className = 'location-card';

        card.innerHTML = `
            <h2>
                ${result.city}
                <span class="score">${result.score}/100</span>
            </h2>
            <div>A ${result.distance} km de distancia</div>
            <div class="weather-info">
                <div class="weather-stat">
                    <div>Temperatura</div>
                    <span>${result.weather.temperature}°C</span>
                </div>
                <div class="weather-stat">
                    <div>Viento</div>
                    <span>${result.weather.wind_speed} km/h</span>
                </div>
                <div class="weather-stat">
                    <div>Lluvia</div>
                    <span>${result.weather.rain_probability}%</span>
                </div>
            </div>
            <div style="margin-top: 10px;">
                ${result.weather.descriptions.join(' / ')}
            </div>
        `;

        resultsDiv.appendChild(card);
    });
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
}

// Enable search on Enter key
document.getElementById('location').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchWeather();
    }
});
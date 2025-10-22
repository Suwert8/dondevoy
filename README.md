# DondeVoy - Buscador de Buen Tiempo

Esta aplicación te ayuda a encontrar lugares cercanos con el mejor clima para visitar. Compara diferentes fuentes de información meteorológica y te sugiere los mejores destinos basándose en temperatura, viento y probabilidad de lluvia.

## Requisitos

- Python 3.7 o superior
- Conexión a internet
- Claves API de servicios meteorológicos

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Crea un archivo `.env` en la raíz del proyecto con tus claves API:
```
OPENWEATHER_API_KEY=tu_clave_aqui
WEATHERAPI_KEY=tu_clave_aqui
```

Puedes obtener las claves API en:
- OpenWeatherMap: https://openweathermap.org/api
- WeatherAPI.com: https://www.weatherapi.com/

## Uso

Ejecuta el programa con:
```bash
python main.py
```

Introduce tu ubicación cuando se te solicite y la aplicación encontrará los mejores lugares cercanos para visitar basándose en las condiciones climáticas.

## Configuración

Puedes ajustar los criterios de búsqueda en el archivo `config.py`:

- `IDEAL_TEMP_MIN`: Temperatura mínima ideal (°C)
- `IDEAL_TEMP_MAX`: Temperatura máxima ideal (°C)
- `MAX_WIND_SPEED`: Velocidad máxima del viento (km/h)
- `MAX_RAIN_PROBABILITY`: Probabilidad máxima de lluvia (%)
- `MAX_DISTANCE`: Distancia máxima de búsqueda (km)

## Interfaz web

⚠️ **IMPORTANTE**: No abras el archivo `index.html` directamente desde el sistema de archivos (file://) - esto causará errores de CORS con las APIs externas.

### Cómo ejecutar la aplicación web

**Opción recomendada - Servidor Python:**

```bash
python server.py
```

Luego abre tu navegador en: http://localhost:8000

**Otras opciones:**

Con Node.js:
```bash
npx http-server -p 8000
```

Con PHP:
```bash
php -S localhost:8000
```

### Configuración web

1. Haz clic en el botón de configuración (⚙️) en la esquina superior derecha
2. Ingresa tu OpenWeather API Key
3. Ajusta los parámetros según tus preferencias:
   - Distancia máxima de búsqueda
   - Temperatura ideal (mínima y máxima)
   - Viento máximo aceptable
   - Cantidad de puntos de muestreo
   - Concurrencia para las peticiones
4. Haz clic en "Guardar"

### Características de la interfaz web

- 🌤️ Búsqueda de lugares con buen tiempo
- 📍 Geolocalización automática
- 🗺️ Mapa interactivo con puntos de clima sincronizados con la lista
- 📊 Puntuación de clima basada en temperatura, viento y lluvia
- 🔍 Filtros y ordenación de resultados
- 📄 Paginación de resultados (10 por página)
- ⚙️ Panel de configuración personalizable
- 🎯 Sincronización bidireccional entre mapa y tarjetas de resultados
import folium
import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%t+%C+%h"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return f"{city}: Weather unavailable"
    except Exception as e:
        return f"{city}: Error"

# Cities with coordinates
cities = {
    "Delhi": [28.6139, 77.2090],
    "Mumbai": [19.0760, 72.8777],
    "Chennai": [13.0827, 80.2707],
    "Bangalore": [12.9716, 77.5946],
    "Hyderabad": [17.3850, 78.4867],
    "Lucknow": [26.8467, 80.9462]

}

# Create the base map
weather_map = folium.Map(location=[20.5937, 78.9629], zoom_start=6)
folium.TileLayer(
    tiles='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
    attr='&copy; <a href="https://carto.com/">CARTO</a>',
    name='CartoDB Positron (EN)',
    control=False
).add_to(weather_map)


# Add real-time weather info
for city, coords in cities.items():
    weather = get_weather(city)
    folium.Marker(
        location=coords,
        popup=weather,
        icon=folium.Icon(color="blue", icon="cloud")
    ).add_to(weather_map)

# Saving and open
weather_map.save("weather_map_realtime_no_api.html")
print(" Real-time map saved as 'weather_map_realtime_no_api.html'")

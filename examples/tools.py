from livekit.agents import function_tool


@function_tool
async def get_weather(city: str) -> dict:
    """
    Get weather data for a city in Saudi Arabia.
    
    Args:
        city: Name of the city in Saudi Arabia (Arabic or English)

    Returns:
        Dictionary containing weather information
    """
    # Weather data for Saudi cities
    weather_data = {
        "riyadh": {
            "city": "الرياض (Riyadh)",
            "temperature": 28,
            "condition": "مشمس (Sunny)",
            "humidity": 25,
            "wind_speed": 12,
        },
        "الرياض": {
            "city": "الرياض (Riyadh)",
            "temperature": 28,
            "condition": "مشمس (Sunny)",
            "humidity": 25,
            "wind_speed": 12,
        },
        "jeddah": {
            "city": "جدة (Jeddah)",
            "temperature": 32,
            "condition": "حار ورطب (Hot & Humid)",
            "humidity": 65,
            "wind_speed": 15,
        },
        "جدة": {
            "city": "جدة (Jeddah)",
            "temperature": 32,
            "condition": "حار ورطب (Hot & Humid)",
            "humidity": 65,
            "wind_speed": 15,
        },
        "dammam": {
            "city": "الدمام (Dammam)",
            "temperature": 30,
            "condition": "غيوم خفيفة (Partly Cloudy)",
            "humidity": 55,
            "wind_speed": 18,
        },
        "الدمام": {
            "city": "الدمام (Dammam)",
            "temperature": 30,
            "condition": "غيوم خفيفة (Partly Cloudy)",
            "humidity": 55,
            "wind_speed": 18,
        },
        "mecca": {
            "city": "مكة المكرمة (Mecca)",
            "temperature": 35,
            "condition": "حار جداً (Very Hot)",
            "humidity": 30,
            "wind_speed": 10,
        },
        "مكة": {
            "city": "مكة المكرمة (Mecca)",
            "temperature": 35,
            "condition": "حار جداً (Very Hot)",
            "humidity": 30,
            "wind_speed": 10,
        },
        "medina": {
            "city": "المدينة المنورة (Medina)",
            "temperature": 33,
            "condition": "مشمس (Sunny)",
            "humidity": 20,
            "wind_speed": 14,
        },
        "المدينة": {
            "city": "المدينة المنورة (Medina)",
            "temperature": 33,
            "condition": "مشمس (Sunny)",
            "humidity": 20,
            "wind_speed": 14,
        },
        "abha": {
            "city": "أبها (Abha)",
            "temperature": 22,
            "condition": "معتدل (Mild)",
            "humidity": 45,
            "wind_speed": 8,
        },
        "أبها": {
            "city": "أبها (Abha)",
            "temperature": 22,
            "condition": "معتدل (Mild)",
            "humidity": 45,
            "wind_speed": 8,
        },
        "tabuk": {
            "city": "تبوك (Tabuk)",
            "temperature": 26,
            "condition": "صافي (Clear)",
            "humidity": 15,
            "wind_speed": 16,
        },
        "تبوك": {
            "city": "تبوك (Tabuk)",
            "temperature": 26,
            "condition": "صافي (Clear)",
            "humidity": 15,
            "wind_speed": 16,
        },
    }

    # Normalize city name
    city_normalized = city.lower().strip()

    # Return weather data or default
    return weather_data.get(
        city_normalized,
        {
            "city": city,
            "temperature": 30,
            "condition": "مشمس (Sunny)",
            "humidity": 40,
            "wind_speed": 12,
        },
    )
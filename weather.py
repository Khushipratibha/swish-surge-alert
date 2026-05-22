import requests
from config import OPENWEATHER_API_KEY, CITY


def get_current_weather():
    """
    Fetches current weather data for the configured city.
    Returns a dict with weather condition and temperature.
    Raises an exception if the API call fails.
    """
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    return {
        "condition": data["weather"][0]["main"],        # e.g. "Rain", "Clouds"
        "description": data["weather"][0]["description"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "city": data["name"],
    }

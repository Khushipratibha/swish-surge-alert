from datetime import datetime


# ── Surge level constants ──────────────────────────────────────────────────────
LOW = "LOW"
MEDIUM = "MEDIUM"
HIGH = "HIGH"
CRITICAL = "CRITICAL"


def get_surge_level(weather: dict) -> dict:
    """
    Evaluates surge risk based on:
      - Current weather condition (rain, drizzle)
      - Time of day (breakfast, lunch, dinner, late-night windows)

    Returns a dict with surgeLevel, message, and reasoning.
    """
    condition = weather["condition"]
    hour = datetime.now().hour

    is_rain = condition in ["Rain", "Drizzle", "Thunderstorm"]
    is_breakfast = 8 <= hour <= 10
    is_lunch = 12 <= hour <= 14
    is_dinner = 19 <= hour <= 22
    is_peak = is_lunch or is_dinner
    is_late_night = hour >= 23 or hour <= 1

    # ── Decision logic ─────────────────────────────────────────────────────────
    if is_rain and is_peak:
        return {
            "surgeLevel": CRITICAL,
            "message": (
                "🚨 CRITICAL SURGE ALERT\n"
                f"Rain + {'Lunch' if is_lunch else 'Dinner'} peak detected in Bangalore.\n"
                "Actions:\n"
                "  • Pre-prep 3x all fast items (Maggi, sandwiches, beverages)\n"
                "  • Alert all available riders immediately\n"
                "  • Open backup prep station\n"
                f"Current weather: {weather['description'].title()}, {weather['temp']}°C"
            ),
            "reason": "rain + peak hours",
        }

    elif is_rain and is_breakfast:
        return {
            "surgeLevel": HIGH,
            "message": (
                "⚠️ HIGH SURGE ALERT\n"
                "Rain during breakfast hours detected.\n"
                "Actions:\n"
                "  • Pre-prep 2x breakfast items\n"
                "  • Ensure hot beverages are stocked\n"
                f"Current weather: {weather['description'].title()}, {weather['temp']}°C"
            ),
            "reason": "rain + breakfast hours",
        }

    elif is_rain:
        return {
            "surgeLevel": HIGH,
            "message": (
                "⚠️ HIGH SURGE ALERT\n"
                "Rain detected in Bangalore.\n"
                "Actions:\n"
                "  • Pre-prep 2x Maggi, sandwiches\n"
                "  • Check rider availability\n"
                f"Current weather: {weather['description'].title()}, {weather['temp']}°C"
            ),
            "reason": "rain detected",
        }

    elif is_peak:
        return {
            "surgeLevel": MEDIUM,
            "message": (
                "📈 PEAK HOUR ALERT\n"
                f"{'Lunch' if is_lunch else 'Dinner'} peak hours active.\n"
                "Actions:\n"
                "  • Ensure all prep stations fully stocked\n"
                "  • Monitor prep times closely\n"
                f"Current weather: {weather['description'].title()}, {weather['temp']}°C"
            ),
            "reason": "peak dining hours",
        }

    elif is_late_night:
        return {
            "surgeLevel": MEDIUM,
            "message": (
                "🌙 LATE NIGHT WINDOW\n"
                "Late night order window active.\n"
                "Actions:\n"
                "  • Stock up snack items and beverages\n"
                "  • Ensure at least 2 riders on standby\n"
                f"Current weather: {weather['description'].title()}, {weather['temp']}°C"
            ),
            "reason": "late night window",
        }

    else:
        return {
            "surgeLevel": LOW,
            "message": None,
            "reason": "no surge conditions detected",
        }

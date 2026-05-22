import schedule
import time
import logging
from datetime import datetime

from weather import get_current_weather
from surge_logic import get_surge_level, LOW
from notifier import send_telegram_alert

# ── Logging setup ──────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


def check_and_alert():
    """
    Core job: fetch weather → evaluate surge → send alert if needed.
    Runs every 30 minutes via the scheduler.
    """
    log.info("Running surge check...")

    try:
        weather = get_current_weather()
        log.info(f"Weather fetched: {weather['condition']}, {weather['temp']}°C, humidity {weather['humidity']}%")

        result = get_surge_level(weather)
        surge_level = result["surgeLevel"]
        message = result["message"]

        log.info(f"Surge level: {surge_level} | Reason: {result['reason']}")

        if surge_level != LOW and message:
            success = send_telegram_alert(message)
            if success:
                log.info(f"Alert sent successfully for surge level: {surge_level}")
            else:
                log.warning("Alert failed to send.")
        else:
            log.info("No surge detected. No alert sent.")

    except Exception as e:
        log.error(f"Error during surge check: {e}")


def main():
    log.info("🚀 Swish Surge Alert Agent started.")
    log.info("Checking every 30 minutes for surge conditions in Bangalore.")

    # Run once immediately on startup
    check_and_alert()

    # Then schedule every 30 minutes
    schedule.every(30).minutes.do(check_and_alert)

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()

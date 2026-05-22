# 🚨 Swish Kitchen Surge Alert Agent

A lightweight Python agent that proactively alerts Swish kitchen managers about incoming order surges — before they happen.

## The Problem It Solves

Swish's core promise is **fresh food in 10 minutes**. That promise breaks when the kitchen gets overwhelmed by sudden order spikes — during rain, IPL matches, or peak lunch/dinner hours. By the time the surge hits, it's already too late to pre-prep.

This agent checks conditions every 30 minutes and gives kitchen staff a **heads-up before the surge**, not after.

## How It Works

```
Every 30 minutes:
  1. Fetch live weather data for Bangalore (OpenWeatherMap API)
  2. Evaluate surge risk based on weather + time of day
  3. If surge detected → send Telegram alert to kitchen manager
  4. If no surge → stay silent (no spam)
```

## Surge Detection Logic

| Condition | Surge Level | Action Triggered |
|---|---|---|
| Rain + Lunch/Dinner peak | 🚨 CRITICAL | Pre-prep 3x, alert all riders |
| Rain + Breakfast hours | ⚠️ HIGH | Pre-prep 2x breakfast items |
| Rain only | ⚠️ HIGH | Pre-prep 2x, check riders |
| Lunch/Dinner peak only | 📈 MEDIUM | Stock all stations |
| Late night (11pm–1am) | 🌙 MEDIUM | Stock snacks and beverages |
| Normal conditions | ✅ LOW | No alert sent |

## Project Structure

```
swish-surge-alert/
├── main.py          # Entry point — runs the scheduler
├── weather.py       # Fetches live weather from OpenWeatherMap
├── surge_logic.py   # Surge detection brain
├── notifier.py      # Sends Telegram alert
├── config.py        # Loads environment variables
├── .env.example     # Template for secrets
├── requirements.txt # Dependencies
└── .gitignore
```

## Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/swish-surge-alert.git
cd swish-surge-alert
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up your secrets**
```bash
cp .env.example .env
```
Fill in your `.env` file:
```
OPENWEATHER_API_KEY=your_key_here
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
CITY=Bangalore
```

**4. Run the agent**
```bash
python main.py
```

The agent runs immediately on startup, then checks every 30 minutes automatically.

## Example Telegram Alert

```
🚨 CRITICAL SURGE ALERT
Rain + Dinner peak detected in Bangalore.
Actions:
  • Pre-prep 3x all fast items (Maggi, sandwiches, beverages)
  • Alert all available riders immediately
  • Open backup prep station
Current weather: Heavy Rain, 24°C
```

## Why This Matters for Swish

Swish owns its kitchen, tech, and last mile — which means it also owns the ability to act on predictive signals faster than any third-party platform ever could. This agent is a small example of what that closed-loop advantage looks like in practice.

## Built By

Pratibha — B.Tech CSE-AI, IGDTUW  
Built as a practical demonstration of AI agent design for Swish's operational challenges.

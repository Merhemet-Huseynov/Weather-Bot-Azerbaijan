# Weather Telegram Bot

## Overview

This project is a Telegram bot that provides weather information. Users can request both the current day's weather and a 5-day weather forecast for a specified city. The bot fetches data from the OpenWeather API and formats it for easy presentation to the user. It provides detailed weather data such as temperature, weather description, sunrise, and sunset times in Azerbaijani.

## Features

- **Current Weather**: Retrieves the weather data for the current day in a specific city.
- **5-Day Forecast**: Fetches a 5-day weather forecast for the specified city.
- **Telegram Integration**: Fully integrated with Telegram, allowing users to get weather information via simple commands.
- **Weather Details**: Provides information such as minimum and maximum temperatures, weather descriptions, sunrise, and sunset times.
- **Error Handling**: Handles errors gracefully, informing users when something goes wrong (e.g., city not found or invalid API key).

## Requirements

- **Python 3.8+**: Ensure Python 3.8 or later is installed on your system.
- **python-telegram-bot**: Library for interacting with the Telegram Bot API.
- **requests**: Used to make HTTP requests to the OpenWeather API.

Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `config.txt` file in the `weather_bot/config/` directory with your **Telegram bot token** and **OpenWeather API key**:

```text
BOT_TOKEN=your_telegram_bot_token
WEATHER_API_KEY=your_openweather_api_key
```

## Running the Bot

1. Clone or download the repository.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
3. To run the bot, execute the following command:
   ```bash
   python main.py
   ```

4. The bot will start and begin polling Telegram for commands.

## Commands

- `/start`: Displays a welcome message and instructions for using the bot.
- `/weather_daily [city_name]`: Retrieves the current day's weather information for the specified city.
- `/weather_forecast [city_name]`: Retrieves the 5-day weather forecast for the specified city.

### Example

To get a 5-day weather forecast for Baku:

```bash
/weather_forecast Bakı
```

## Modules

### 1. **Weather API** (`weather_api/weather_api.py`)

   - Handles API requests to OpenWeather to fetch weather data based on the city name.

### 2. **Configuration** (`weather_bot/config/load_config.py`)

   - Loads bot configuration such as the Telegram token and OpenWeather API key from a configuration file.

### 3. **Start Command** (`weather_bot/config/start.py`)

   - Handles the `/start` command and sends a welcome message to users.

### 4. **Weather Handlers** (`weather_bot/config/weather.py`)

   - Handles the `/weather_daily` and `/weather_forecast` commands to fetch and display weather data.

### 5. **Weather Formatting** (`weather_bot/utils/format_weather.py`)

   - Formats the weather data into a human-readable message for the user.

## Example Workflow

1. The bot receives a `/weather_forecast Bakı` command.
2. It makes an API request to OpenWeather for a 5-day forecast of Baku.
3. The bot formats and returns the forecast information to the user.

## Troubleshooting

- If you encounter issues, check the bot logs for detailed error messages.
- Ensure that you have a valid API key for OpenWeather and the correct Telegram bot token.
- Verify that you are using a compatible version of Python.
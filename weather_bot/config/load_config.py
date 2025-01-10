from dotenv import load_dotenv
import os

def load_config():
    # .env faylını yükləyin
    load_dotenv()

    # Ətraf mühit dəyişənlərini oxuyun
    config = {
        "BOT_TOKEN": os.getenv("BOT_TOKEN"),
        "WEATHER_API_KEY": os.getenv("WEATHER_API_KEY")
    }

    return config

# Konfiqurasiya yükləyir
config = load_config()

BOT_TOKEN = config.get("BOT_TOKEN")
WEATHER_API_KEY = config.get("WEATHER_API_KEY")
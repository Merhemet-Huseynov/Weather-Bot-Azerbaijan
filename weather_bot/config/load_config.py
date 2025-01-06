def load_config():
    config = {}
    with open("D:/weather_bot/weather_bot/config/config.txt", "r") as file:
        for line in file:
            # Hər bir xətti oxuyub "=" işarəsindən bölüb dəyəri təyin edirik
            if "=" in line:
                key, value = line.strip().split("=")
                config[key] = value
    return config

config = load_config()
BOT_TOKEN = config.get("BOT_TOKEN")
WEATHER_API_KEY = config.get("WEATHER_API_KEY")


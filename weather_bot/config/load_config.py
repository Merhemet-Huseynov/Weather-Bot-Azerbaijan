from pathlib import Path

def load_config():
    config = {}
    
    # Fayl yolunu düzgün qur
    config_path = Path(__file__).resolve().parent / "config.txt"
    
    # Faylı aç və oxu
    with open(config_path, "r") as file:
        for line in file:
            # "key=value" formatında məlumatları parçala
            if "=" in line:
                key, value = line.strip().split("=", 1)
                config[key] = value

    return config

# Konfiqurasiya yüklə
config = load_config()
BOT_TOKEN = config.get("BOT_TOKEN")
WEATHER_API_KEY = config.get("WEATHER_API_KEY")
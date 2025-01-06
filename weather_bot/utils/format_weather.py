from datetime import datetime

def format_forecast(forecast_data, is_daily=False):
    forecast_message = ""

    for day in forecast_data:
        date = day["date"]
        temp_min = day["temp_min"]
        temp_max = day["temp_max"]
        description = day["description"]
        sunrise = day.get("sunrise", "N/A")
        sunset = day.get("sunset", "N/A")

        # Sunrise və Sunset varsa, onları datetime formatına çeviririk
        if sunrise != "N/A":
            sunrise = datetime.utcfromtimestamp(sunrise).strftime("%H:%M:%S")
        if sunset != "N/A":
            sunset = datetime.utcfromtimestamp(sunset).strftime("%H:%M:%S")

        forecast_message += (f"📅 Tarix: {date}\n"
                             f"❄️ Min. Temp: {temp_min}°C\n"
                             f"🌞 Max. Temp: {temp_max}°C\n"
                             f"🌥️ Hava: {description}\n"
                             f"🌅 Gün Doğuşu: {sunrise}\n"
                             f"🌙 Gün Batışı: {sunset}\n\n")

        if is_daily:
            break  # yalnız ilk günü göstərmək üçün

    return forecast_message

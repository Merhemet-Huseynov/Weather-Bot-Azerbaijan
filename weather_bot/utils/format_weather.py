from datetime import datetime

def format_city_header(city_name):
    return f"🌍 Şəhər: {city_name}\n\n"

def format_date_info(day):
    """Hər gün üçün məlumatı formatlayır."""
    date = day["date"]
    temp_min = day["temp_min"]
    temp_max = day["temp_max"]
    description = day["description"]
    sunrise = day.get("sunrise", "N/A")
    sunset = day.get("sunset", "N/A")

    # Gün doğuşu və batışını formatlama
    sunrise = format_time(sunrise)
    sunset = format_time(sunset)

    return (f"📅 Tarix: {date}\n"
            f"❄️ Min. Temp: {temp_min}°C\n"
            f"🌞 Max. Temp: {temp_max}°C\n"
            f"🌥️ Hava: {description}\n"
            f"🌅 Gün Doğuşu: {sunrise}\n"
            f"🌙 Gün Batışı: {sunset}\n\n")

def format_time(timestamp):
    """UNIX timestamp-i oxunaqlı vaxta çevirir."""
    if timestamp == "N/A":
        return "N/A"
    return datetime.utcfromtimestamp(timestamp).strftime("%H:%M:%S")

def format_forecast(forecast_data, city_name, is_daily=False):
    """Tam proqnoz məlumatını formatlayır."""
    forecast_message = format_city_header(city_name)

    if is_daily:
        forecast_message += format_date_info(forecast_data[0])
    else:
        for day in forecast_data:
            forecast_message += format_date_info(day)

    return forecast_message
import requests
from weather_bot.config import WEATHER_API_KEY

def fetch_weather_data(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
        "lang": "az"
    }
    response = requests.get(base_url, params=params)
    return response

def parse_forecast_data(data):
    forecast_data = []
    for day in data["list"][::8]:
        date = day["dt_txt"].split()[0]
        temp_min = day["main"]["temp_min"]
        temp_max = day["main"]["temp_max"]
        description = day["weather"][0]["description"]
        forecast_data.append({
            "date": date,
            "temp_min": temp_min,
            "temp_max": temp_max,
            "description": description
        })
    return forecast_data

def handle_error(response):
    if response.status_code == 404:
        return (f"Şəhər tapılmadı, zəhmət olmasa düzgün "
                f"ad daxil edin."
                )
    elif response.status_code == 401:
        return (f"API açarınız yanlışdır, zəhmət olmasa "
                f" düzgün açar istifadə edin."
                )
    else:
        return (f"Xəta baş verdi: {response.status_code}. Zəhmət"
                f" olmasa daha sonra yenidən cəhd edin."
               )

def get_weather_forecast(city_name):
    response = fetch_weather_data(city_name, WEATHER_API_KEY)
    
    if response.status_code == 200:
        data = response.json()
        city_name = data["city"]["name"]
        forecast_data = parse_forecast_data(data)
        return city_name, forecast_data 
         
    return handle_error(response)
 
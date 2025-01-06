from telegram import Update
from telegram.ext import ContextTypes
from weather_api import get_weather_forecast
from utils.format_weather import format_forecast

async def weather_forecast_handler(update: Update, 
                                   context: ContextTypes.DEFAULT_TYPE
                                   ):
    city_name = " ".join(context.args)
    
    if city_name:
        forecast_data = get_weather_forecast(city_name)
        
        if isinstance(forecast_data, list):
            formatted_forecast = format_forecast(forecast_data)
            await update.message.reply_text(
                f"5 Günlük hava proqnozu:\n{formatted_forecast}"
            )
        else:
            await update.message.reply_text(
                f"Üzr istəyirəm, {city_name} üçün 5 günlük"
                f" proqnoz tapılmadı. {forecast_data}"
                )
    else:
        await update.message.reply_text(
            "Zəhmət olmasa şəhər adını yazın. Məsələn: /weather_forecast Bakı"
            )

async def weather_daily_handler(update: Update, 
                                context: ContextTypes.DEFAULT_TYPE
                                ):
    city_name = " ".join(context.args)
    
    if city_name:
        forecast_data = get_weather_forecast(city_name)
        
        if isinstance(forecast_data, list): 
            daily_forecast = forecast_data[0] 
            formatted_daily = format_forecast(forecast_data, is_daily=True)
            await update.message.reply_text(
                f"Günlük hava məlumatı:\n{formatted_daily}"
                )
        else:
            await update.message.reply_text(
                f"Üzr istəyirəm, {city_name} üçün günlük"
                f"hava məlumatı tapılmadı. {forecast_data}"
                )
    else:
        await update.message.reply_text(
            "Zəhmət olmasa şəhər adını yazın. Məsələn: /weather_daily Bakı"
            )
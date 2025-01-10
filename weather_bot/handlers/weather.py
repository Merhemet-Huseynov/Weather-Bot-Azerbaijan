from telegram import Update
from telegram.ext import ContextTypes
from weather_api import get_weather_forecast
from weather_bot.utils import format_forecast

async def send_forecast(update: Update, city_name: str, 
                        forecast_data: list, is_daily: bool = False):
    if is_daily:
        forecast = forecast_data[0]
        formatted_forecast = format_forecast(forecast_data, city_name, is_daily=True)
        await update.message.reply_text(
            f"Günlük hava məlumatı:\n{formatted_forecast}"
        )
    else:
        formatted_forecast = format_forecast(forecast_data, city_name)
        await update.message.reply_text(
            f"5 Günlük hava proqnozu:\n{formatted_forecast}"
        )

async def weather_forecast_handler(update: Update, 
                                   context: ContextTypes.DEFAULT_TYPE):
    city_name = " ".join(context.args)

    if city_name:
        result = get_weather_forecast(city_name)
        if isinstance(result, tuple) and len(result) == 2:
            city_name, forecast_data = result
            if isinstance(forecast_data, list):
                await send_forecast(update, city_name, 
                                    forecast_data, is_daily=False
                                    )
            else:
                await update.message.reply_text(
                    f"Üzr istəyirəm, {city_name} üçün 5 günlük "
                    f"proqnoz tapılmadı. {forecast_data}"
                )
        else:
            await update.message.reply_text(result)
    else:
        await update.message.reply_text(
            "Zəhmət olmasa şəhər adını yazın. "
            "Məsələn: /weather_forecast Bakı"
        )

async def weather_daily_handler(update: Update, 
                                context: ContextTypes.DEFAULT_TYPE):
    city_name = " ".join(context.args)

    if city_name:
        result = get_weather_forecast(city_name)
        if isinstance(result, tuple) and len(result) == 2:
            city_name, forecast_data = result
            if isinstance(forecast_data, list):
                await send_forecast(update, city_name, 
                                    forecast_data, is_daily=True)
            else:
                await update.message.reply_text(
                    f"Üzr istəyirəm, {city_name} üçün günlük "
                    f"hava məlumatı tapılmadı. {forecast_data}"
                )
        else:
            await update.message.reply_text(result)
    else:
        await update.message.reply_text(
            "Zəhmət olmasa şəhər adını yazın. "
            "Məsələn: /weather_daily Bakı"
        )

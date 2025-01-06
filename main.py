from telegram import Bot
from telegram.ext import Application, CommandHandler
from weather_bot.handlers.weather import weather_daily_handler, weather_forecast_handler
from weather_bot.handlers.start import start_handler

# Handler-ları qeydiyyatdan keçirin
application.add_handler(CommandHandler("start", start_handler))
application.add_handler(CommandHandler("weather_daily", weather_daily_handler))
application.add_handler(CommandHandler("weather_forecast", weather_forecast_handler))

if __name__ == "__main__":
    print("Bot started...")
    application.run_polling()

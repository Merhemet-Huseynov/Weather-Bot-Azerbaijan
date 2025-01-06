from telegram import Bot
from telegram.ext import Application, CommandHandler
from weather_bot.config import BOT_TOKEN
from weather_bot.handlers import weather_daily_handler, weather_forecast_handler
from weather_bot.handlers import start_handler

# Application yaradın
application = Application.builder().token(BOT_TOKEN).build()

# Handler-ları qeydiyyatdan keçirin
application.add_handler(CommandHandler("start", start_handler))
application.add_handler(CommandHandler("weather_daily", weather_daily_handler))
application.add_handler(CommandHandler("weather_forecast", weather_forecast_handler))

if __name__ == "__main__":
    print("Bot started...")
    application.run_polling()
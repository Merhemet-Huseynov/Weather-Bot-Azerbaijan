from telegram import Update
from telegram.ext import ContextTypes

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "Salam! Mən hava məlumatlarını təqdim edən botam.\n\n"
        "Aşağıdakı əmrlərdən istifadə edə bilərsiniz:\n"
        "/weather_daily [şəhər adı] - Günlük hava məlumatını əldə etmək üçün.\n"
        "/weather_forecast [şəhər adı] - 5 günlük hava proqnozunu əldə etmək üçün.\n"
        "Misal: /weather_forecast Bakı"
    )
    await update.message.reply_text(welcome_message)
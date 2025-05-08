import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from google import genai

# Gemini API kaliti
GEMINI_API_KEY = "AIzaSyAViOIXp_p23bZfM476fOYe7xyc284zrVc"

# Telegram bot tokeni
TELEGRAM_API_TOKEN = "7962173508:AAF6pVxFY9Hz1xhdB1SWHdpHvrDIApAUQys"

# Logging sozlamalari
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Gemini AI bilan suhbat funksiyasi
def chatbot(text):
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents='Faqat uzbek tilida yoz/n' + text
    )
    return response.text

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Assalamu alaykum, men BMI uchun Normamatova O'g'iloy tomonidan yaratilgan chatbotman. Savolingiz bolsa yozing?"
    )

# /help komandasi
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Savolingizni yozing, men javob beraman!")

# Matnli xabarlar uchun handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text
    try:
        response = chatbot(user_input)
        await update.message.reply_text(response)
    except Exception as e:
        logger.error(f"Xatolik: {e}")
        await update.message.reply_text("Xatolik yuz berdi. Keyinroq urinib ko‘ring.")

# Botni ishga tushirish
def main() -> None:
    application = Application.builder().token(TELEGRAM_API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

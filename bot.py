from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '8016563509:AAGnj_sS9eeMWkUULjUR8yn6ZgB1TdyHE2Y'  # ← вставлен твой токен

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Привет, {update.effective_user.first_name}! Я ресторанный бот.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()

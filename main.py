import logging
import yfinance as yf
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os 
from dotenv import load_dotenv
from utils.price_fetcher import get_crypto_prices, get_equities_prices

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Logging for debugging
logging.basicConfig(level=logging.INFO)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Send /portfolio to get the latest price update.")

# /portfolio command handler
async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    equities = get_equities_prices()
    crypto = get_crypto_prices()
    message = f"🗓️ Daily Portfolio Update:\n\n{equities}\n\n{crypto}"
    await update.message.reply_text(message)

# Main function to launch bot
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("portfolio", portfolio))
    app.run_polling()

if __name__ == "__main__":
    main()
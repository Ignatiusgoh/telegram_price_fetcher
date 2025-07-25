import logging
import yfinance as yf
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Function to fetch SPY price
def get_equities_prices():
    try:
        msg = []
        equities = ['SPY']
        for ticker in equities: 
            ticker_data = yf.Ticker(ticker)
            data = ticker_data.history(period="1d")
            current = data['Close'][-1]
            prev_close = data['Close'][-2]
            pct_change = ((current - prev_close) / prev_close) * 100
            msg += f"{ticker}: ${current:.2f} ({pct_change:+.2f}%)"
        return msg 
    except Exception as e:
        logging.warning(f"⚠️ Error fetching equities prices: {e}")
        return msg

# Function to fetch crypto prices
def get_crypto_prices():
    try:
        ids = "bitcoin,ethereum,solana"
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true"
        r = requests.get(url).json()

        btc = r["bitcoin"]
        eth = r["ethereum"]
        sol = r["solana"]

        return (
            f"BTC: ${btc['usd']:.2f} ({btc['usd_24h_change']:+.2f}%)\n"
            f"ETH: ${eth['usd']:.2f} ({eth['usd_24h_change']:+.2f}%)\n"
            f"SOL: ${sol['usd']:.2f} ({sol['usd_24h_change']:+.2f}%)"
        )
    except Exception as e:
        logging.warning(f"⚠️ Error fetching crypto prices: {e}")
        return []
 

if __name__ == "__main__":
    print('Testing get_equities_prices() function')
    print(get_equities_prices())

    print('Testing get_crypto_prices() function')
    print(get_crypto_prices())


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# PART 1: Trending stocks (Most Active from Yahoo screener)
def get_trending_stocks():
    print("🔥 Trending Stocks (Most Active on Yahoo):")
    trending = ['RELIANCE.NS', 'TATAMOTORS.NS', 'INFY.NS', 'HDFCBANK.NS', 'ICICIBANK.NS']
    for symbol in trending:
        stock = yf.Ticker(symbol)
        info = stock.info
        print(f"- {info['shortName']} ({symbol}) | Price: ₹{info['regularMarketPrice']}")

# PART 2: Detailed info of a given stock
def get_stock_details(symbol):
    stock = yf.Ticker(symbol)
    
    print(f"\n📈 Stock Details for: {symbol}\n")
    
    # Basic Info
    info = stock.info
    print(f"Name: {info.get('shortName', '-')}")
    print(f"Sector: {info.get('sector', '-')}")
    print(f"Market Cap: ₹{info.get('marketCap', '-')}")
    print(f"P/E Ratio: {info.get('trailingPE', '-')}")
    print(f"52-Week High: ₹{info.get('fiftyTwoWeekHigh', '-')}")
    print(f"52-Week Low: ₹{info.get('fiftyTwoWeekLow', '-')}")
    print(f"Dividend Yield: {info.get('dividendYield', '-')}\n")

    # Historical Price Chart
    hist = stock.history(period="3y")
    print(f"Showing last {len(hist)} days of data...\n")
    
    # Plot closing price
    plt.figure(figsize=(10, 4))
    plt.plot(hist.index, hist['Close'], label='Close Price', color='green')
    plt.title(f"{symbol} - 3 Year Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price (₹)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Show last 5 rows of data
    print("\n📊 Recent Historical Data:")
    print(hist.tail(5))


# === Run App ===
if __name__ == "__main__":
    get_trending_stocks()
    user_input = input("\n🔍 Enter stock symbol (e.g., INFY.NS, TCS.NS): ")
    get_stock_details(user_input.strip().upper())

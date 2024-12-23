import yfinance as yf
import pandas as pd

def get_bid_ask(symbol, interval="1m", period = "1d"):
    try:
        data = yf.download(tickers = symbol, interval = interval, period = period, progress = False)

        if data.empty:
            print("no data :(")
            return None
        
        #yfinance does not give intraday quotes so just going to use high low prices and set bid = low, ask = high, good proxy but needs to be fixed
        data["Bid"] = data["Low"]
        data["Ask"] = data["High"]

        return data[["Bid","Ask"]]
    except Exception as e:
        return e
    
def load_data(symbols, interval="1m", period = "1d"):
    data = {}
    for symbol in symbols:
        df = get_bid_ask(symbol=symbol, interval=interval, period=period)
        if df is not None:
            data[symbol] = df
        else:
            print("No data for this stock")
        return data
    
if __name__ == "__main__":
    symbols_to_fetch = ["BRK-A","BRK-B"]
    interval = "1m"
    period = "1d"

    data = load_data(symbols_to_fetch,interval, period)

    for symbol, df in data.items():
        print(df.head())


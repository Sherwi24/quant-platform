import yfinance as yf

def get_data(symbol="BTC-USD", period="6mo", interval="1h"):
    df = yf.download(symbol, period=period, interval=interval)

    # 🔥 FIX MULTI-INDEX ISSUE
    if isinstance(df.columns, __import__("pandas").MultiIndex):
        df.columns = df.columns.droplevel(1)

    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.dropna(inplace=True)

    return df
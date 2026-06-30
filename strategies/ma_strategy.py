def apply_strategy(df):
    df = df.copy()

    df["SMA_10"] = df["Close"].rolling(10).mean()
    df["SMA_50"] = df["Close"].rolling(50).mean()

    df["signal"] = 0

    df.loc[df["SMA_10"] > df["SMA_50"], "signal"] = 1
    df.loc[df["SMA_10"] < df["SMA_50"], "signal"] = -1

    df["signal"] = df["signal"].astype(int)

    return df
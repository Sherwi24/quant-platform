def backtest(df):
    cash = 10000.0
    position = 0.0

    for i in range(len(df)):
        signal = int(df["signal"].iloc[i])
        price = float(df["Close"].iloc[i])

        if signal == 1 and cash > 0:
            position = cash / price
            cash = 0.0

        elif signal == -1 and position > 0:
            cash = position * price
            position = 0.0

    return cash + position * float(df["Close"].iloc[-1])
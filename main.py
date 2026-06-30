from data_fetch import get_data
from strategies.ma_strategy import apply_strategy

def run():
    df = get_data("BTC-USD")
    df = apply_strategy(df)

    print("TYPE OF CLOSE COLUMN:")
    print(type(df["Close"]))

    print("\nFIRST ROW CLOSE VALUE:")
    print(df["Close"].iloc[0])

    print("\nTYPE OF SIGNAL:")
    print(type(df["signal"]))

    print("\nFIRST SIGNAL VALUE:")
    print(df["signal"].iloc[0])

if __name__ == "__main__":
    run()
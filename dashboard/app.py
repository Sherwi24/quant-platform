import streamlit as st
from data_fetch import get_data
from strategies.ma_strategy import apply_strategy
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_fetch import get_data
from strategies.ma_strategy import apply_strategy

st.title("Quant Trading Dashboard")

df = get_data("BTC-USD")
df = apply_strategy(df)

st.line_chart(df["Close"])
st.line_chart(df[["SMA_10", "SMA_50"]])
st.write(df.tail())
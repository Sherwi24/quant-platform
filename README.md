# 📊 Quantitative Trading & Risk Intelligence Platform

A Python-based quantitative trading system that fetches market data, generates trading signals, performs backtesting, and visualizes results through an interactive Streamlit dashboard.

---

## 🚀 Project Overview

This project simulates a simplified quantitative trading pipeline used in real-world trading systems.

It includes:

- 📡 Market data collection using Yahoo Finance
- 📊 Technical indicator generation (Moving Averages)
- 🧠 Trading strategy (SMA crossover)
- 📉 Backtesting engine (portfolio simulation)
- 📈 Interactive Streamlit dashboard

---

## 🧱 System Architecture

Market Data → Feature Engineering → Strategy → Backtesting → Visualization

---

## ⚙️ Features

### 📡 Data Pipeline
- Fetches historical BTC/stock data using `yfinance`
- Supports OHLCV data (Open, High, Low, Close, Volume)

### 📊 Trading Strategy
- Simple Moving Average (SMA) crossover strategy
- Buy signal: Short MA > Long MA  
- Sell signal: Short MA < Long MA  

### 📉 Backtesting Engine
- Simulates trades on historical data
- Tracks:
  - Portfolio value
  - Position size
  - Final returns

### 📈 Dashboard (Streamlit)
- Interactive price charts
- Moving average visualization
- Data preview table

---

## 🛠️ Tech Stack

- Python 🐍  
- Pandas & NumPy 📊  
- yfinance 📡  
- Streamlit 📈  
- Matplotlib 📉  

---

## 📁 Project Structure

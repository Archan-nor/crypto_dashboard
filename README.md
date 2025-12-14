# Real-Time Cryptocurrency Dashboard (Binance)

## Overview
This project is a real-time cryptocurrency dashboard developed using Python.
It displays live market data from Binance, including prices, price changes,
and candlestick charts. The project focuses on real-time data handling,
GUI development, and clean object-oriented design.

---

## Features
- Real-time cryptocurrency price ticker (BTC, ETH)
- Live price change and percentage change
- Color-coded price movement (green/red)
- Real-time candlestick chart (1-minute interval)
- Volume display
- Show / Hide chart functionality
- Responsive and organized GUI layout
- Graceful shutdown with WebSocket cleanup

---

## Technologies Used
- Python 3
- Tkinter
- Binance WebSocket API
- Binance REST API
- Matplotlib
- NumPy

---

## Project Structure
crypto_dashboard/

├── main.py                 # Entry point
├── components/
│   ├── __init__.py
│   ├── ticker.py          # CryptoTicker class
│   ├── orderbook.py       # OrderBookPanel class
│   ├── technical.py       # TechnicalAnalysisPanel class
│   └── futures.py         # FuturesPanel class
├── utils/
│   ├── __init__.py
│   ├── binance_api.py     # API helper functions
│   └── indicators.py      # Technical analysis calculations
├── config.py              # Configuration (symbols, colors, etc.)
└── requirements.txt       # Dependencies

requireme
  

## How to Run the Project
1. Install dependencies:
-pip install -r requirements.txt

2. Run the application:
-python main.py

## UI Design
The final UI design of the dashboard is saved in this folder

## Demo Video
A short demonstration video showing the main features of the dashboard:
Demo Video link: https://youtu.be/0DzV4oW11Z8

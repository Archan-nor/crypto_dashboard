
import tkinter as tk
import json, threading
from websocket import WebSocketApp
from config import BINANCE_WS, COLORS

class CryptoTicker(tk.Frame):
    def __init__(self, parent, symbol):
        super().__init__(parent, bd=1, relief=tk.GROOVE)
        self.symbol = symbol.lower()
        self.is_closing = False

        tk.Label(self, text=symbol, font=("Arial", 14, "bold")).pack(pady=5)
        self.price = tk.Label(self, text="--", font=("Arial", 28, "bold"))
        self.price.pack()
        self.change = tk.Label(self, text="--", font=("Arial", 11))
        self.change.pack(pady=5)

        self.ws = WebSocketApp(
            f"{BINANCE_WS}/{self.symbol}@ticker",
            on_message=self.on_message
        )
        threading.Thread(target=self.ws.run_forever, daemon=True).start()

    def on_message(self, ws, msg):
        if self.is_closing:
            return
        data = json.loads(msg)
        self.after(0, self.update_ui, data)

    def update_ui(self, data):
        price = float(data["c"])
        change = float(data["p"])
        percent = float(data["P"])
        color = COLORS["up"] if change > 0 else COLORS["down"]
        self.price.config(text=f"{price:,.2f} USDT", fg=color)
        self.change.config(text=f"{change:+,.2f} ({percent:+.2f}%)", fg=color)

    def close(self):
        self.is_closing = True
        if self.ws:
            self.ws.close()

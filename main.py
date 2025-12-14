
import tkinter as tk
from components.ticker import CryptoTicker
from components.technical import TechnicalAnalysisPanel
from config import SYMBOLS

class CryptoDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Binance Real-Time Dashboard")
        self.geometry("1200x720")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        top = tk.Frame(self)
        top.pack(fill=tk.X, padx=10, pady=10)

        self.tickers = []
        for sym in SYMBOLS[:2]:
            t = CryptoTicker(top, sym)
            t.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)
            self.tickers.append(t)

        self.chart = TechnicalAnalysisPanel(self, "BTCUSDT")
        self.chart.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def on_close(self):
        for t in self.tickers:
            t.close()
        self.chart.close()
        self.destroy()

if __name__ == "__main__":
    CryptoDashboard().mainloop()

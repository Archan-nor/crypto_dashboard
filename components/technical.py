
import tkinter as tk
import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from utils.binance_api import get_klines

class TechnicalAnalysisPanel(tk.Frame):
    def __init__(self, parent, symbol):
        super().__init__(parent)
        self.symbol = symbol
        self.visible = True
        self.is_closing = False

        controls = tk.Frame(self)
        controls.pack(anchor="w", pady=3)

        tk.Button(controls, text="Show Chart", command=self.show).pack(side=tk.LEFT)
        tk.Button(controls, text="Hide Chart", command=self.hide).pack(side=tk.LEFT, padx=5)
        tk.Label(controls, text="Chart Streaming | Tickers Active", fg="green").pack(side=tk.LEFT, padx=10)

        self.fig = Figure(figsize=(10,4))
        self.ax_price = self.fig.add_subplot(211)
        self.ax_vol = self.fig.add_subplot(212, sharex=self.ax_price)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.update_chart()

    def update_chart(self):
        if self.is_closing or not self.visible:
            return

        klines = get_klines(self.symbol)
        self.ax_price.clear()
        self.ax_vol.clear()

        for k in klines:
            t = datetime.datetime.fromtimestamp(k[0]/1000)
            o, h, l, c, v = float(k[1]), float(k[2]), float(k[3]), float(k[4]), float(k[5])
            color = "green" if c >= o else "red"
            self.ax_price.plot([t, t], [l, h], color=color)
            self.ax_price.plot([t, t], [o, c], linewidth=6, color=color)
            self.ax_vol.bar(t, v, color=color, width=0.0005)

        self.ax_price.set_title(f"{self.symbol} 1m Real-Time (Binance)")
        self.fig.autofmt_xdate()
        self.canvas.draw()
        self.after(10000, self.update_chart)

    def hide(self):
        self.visible = False
        self.canvas.get_tk_widget().pack_forget()

    def show(self):
        if not self.visible:
            self.visible = True
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            self.update_chart()

    def close(self):
        self.is_closing = True

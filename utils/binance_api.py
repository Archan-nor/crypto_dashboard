
import requests
from config import BINANCE_REST

def get_klines(symbol, interval="1m", limit=50):
    r = requests.get(
        f"{BINANCE_REST}/api/v3/klines",
        params={"symbol": symbol, "interval": interval, "limit": limit},
        timeout=10
    )
    r.raise_for_status()
    return r.json()

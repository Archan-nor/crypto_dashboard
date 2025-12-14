def sma(data, period=14):
    return sum(data[-period:]) / period

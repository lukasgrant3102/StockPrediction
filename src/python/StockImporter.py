from yfinance import *


class StockImporter:

    def __init__(self, ticker):
        StockInfo = Ticker(ticker)
        self.StockHistory = StockInfo.history(period='5y', interval='1wk')
        self.ticker = ticker
        self.StockCloseValues = self.StockHistory['Close']

    # Gets the closing value each day for specified stock
    def get_close_values(self):
        return self.StockCloseValues


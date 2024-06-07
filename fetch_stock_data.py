import pandas as pd
import yfinance as yf


def fetch_stock_data(start_date, end_date):
    ticker = "AAPL"
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data


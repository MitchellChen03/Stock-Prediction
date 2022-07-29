import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def stock_data():
    ticker = yf.Ticker('AAPL')
    ticker_history = ticker.history(start="2022-01-30", end = "2022-01-30", interval ='1mo' )
    print(ticker_history)

    sf = ticker_history
    df = pd.DataFrame({'Date':sf.index, 'Values':sf.values})
    print(pd.DataFrame({'Date':sf.index}))
    print(pd.DataFrame({'Values':sf.values}))
while True:
    stock_data()
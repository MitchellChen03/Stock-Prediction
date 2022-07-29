import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# function getting data for the last x years with x weeks space
# from checking data and specific observation.
def stock_data(ticker, period, interval, observation):
    ticker = yf.Ticker(ticker)
    ticker_history = ticker.history(period, interval)

    sf = ticker_history[observation]
    print(observation)
    df = pd.DataFrame({'Date':sf.index, 'Values':sf.values})


    x = df['Date'].tolist()
    y = df['Values'].tolist()

    plt.style.use('dark_background')
    plt.plot(x,y)
    plt.ylabel('Price($)')
    plt.xlabel('Date', rotation=0)
    plt.show()

if __name__ == '__main__':
    stock_data('GOOGL', '2y', '1wk', 'Open')
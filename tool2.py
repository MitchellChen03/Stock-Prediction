import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
msft = yf.Ticker("AAPL")
hist = msft.history(start="2021-01-03", end="2022-01-30")
print(hist)
df = pd.DataFrame(hist)
print(len(df.index))
######################################################

data = yf.download("AAPL", start="2021-01-03", end="2022-01-30")

finace = list(data['Close'])
print(finace)
print(len(finace))

# Program to calculate moving average
arr = finace
window_size = 3

i = 0
# Initialize an empty list to store moving averages
moving_averages = []

# Loop through the array to consider
# every window of size 3
for ind in range(len(data)-window_size +1 ):
    moving_averages.append(np.mean(finace[ind:ind+window_size]))


print(moving_averages)
print(len(moving_averages))

x_values = df.index
y_values = moving_averages

plt.plot(x_values,y_values)
plt.show()

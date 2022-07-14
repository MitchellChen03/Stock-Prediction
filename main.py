import numpy as np
import yfinance as yf
from matplotlib import pyplot as plt
import pandas as pd
import random

# this the y axis
data = yf.download("AAPL", start="2021-01-03", end="2022-01-30")

finace = list(data['Close'])

# first line
window = 30
average_data = []

for ind in range(len(finace) - window + 1):
    average_data.append(np.mean(finace[ind:ind + window]))

for ind in range(window - 1):
    average_data.insert(0, np.nan)

# second line

window2 = 20
average_data2 = []

for ind in range(len(finace) - window2 + 1):
    average_data2.append(np.mean(finace[ind:ind + window2]))

for ind in range(window2 - 1):
    average_data2.insert(0, np.nan)

# third line
window3 = 50
average_data3 = []

for ind in range(len(finace) - window3 + 1):
    average_data3.append(np.mean(finace[ind:ind + window3]))

for ind in range(window3 - 1):
    average_data3.insert(0, np.nan)

# This is the x axis
msft = yf.Ticker("AAPL")
hist = msft.history(start="2021-01-03", end="2022-01-30")
df = pd.DataFrame(hist)

# Calculate random for average 1
v1 = 0.005
v2 = 0.001
random1 = []

for ind in average_data:
    random_number = random.uniform(v1, v2)
    i = random_number * ind
    random1.append(i)
# Calculate random for average 2
random2 = []

for ind in average_data2:
    random_number2 = random.uniform(v1, v2)
    i = random_number2 * ind
    random2.append(i)
# Calculate random for average 3
random3 = []

for ind in average_data3:
    random_number3 = random.uniform(v1, v2)
    i = random_number3 * ind
    random3.append(i)
# sum of all the randoms

sum_random = []

for (item1, item2, item3) in zip(random1, random2, random3):
    sum_random.append(item1+item2+item3)

# Difference of the cost

dif_of_cost = []

for (item1, item2) in zip(finace, sum_random):
    dif_of_cost.append(item1 - item2)
# Percentage dif
percent_diff = []
for (item1, item2) in zip(dif_of_cost, sum_random):
    percent_diff.append((item2/item1)*100)

for i in percent_diff:
    print(i)


# plot the graph

plt.plot(df.index, finace)
plt.plot(df.index, average_data)
plt.plot(df.index, average_data2)
plt.plot(df.index, average_data3)
plt.plot(df.index, sum_random)
plt.plot(df.index, dif_of_cost)
plt.show()

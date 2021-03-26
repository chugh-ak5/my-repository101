import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tsla = wb.DataReader('TSLA', data_source='yahoo', start='2010-06-29')

tsla['simple_return'] = (tsla['Adj Close'] / tsla['Adj Close'].shift(1)) - 1
print(tsla['simple_return'])

# simple returns on TESLA
tsla['simple_return'].plot(figsize=(8,10))
plt.show()

# average daily returns on TESLA
avg_returns_daily = tsla['simple_return'].mean()
print(avg_returns_daily)

# average annual Returns on TESLA
avg_returns_annual = tsla['simple_return'].mean() * 250
print(avg_returns_annual)

# annual returns on TESLA as a %
print(str(round(avg_returns_annual, 4) * 100) + '%')

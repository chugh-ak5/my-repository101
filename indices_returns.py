import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

indices = ['^GDAXI', '^IXIC', '^GSPC', '^FCHI', '^BSESN', '^N225']

indices_data = pd.DataFrame()

for i in indices:
    indices_data[i] = wb.DataReader(i, data_source='yahoo', start='2010-01-01')['Adj Close']
    print(indices_data.head())
    print(indices_data.tail())

# normalizing the dataset of indices
(indices_data / indices_data.iloc[0] * 100).plot(figsize=(15,7));
plt.show()

# finding the daily returns on the indices
indices_returns = (indices_data / indices_data.shift(1)) - 1
print(indices_returns)

# annual returns on the indices
indices_annual_returns = indices_returns.mean() * 250
print(indices_annual_returns)

# annual returns on the indices as a %
print(str(round(indices_annual_returns, 4) * 100) + '%')

# comparing an individual securtity to check its performance
indices_stock_compare = ['BRK-B', '^GSPC', '^DJI']

indices_stock = pd.DataFrame()

for i in indices_stock_compare:
    indices_stock[i] = wb.DataReader(i, data_source='yahoo', start='2010-01-01')['Adj Close']
    print(indices_stock.head())
    print(indices_stock.tail())

# normalizing the dataset of the stock and indices
(indices_stock / indices_stock.iloc[0] * 100).plot(figsize=(15,7));
plt.show()

# highly correlated Berkshire Hathaway stock with weighting of ~1.5% on indices
print(indices_stock.corr())

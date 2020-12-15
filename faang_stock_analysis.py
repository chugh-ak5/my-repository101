import pandas as pd 	
import numpy as np 	
import seaborn as sns 	
import matplotlib.pyplot as plt 	
from pandas_datareader import data as wb	

tickers = ['FB', 'AAPL', 'AMZN', 'NFLX', 'GOOG']	

data = pd.DataFrame()	

for t in tickers:	
    data[t] = wb.DataReader(t, start='2020-01-01', end='2020-12-15', data_source='yahoo')['Adj Close']	
		print(data.head())	

#Normalized Data & Plots 	
normalized_data = (data / data.iloc[0] * 100)	
normalized_data.plot(figsize=(15,8))	
plt.show()	

#Descriptive Statistics & Correlation Matrix	
normalized_data.describe()	
corr_matrix = normalized_data.corr()	
sns.heatmap(corr_matrix, annot = True)	
plt.show()	

#Simple return on an Equally Weighted Portfolio 	
daily_returns = (data / data.shift(1)) - 1	
daily_returns.head()	

weights_1 = np.array([0.2, 0.2, 0.2, 0.2, 0.2])	
np.dot(daily_returns, weights_1)	

annualized_returns = daily_returns.mean() * 250	
np.dot(annualized_returns, weights_1)	

portfolio_1 = str(round(np.dot(annualized_returns, weights_1), 5) * 100) + '%'	
portfolio_1

#Simple return on an Unequally Weighted Portfolio 	
weights_2 = np.array([0.2,0.1,0.15,0.25,0.3])	
np.dot(daily_returns, weights_2)	
np.dot(annualized_returns, weights_2)	

portfolio_2 = str(round(np.dot(annualized_return, weights_2), 5) * 100) + '%'
portfolio_2

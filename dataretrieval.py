'''
Created on Nov 24, 2017

@author: connorfairman
'''
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

# Instruments to download
tickers = ['AAPL', 'MSFT', 'SPY', 'OSTK', 'GOOGL']

# Define online source to use
data_source = 'google'

# All available data from 01/01/2000 until 12/31/2016
start_date = '2015-05-01'
end_date = '2017-11-22'

#Use pandas_reader.data.DataReader to load the desired data. 
panel_data = data.DataReader(tickers, data_source, start_date, end_date)

#Getting just the adjusted closing prices. This will return a pandas datafram
#The index in this dataframe is the major index of the panel_data.
close = panel_data.ix['Close']

#Getting all weekdays between 01/01/2000 and 11/22/2017
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

#Align the existing prices in adj_close with our new set of dates.
#Reindex close using all_weekdays as the new index.
close = close.reindex(all_weekdays)

close.head(10)


#Now let's get the MSFT timeseries. This now returns a Pandas Series 
#object indexed by date.
msft = close.ix[:, 'OSTK']

#Calculate the 20 and 100 days moving averages of the closing prices
short_rolling_msft = msft.rolling(window=20).mean()
long_rolling_msft = msft.rolling(window=100).mean()

#Plot everything by leveraging the very powerful matplotlib package
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(msft.index, msft, label='OSTK')
ax.plot(short_rolling_msft.index, short_rolling_msft, label='20 days rolling')
ax.plot(long_rolling_msft.index, long_rolling_msft, label='100 days rolling')
ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()

print(plt.show())
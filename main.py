# Main source file to perform ML on Nvidia Stock Price Dataset
# https://www.kaggle.com/datasets/syedfaizanalii/nividia-stock-dataset-2023-2024

# Test Change
# Objective: 
# Given: a day's open, high, low, close, Adj close, and volume, 
# Determine: next day's close using machine learning


########################### SETUP #####################################
# Import Libs   
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
from matplotlib.ticker import MaxNLocator

# Generate the DataFrame from Yahoo Finance Data
#data_timeframe = 365
#today = datetime.today().strftime('%Y-%m-%d')
#one_year_ago = (datetime.today() - timedelta(days=data_timeframe)).strftime('%Y-%m-%d')
#symbol = "nvda"
#yf_nvda_data = yf.download(symbol, start=today, end=one_year_ago)

#print(f"the data looks like \n {yf_nvda_data}")


#msft = yf.Ticker("MSFT")


#msft.info
#print(f"the data looks like \n {msft.info}")




# Generate the DataFrame from CSV Data
df = pd.read_csv("nvidia_stock_data.csv")
print(f"The df structure looks like... \n {df}")

# Create a second DF that will hold the new data analysis
df_gen = df


# Break out Columns
dates      = df['Date']
opens      = df['Open']
highs      = df['High']
lows       = df['Low']
closes     = df['Close']
adj_closes = df['Adj Close']
volume     = df['Volume']


########################### COLUMN GEN ##################################

# Daily Price Change
day_results = []
for i,j in zip(opens, closes):
    if j > i:
        day_results.append('Higher') # Ended Higher
    else:
        day_results.append('Lower') # Ended Lower
df_gen['Daily Moves'] = day_results # Add column to new DF

# Create column for daily moves ($)
daily_moves_value = []
for i,j in zip(opens, closes):
    daily_moves_value.append(j-i)
df_gen["Daily Moves ($)"] = daily_moves_value

# Create column for daily moves (%)
daily_moves_percent = []
for i,j in zip(opens, closes):
    daily_moves_percent.append(((j-i)/i)*100)
df_gen["Daily Moves (%)"] = daily_moves_percent 

# Intraday Value Change (% Change from yesterday to today)
df_gen['Intraday Change (%)'] = df_gen['Close'].diff()

# Volitility
df_gen['Daily Volatility (30-day)'] = df_gen['Daily Moves (%)'].rolling(window=30).std() * np.sqrt(252)

# High Low Daily Difference
daily_difference_value = []
for c,b in zip(highs, lows):
    daily_difference_value.append(c-b)
df_gen["High Low Daily Difference"] = daily_difference_value

# Closes Adj_closes Daily Difference
daily_close_diff_value = []
for n,m in zip(closes, adj_closes):
    daily_close_diff_value.append(m-n)
df_gen["closes adj_closes daily difference"] = daily_close_diff_value







print(f"New dataset = \n {df_gen}")

########################### ANALYSIS ##################################

# Generate Plot
df.plot.scatter(x = 'Date', y = 'Close')
plt.xlabel('Date')  
plt.ylabel('Price ($)')  
plt.title('NVDA Price Close') 
plt.gca().xaxis.set_major_locator(MaxNLocator(5))
plt.grid()
plt.show()
#plt.plot()












# My BreakPoint
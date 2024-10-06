# Main source file to perform ML on Nvidia Stock Price Dataset
# https://www.kaggle.com/datasets/syedfaizanalii/nividia-stock-dataset-2023-2024

# Objective: 
# Given: a day's open, high, low, close, Adj close, and volume, 
# Determine: next day's close using machine learning


########################### SETUP #####################################
# Import Libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

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

# Analysis on Daily Moves
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
    daily_moves_percent.append((j-i)/i)
df_gen["Daily Moves (%)"] = daily_moves_percent



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
print(f"New dataset = \n {df_gen}")

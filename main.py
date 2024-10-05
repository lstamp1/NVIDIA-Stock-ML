# Main source file to perform ML on Nvidia Stock Price Dataset
# https://www.kaggle.com/datasets/syedfaizanalii/nividia-stock-dataset-2023-2024

# Import Libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Generate the DataFrame from CSV Data
df = pd.read_csv("nvidia_stock_data.csv")
print(f"The df structure looks like... \n {df}")

# Break out Columns
dates      = df['Date']
opens      = df['Open']
highs      = df['High']
lows       = df['Low']
closes     = df['Close']
adj_closes = df['Adj Close']
volume     = df['Volume']



# Analysis on Daily Moves
day_results = []
for i,j in zip(opens, closes):
    if j > i:
        day_results.append('Higher') # Ended Higher
    else:
        day_results.append('Lower') # Ended Lower
# Plot Daily Moves
plt.hist(day_results, bins=2, edgecolor='black')  
plt.title('Higher or Lower for Day')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()



# Generate Plot
df.plot.scatter(x = 'Date', y = 'Close')
plt.xlabel('Date')  
plt.ylabel('Price ($)')  
plt.title('NVDA Price Close') 
plt.gca().xaxis.set_major_locator(MaxNLocator(5))
plt.grid()
plt.show()
#plt.plot()


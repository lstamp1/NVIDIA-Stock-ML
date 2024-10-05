# Main source file to perform ML on Nvidia Stock Price Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

df = pd.read_csv("nvidia_stock_data.csv")



print(f"The df structure looks like... \n {df}")

df.plot.scatter(x = 'Date', y = 'Close')

plt.xlabel('Date')  
plt.ylabel('Price ($)')  
plt.title('NVDA Price Close') 
plt.gca().xaxis.set_major_locator(MaxNLocator(5))
plt.grid()
plt.show()
#plt.plot()


import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
path = 'Vipdata.xlsx'
df = pd.read_excel(path)
df_li=df.values.tolist()
dates=[]
for date in df_li:
    dates.append(date[0])

print(dates)
sends=[]
for send in df_li:
    sends.append(send[1])
print(sends)
z=pd.to_datetime(df['Date'])
print(z)
x_values=z

y_values=dates
# plt.style.use('seaborn')
ax= plt.subplots()
# my_x_ticks = np.arange(len(dates))
# plt.xticks = my_x_ticks
# ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
plt.plot(x_values,y_values) # Using a Colormap
plt.show()
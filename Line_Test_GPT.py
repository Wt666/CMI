import pandas as pd
import matplotlib.pyplot as plt

#Read Excel file
Data = pd.read_excel ('filename.xlsx')

#Set x and y axes
X = Data ['month']
Y = Data ['turnover']

#Draw a line diagram
plt.plot (X, Y, color = 'blue')

#Add chart title and axis labels
plt.title ('Month versus Turnover')
plt.xlabel ('month')
plt.ylabel ('turnover')

#Show chart
plt.show ()
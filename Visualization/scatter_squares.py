import matplotlib.pyplot as plt

x_values=range(1,500)

y_values=[x**2 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values,s=10,c=y_values, cmap=plt.cm.Blues) # Using a Colormap

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis=([0,1100,0,1100000])

plt.show()
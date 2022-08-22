import csv
import matplotlib.pyplot as plt
from datetime import datetime
import time
filename = 'pcc_2e-master/chapter_16/the_csv_file_format/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index,column_header)

    dates, highs, lows =[],[],[]
    for row in reader:
        # row[2] = int(row[2])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# print(highs)

#Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha = 0.5)
ax.plot(dates, lows, c='green', alpha = 0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# Format plot.
plt.title("Daily high temperatures-2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
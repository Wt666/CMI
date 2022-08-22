import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'pcc_2e-master/chapter_16/the_csv_file_format/data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, colunm_header in enumerate(header_row):
    #     print(index,colunm_header)

    dates, highs, lows = [], [], []
    for row in reader:
        # row[2] = int(row[2])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# print(highs)
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha = 0.5)
ax.plot(dates, lows, c='green', alpha = 0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# Format plot.
plt.title("Daily high temperatures-2018\nDeath Valley", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
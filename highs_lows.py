import csv
from matplotlib import pyplot as plt
from datetime import datetime


# Get dates, high, and low temperatures from file
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)


# Plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# Style plot
plt.title('Najwyższa i najniższa temperatura dnia, 2014', fontsize=24)
plt.xlabel("", fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()



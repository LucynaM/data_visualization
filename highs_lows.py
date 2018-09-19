import csv
from matplotlib import pyplot as plt
from datetime import datetime


# Get dates, high, and low temperatures from file
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)


# Plot data
fig = plt.figure(dpi=96, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Style plot
plt.title('Najwyższa i najniższa temperatura dnia, 2014\nDolina Śmierci, Kalifornia', fontsize=24)
plt.xlabel("", fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()



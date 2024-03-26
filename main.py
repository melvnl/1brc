import csv
from utils import time_decorator

@time_decorator
def calculate_stats(csv_filename):
    station_temperatures = {}
    station_counts = {}
    flag = 1

    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            flag = flag+1
            print("processing row: {}".format(flag))
            station = row[0]
            temperature = float(row[1])

            if station in station_temperatures:
                station_temperatures[station].append(temperature)
            else:
                station_temperatures[station] = [temperature]

            if station in station_counts:
                station_counts[station] += 1
            else:
                station_counts[station] = 1

    station_stats = {}
    for station, temperatures in sorted(station_temperatures.items()):
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / station_counts[station]
        max_temp = max(temperatures)
        station_stats[station] = (min_temp, mean_temp, max_temp)

    return station_stats

def print_station_stats(station_stats):
    result = '{'
    for station, stats in sorted(station_stats.items()):
        min_temp, mean_temp, max_temp = stats
        result += '{}={:.1f}/{:.1f}/{:.1f}, '.format(station, min_temp, mean_temp, max_temp)
    result = result.rstrip(', ') + '}'
    print(result)

# Calculate statistics
station_stats = calculate_stats('measurements.csv')

# Print statistics
print_station_stats(station_stats)

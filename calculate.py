import csv
from utils import time_decorator

class StationData:
    def __init__(self, name, min_temp, max_temp, sum_temp, count):
        self.name = name
        self.min = min_temp
        self.max = max_temp
        self.sum = sum_temp
        self.count = count

@time_decorator
def run():
    data = {}

    with open("measurements.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = row[0]
            temperature = float(row[1])

            if name not in data:
                data[name] = StationData(name, temperature, temperature, temperature, 1)
            else:
                station = data[name]
                if temperature < station.min:
                    station.min = temperature
                if temperature > station.max:
                    station.max = temperature
                station.sum += temperature
                station.count += 1
    print_result(data)

def print_result(data):
    sorted_keys = sorted(data.keys())
    print("{", end="")
    for key in sorted_keys:
        station = data[key]
        print(f"{station.name}={station.min:.1f}/{station.sum/station.count:.1f}/{station.max:.1f}, ", end="")
    print("}")

def main():
    # INFO: run took 6 minutes 22 seconds to execute.
    run()

if __name__ == "__main__":
    main()

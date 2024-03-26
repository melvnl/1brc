import random
import csv
import sys
from utils import time_decorator

city_names = [
    "Hamburg", "Bulawayo", "Palembang", "St. John's",
    "Cracow", "Bridgetown", "Istanbul", "Roseau", "Conakry"
]

def generate_temperature():
    # if we use .1f instead it will make the process faster even faster (13 minutes 22 seconds)
    # probably since round() is a math operations
    # return format(random.uniform(0, 99), '.1f')
    return round(random.uniform(0, 99), 1)

def generate_data_row():
    city = random.choice(city_names)
    temperature = generate_temperature()
    return [city, temperature]

@time_decorator
def generate_data(num_rows, filename):
    # INFO: generate_data took 16 minutes 19 seconds to execute.
    with open(filename, 'w', newline='') as csvfile:
        progress = 0
        writer = csv.writer(csvfile)
        batch_size = 10000 # instead of writing line by line to file, process a batch of stations and put it to disk
        chunks = num_rows // batch_size

        for chunk in range(chunks):
            data = []
            for _ in range(batch_size):
                city = random.choice(city_names)
                temperature = generate_temperature()
                data.append([city, temperature])

            writer.writerows(data)

            # Update progress bar every 1%
            if (chunk + 1) * 100 // chunks != progress:
                progress = (chunk + 1) * 100 // chunks
                bars = '=' * (progress // 2)
                sys.stdout.write(f"\r[{bars:<50}] {progress}%")
                sys.stdout.flush()
    sys.stdout.write('\n')

# Generate data for CSV
generate_data(1000000000, 'measurements.csv')

print("CSV file generated successfully.")

import random
import csv
from utils import time_decorator

city_names = [
    "Hamburg", "Bulawayo", "Palembang", "St. John's",
    "Cracow", "Bridgetown", "Istanbul", "Roseau", "Conakry"
]

def generate_temperature():
    return round(random.uniform(0, 99), 1)

def generate_data_row():
    city = random.choice(city_names)
    temperature = generate_temperature()
    return [city, temperature]

@time_decorator
def generate_data(num_rows, filename, num_threads=5):
    # INFO: generate_data took 2758.31 seconds to execute.
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(num_rows):
            city = random.choice(city_names)
            temperature = generate_temperature()
            writer.writerow([city, temperature])

# Generate data for CSV
generate_data(1000000000, 'measurements.csv')

print("CSV file generated successfully.")


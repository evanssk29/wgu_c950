# Steven Evans
# Student ID: 000391474
import csv

# Loads and appends address data
def load_address_data(fileName):
    address_data = []
    with open(fileName) as csv_file:
        count = 0
        csv_reader = csv.reader(csv_file, delimiter = ",")
        for row in csv_reader:
            address_data.append(row[0])
        return address_data
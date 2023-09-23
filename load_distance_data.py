# Steven Evans
# Student ID: 000391474
import csv

# Loads and returns distance data
def loadDistanceData(fileName):
    distance_data = []
    with open(fileName) as csv_file:
        count = 0
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            distance_data.append(row)
        return distance_data
# Steven Evans
# Student ID: 000391474
import csv
from package import Package

# parameters for package data
def loadPackageData(package_file, hash_table):
    with open(package_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            p_id = int(row[0])
            p_address = row[1]
            p_city = row[2]
            p_state = row[3]
            p_zip = row[4]
            p_deadline = row[5]
            p_weight = row[6]

            package = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight)
            hash_table.insert(p_id, package)

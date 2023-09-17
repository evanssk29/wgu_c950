import csv


def load_address_data(fileName):
    address_data = []
    with open(fileName) as csv_file:
        count = 0
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            # distList = [float(x) for x in row [0 : :] if x != ""]
            # distance_data.append(distList)
            address_data.append(row)
        return address_data
import csv
from package import Package


def loadPackageData(package_file, hash_table):
    with open(package_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            print(row)
            package = Package()
            package.id = int(str.strip(row[0]))
            package.TRUCK = None
            package.address = row[1]
            package.INFO: list[str] = [str.strip(x) for x in row[1::]]
            package.STATUS = 'HUB'
            package.delivered = None
            hash_table.insert(package.id, package)
            print(package)
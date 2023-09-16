import csv


def loadPackageData(package_file, hash_table):
    with open(package_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            print(row)
            PACKAGE = PACKAGE()
            PACKAGE.ID = int(str.strip(row[0]))
            PACKAGE.TRUCK = None
            PACKAGE.address = row[1]
            PACKAGE.INFO: list[str] = [str.strip(x) for x in row[1::]]
            PACKAGE.STATUS = 'HUB'
            PACKAGE.delivered = None
            hash_table.insert(PACKAGE.ID, PACKAGE)
            print(PACKAGE)
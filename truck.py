# Steven Evans
# Student ID: 000391474


def load_packages_truck(package_numbers_list, hTable):
    package_list = []
    for i in package_numbers_list:
        i = int(i)
        hTable.find(i).status = "TRANSIT"
        package_list.append(hTable.find(i))
    return package_list


class Truck:
    # Constructor to initialize the object with required parameters.
    def __init__(self, packages = None, time_left_hub = None):
        self.packages = packages
        self.time_left_hub = time_left_hub
        self.time = time_left_hub
        self.miles = 0
        self.current_location = "4001 South 700 East" # Sets location to HUB
        return
def load_packages_truck(package_numbers_list, hTable):
    package_list = []
    for i in package_numbers_list:
        i = int(i)
        hTable.find(i).status = "TRANSIT"
        package_list.append(hTable.find(i))
    return package_list


class Truck(object):

    def __init__(self, packages = None, location = None, current_time = None, time_left_hub = None):
        self.packages = packages
        self.location = location
        self.current_time = current_time
        self.time_left_hub = time_left_hub
        return

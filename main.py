import datetime
from hash_table import hash_table
from load_address_data import load_address_data
from load_distance_data import loadDistanceData
from load_package_data import loadPackageData
from truck import Truck
# Steven Evans
# Student ID: 000391474

# Import the distance and address CSV.
file_name = "csv/distanceCSV.csv"
address_file_name = "csv/addressCSV.csv"
distance_data = loadDistanceData (file_name)
print(distance_data)

print(float(distance_data[2][1])+0)

package_hashtable = hash_table()
print(package_hashtable.hash_array)
loadPackageData("csv/packageCSV.csv", package_hashtable)
print(package_hashtable.hash_array)

p = package_hashtable.find(9)
print(p)

address_data = load_address_data (address_file_name)
print(address_data)

def find_address_index(address_to_find):
    for address in address_data:
        if address_to_find == address[2]:
            return(int(address[0]))
    return -1

def get_distance_two_addresses(starting, destination):
    starting_index = find_address_index(starting)
    destination_index = find_address_index(destination)

    distance = 0
    #
    if starting_index > destination_index:
        distance = float(distance_data[starting_index][destination_index])
    #
    else:
        distance = float(distance_data[destination_index][starting_index])
    return distance
# Parameters for truck deliveries
def truck_delivery(truck):
    current_time = truck.time_left_hub
    current_location = truck.location

    while len(truck.packages) > 0: # While truck still has packages to deliver, prints distance.
        min_distance = 1000
        min_package = None
        for id in truck.packages:
            package = package_hashtable.find(id)
            distance = get_distance_two_addresses(current_location, package.address)
            if distance < min_distance:
                min_distance = distance
                min_package = package

        # Mark the package as delivered

        # Calculate delivery time
        current_time = current_time + datetime.timedelta(hours= min_distance/18)
        min_package.tDel = current_time
        print(min_package, min_distance)
        truck.packages.remove(min_package.id)

starting_address = address_data[12][2]

d = get_distance_two_addresses(starting_address, address_data[1][2])

print(d)
HUB = address_data[0][2]

truck_1 = Truck([1, 5, 9], HUB, time_left_hub= datetime.timedelta(hours=8))
truck_delivery(truck_1)

truck_2 = Truck([1, 5, 9], HUB, time_left_hub= datetime.timedelta(hours=9, minutes=10))
truck_delivery(truck_2)

truck_3 = Truck([1, 5, 9], HUB, time_left_hub= datetime.timedelta(hours=10, minutes= 30))
truck_delivery(truck_3)
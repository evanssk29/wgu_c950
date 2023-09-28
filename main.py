# Steven Evans
# Student ID: 000391474
import datetime
from hash_table import hash_table
from load_address_data import load_address_data
from load_distance_data import loadDistanceData
from load_package_data import loadPackageData
from truck import Truck

# Parameters for finding address
def find_address_index(address_to_find):
    index = 0
    for address in address_data:
        if address_to_find == address:
            return(index)
        index += 1
    return -1

# Compares the difference between two addresses
def get_distance_two_addresses(starting, destination):
    starting_index = find_address_index(starting)
    destination_index = find_address_index(destination)

    distance = 0

    if starting_index > destination_index:
        distance = float(distance_data[starting_index][destination_index])

    else:
        distance = float(distance_data[destination_index][starting_index])
    return distance

# test for distances
def test_distances():
    for address in address_data:
        distance = get_distance_two_addresses(address_data[0], address)
        print(distance)

# Import the distance and address CSV.
file_name = "distanceCSV.csv"
address_file_name = "addressCSV.csv"
distance_data = loadDistanceData(file_name)
package_hashtable = hash_table()
loadPackageData("packageCSV.csv", package_hashtable)
address_data = load_address_data(address_file_name)


# Greedy algorithm
def truck_delivery(truck):
    current_time = truck.time_left_hub
    current_location = truck.current_location

    while len(truck.packages) > 0:
        min_distance = 1000
        min_package = None
        for id in truck.packages:
            package = package_hashtable.search(id)
            distance = get_distance_two_addresses(current_location, package.address)
            if distance < min_distance:
                min_distance = distance
                min_package = package

        # Calculate delivery time
        current_time = current_time + datetime.timedelta(hours= min_distance/18)
        min_package.delivery_time = current_time
        min_package.status = "Delivered"
        min_package.left_hub = truck.time_left_hub
        truck.packages.remove(min_package.id)
        truck.miles += min_distance
        current_location = min_package.address


# Assigning packages to truck 1
t1 = [1, 2, 4, 5, 7, 8, 10, 11, 12, 21, 22, 23, 24, 26, 27, 29]
truck_1 = Truck(t1, time_left_hub= datetime.timedelta(hours=8)) # Time truck 1 left hub
truck_delivery(truck_1)

# Assigning packages to truck 2
t2 = [3, 13, 14, 15, 16, 17, 18, 19, 20, 30, 31, 33, 34, 35, 36, 38]
truck_2 = Truck(t2, time_left_hub= datetime.timedelta(hours=9, minutes=10)) # Time truck 2 left hub
truck_delivery(truck_2)

# Assigning packages to truck 3
t3 = [6, 25, 28, 32, 37, 39, 40, 9]
p9 = package_hashtable.search(9)

truck_3 = Truck(t3, time_left_hub= datetime.timedelta(hours=10, minutes= 30)) # Time truck 3 left hub
truck_delivery(truck_3)
total_miles = truck_1.miles + truck_2.miles + truck_3.miles # Total miles for all combined trucks

# User interface to search for packages
while True:
    print("****** Western Governors University Package Service ******")
    print("Total mileage for all trucks:", total_miles) # Prints total miles of all trucks combines
    print("1: All package status at certain time") # UI input options
    print("2: Single package status at a certain time")
    print("3: Exit")
    choice = input("Select an option")

    if choice == "1": #Prints all package status

        user_time_hour = int(input("What hour would you like to see? Enter in military time?"))
        user_time_minutes = int(input("What minutes would you like to see? Enter in military time?"))
        user_time = datetime.timedelta(hours=user_time_hour, minutes=user_time_minutes)

        # test to fix status update



        #

        for package_id in range(1, 41):
            p = package_hashtable.search(package_id)
            if user_time < datetime.timedelta(hours=10, minutes=20):
                p9.address = "300 State St,Salt Lake City,UT,84103"
            else:
                p9.address = "410 S State St,Salt Lake City,UT,84111"

            print(p)



    elif choice == "2": # Prints single package status

        package_id = int(input ("Enter package id"))
        p = package_hashtable.search(package_id)
        user_time_hour = int(input("What hour would you like to see?"))
        user_time_minutes = int(input("What minutes would you like to see?"))
        user_time = datetime.timedelta(hours=user_time_hour, minutes=user_time_minutes)



        if user_time < datetime.timedelta(hours=10, minutes=20):
            p9.address = "300 State St,Salt Lake City,UT,84103"
        else:
            p9.address = "410 S State St,Salt Lake City,UT,84111"


        print(p)


    elif choice == "3": # Exits ui
        exit()
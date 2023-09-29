# Steven Evans
# Student ID: 000391474
import datetime

import package
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
t1 = [1, 13, 5, 14, 15, 16, 19, 20, 29, 30, 31, 37, 40]
truck_1 = Truck(t1, time_left_hub= datetime.timedelta(hours=8)) # Time truck 1 left hub
truck_delivery(truck_1)

# Assigning packages to truck 2
t2 = [2, 3, 4, 7, 8, 18, 6, 25, 32, 34, 28, 36, 38]
truck_2 = Truck(t2, time_left_hub= datetime.timedelta(hours=9, minutes=10)) # Time truck 2 left hub
truck_delivery(truck_2)

# Assigning packages to truck 3
t3 = [9, 10, 11, 12, 17, 21, 35, 22, 23, 24, 26, 27, 33, 39]

p9 = package_hashtable.search(9)

truck_3 = Truck(t3, time_left_hub= datetime.timedelta(hours=10, minutes= 30)) # Time truck 3 left hub
truck_delivery(truck_3)
total_miles = truck_1.miles + truck_2.miles + truck_3.miles # Total miles for all combined trucks



# User interface to search for packages
while True:
    print("****** Western Governors University Package Service ******")
    print("Total mileage for all trucks:", total_miles) # Prints total miles of all trucks combines
    print("1: All package status at certain time")
    print("2: Single package status at a certain time")
    print("3: Exit")
    choice = input("Select an option")

    if choice == "1": #Prints all package status from ui choice 1

        user_time_hour = int(input("Enter hours in 24 hour format HH:"))
        user_time_minutes = int(input("Enter minutes MM:"))
        user_time = datetime.timedelta(hours=user_time_hour, minutes=user_time_minutes)
        delivery_time = package.time_status

        for package_id in range(1, 41):
            p = package_hashtable.search(package_id)
            # Updates package 9 to correct address at 1020
            if user_time < datetime.timedelta(hours=10, minutes=20):
                p9.address = "300 State St,Salt Lake City,UT,84103"
            else:
                p9.address = "410 S State St,Salt Lake City,UT,84111"

            print(p)



    elif choice == "2": # Prints single package status from ui choice 2

        package_id = int(input ("Enter package id:"))
        p = package_hashtable.search(package_id)
        user_time_hour = int(input("Enter hours in 24 hour format HH:"))
        user_time_minutes = int(input("Enter minutes MM:"))
        user_time = datetime.timedelta(hours=user_time_hour, minutes=user_time_minutes)


        # Updates package 9 to correct address at 1020
        if user_time < datetime.timedelta(hours=10, minutes=20):
            p9.address = "300 State St,Salt Lake City,UT,84103"
        else:
            p9.address = "410 S State St,Salt Lake City,UT,84111"

        print(p)


    elif choice == "3": # Exits ui
        exit()
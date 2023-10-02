# Steven Evans
# Student ID: 000391474
import datetime


class Package:

    # Constructor function with required parameters for Package.
    def __init__(self, a_id, address, city, state, z_zip, deadline, weight):
        self.id = a_id     # ID of the package
        self.address = address  # Address of package
        self.city = city   # City of package
        self.state = state  # State of package
        self.zip = z_zip   # Zip code of package
        self.deadline = deadline  # Package deadline
        self.weight = weight # Weight of package
        self.status = "HUB" # Beginning location
        self.delivery_time = None # Time package delivered
        self.left_hub = None # Time left HUB
        return


    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "Package ID: %s, Address: %s, %s, %s, %s, Deadline: %s, Weight: %s lbs, Status: %s, Delivered: %s, Time left HUB: %s" % (self.id, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.status, self.delivery_time, self.left_hub)

    # Updates status of package to en route, delivered, or at hub based on time
    def time_status(self, status_time):
            new_status = "En route" # if statement to show en route
            if status_time > self.delivery_time:
                new_status = "Delivered"

            elif status_time < self.left_hub: # else statement to show at hub
                new_status = "At HUB"
            return self.get_info(status_time, new_status)


    def get_info(self, comparison_time, new_status): # package 9's address updates at 10:20am

            address = self.address
            city = self.city
            state = self.state
            zip = self.zip
            # update package 9 at 10:20am
            if self.id == 9 and comparison_time < datetime.timedelta(hours=10, minutes=20):
                address = "300 State St"
                city = "Salt Lake City"
                state = "UT"
                zip = "84103"

            # else :
            #     address = "410 S State St"
            #     city = "Salt Lake City"
            #     state = "UT"
            #     zip = "84111"

            return "Package ID: %s, Address: %s, %s, %s, %s, Deadline: %s, Weight: %s lbs, Status: %s, Delivered: %s, Time left HUB: %s" % (self.id, address, city, state, zip, self.deadline, self.weight, new_status, self.delivery_time, self.left_hub)

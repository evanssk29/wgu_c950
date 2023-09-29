# Steven Evans
# Student ID: 000391474
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
        # Not working
        # if self.delivery_time > self.left_hub:
        #     self.status = "En route"
        # else:
        #     self.status = "At HUB"
        return "Package ID: %s, Address: %s, %s, %s, %s, Deadline: %s, Weight: %s lbs, Status: %s, Time delivered: %s, Time left HUB: %s" % (self.id, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.status, self.delivery_time, self.left_hub)



    #Not working
    # def time_status(self, status_time):
    #         new_status = "En route"
    #         if status_time > self.delivery_time:
    #             self.status = "Delivered"
    #             # new_status = "Delivered"
    #             return " Package ID: %s, Address: %s, %s, %s, %s, Deadline: %s, Weight: %s lbs, %s, Time Delivered: %s, Time Left HUB: %s" % (self.id, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.status, self.delivery_time, self.left_hub, new_status)
    #         elif status_time < self.left_hub:
    #             self.status = "At HUB"
    #             # new_status = "At HUB"
    #             return " status_time < self.left_hub Package ID: %s, Address: %s, %s, %s, %s, Deadline: %s, Weight: %s lbs, Updated Status: %s" % (self.id, self.address, self.city, self.state, self.zip, self.deadline, self.weight, new_status)
    #         else:
    #             return " else Package ID: %s, %s, %s, %s, %s, Weight: %s lbs, Deadline: %s, Updated Status: %s" % (self.id, self.address, self.city, self.state, self.zip, self.weight, self.deadline, new_status)

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
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip, self.weight, self.deadline, self.status, self.delivery_time, self.left_hub)

    def time_status(self, status_time):
        new_status = "Enroute"
        if status_time > self.delivery_time:
            new_status = "Delivered"
        elif status_time < self.left_hub:
            new_status = "At HUB"
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip, self.weight, self.deadline, new_status, self.left_hub, self.delivery_time,status_time)

class Package(object):

    def __init__(self, id = None, info = None, truck = None, location ='HUB', time_loaded = None, delivered = None):

        self.id = id     # ID of the package
        self.info = info   # A list that contains all information about the package
        self.truck = truck   # Truck name the package is transported on
        self.status = location    # Location of the package
        self.tLoaded = time_loaded   # Time package loaded onto a truck
        self.tDel = delivered   # Time of the delivery of the package
        self.address = None

        return
    def __str__(self):
        return f"{self.id} {self.address}"


    def printPackage(self):
        print("\n\nPackage ID = ", self.id)
        print(" Package Details = ", self.info)
        print("Truck of Package = ", self.truck)
        print("Status of Package = ", self.status)
        print("Time Package Loaded = ", self.tLoaded)
        print("Time Package Delivered= ", self.tDel)
        return
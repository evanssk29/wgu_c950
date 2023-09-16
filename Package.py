class package(object):

    def __init__(self, id = None, info = None, truck = None, location ='HUB', truck_loaded = None, delivered = None):

        self.ID = id
        self.info = info
        self.truck = truck
        self.STATUS = location
        self.tLoaded = truck_loaded
        self.tDel = delivered
        self.address = None

        return
    def __str__(self):
        return f"{self.ID} {self.address}"


    def printPackage(self):
        print("\n\nPackage ID = ", self.ID)
        print(" Package Details = ", self.info)
        print("Truck of Package = ", self.truck)
        print("Status of Package = ", self.STATUS)
        print("Time Package Loaded = ", self.tLoaded)
        print("Time Package Delivered= ", self.tDel)
        return
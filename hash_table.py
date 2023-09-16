from Package import package


class hash_table(object):

    def __init__(self, length = 10):
        self.length = length
        self.hash_array = []
        for i in range(self.length):
            self.hash_array.append([])
        return

    def insert(self, id, PACKAGE):
        key = hash(id) % self.length
        if [id, PACKAGE] not in self.hash_array[key]:
            self.hash_array[key].append([id, PACKAGE])
        return

    def printHashTable(self):
        print(self.hash_array)
        return

    def update(self, id, PACKAGE):
        key = hash(id) % self.length
        for x in self.hash_array[key]:
            if x[0] == id:
                x[1] = PACKAGE
        return

    def find(self, ID):
        key = hash(ID) % self.length
        for x in self.hash_array[key]:
            if x[0] == ID:
                return x[1]
            break
        return None

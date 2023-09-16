from hash_table import hash_table
from load_distance_data import loadDistanceData
from load_package_data import loadPackageData

file_name = "csv/distanceCSV.csv"

distance_data = loadDistanceData (file_name)
print(distance_data)

print(float(distance_data[2][1])+0)

package_hashtable = hash_table()
print(package_hashtable.hash_array)
loadPackageData("csv/packageCSV.csv", hash_table)
print(package_hashtable.hash_array)

p = package_hashtable.find(9)
print(p)
import pymongo  
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["mydatabase"] 

mycol=mydb["customer"]

## Sort
  
# Use the sort() method to sort the result in ascending or descending order.
# The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).

mydoc = mycol.find().sort("name")   #sort ascending

for x in mydoc:
  print(x)
  
# sort("name", 1) #ascending
# sort("name", -1) #descending

mydoc = mycol.find().sort("name", -1)   #sort descending

for x in mydoc:
  print(x)
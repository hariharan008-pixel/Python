import pymongo  
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["mydatabase"] 

mycol=mydb["customer"]

## FIND


# find_one()

x = mycol.find_one()  # returns the first occurrence in the selection.

print(x)


# find()

for x in mycol.find():  # returns all occurrences in the selection.
  print(x)
  
  
# Return Only Some Fields

for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):   # To find specific data.  when it is 0 it will exclude and when it is 1, it will include
  print(x)
  
for x in mycol.find({},{ "address": 0 }):  # This example will exclude "address" from the result:
    print(x)
    
# You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). 
# If you specify a field with the value 0, all other fields get the value 1, and vice versa:
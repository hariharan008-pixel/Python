import pymongo  
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["mydatabase"] 

mycol=mydb["customer"]

## Query

# When finding documents in a collection, you can filter the result by using a query object.
# The first argument of the find() method is a query object, and is used to limit the search.

myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
  
  
#Advanced Query

myquery = { "address": { "$gt": "S" } }  # use the greater than modifier: {"$gt": "S"}:

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
  
  
#Filter With Regular Expressions

myquery = { "address": { "$regex": "^S" } }  # use the regular expression {"$regex": "^S"}

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
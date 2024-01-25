import pymongo  
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["mydatabase"] 

mycol=mydb["customer"]

## Limit

# To limit the result in MongoDB, we use the limit() method.

myresult = mycol.find().limit(5)  # only return 5 documents:

#print the result:
for x in myresult:
  print(x)
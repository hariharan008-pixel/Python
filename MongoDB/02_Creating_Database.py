import pymongo  
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

## Creating DATABASE 

mydb=myclient["mydatabase"]

# Important: In MongoDB, a database is not created until it gets content!
# MongoDB waits until you have created a collection (table), with at least one document (record) 
# before it actually creates the database (and collection).

print(myclient.list_database_names())  # check if a database exist by listing all databases in you systemS
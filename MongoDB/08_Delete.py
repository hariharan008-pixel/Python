import pymongo  
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["mydatabase"] 

mycol=mydb["customer"]

## DELETE


# delete_one()
myquery = { "address": "Mountain 21" } 

mycol.delete_one(myquery)  # To delete one document


# delete_many()

myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)   # To delete more than one document

print(x.deleted_count, " documents deleted.")  


# delete_many({})

x = mycol.delete_many({})   # To delete all documents in a collection, pass an empty query object to the delete_many() method

print(x.deleted_count, " documents deleted.") 
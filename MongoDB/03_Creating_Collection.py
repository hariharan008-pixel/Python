import pymongo  
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["mydatabase"]
print(myclient.list_database_names()) 

## Creating Collection

# To create a collection in MongoDB, use database object and specify the name of the collection you want to create.

mycol=mydb["customer"]

print(mydb.list_collection_names())    # check if a collection exist in a database by listing all collections
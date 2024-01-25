import pymongo  
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["mydatabase"] 

mycol=mydb["customer"]

## UPDATE


# update_one()

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)  #update one document

for x in mycol.find():
  print(x)   #print "customers" after the update:
  

# update_many()

myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)   #update all document

print(x.modified_count, "documents updated.")
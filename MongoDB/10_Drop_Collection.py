import pymongo  
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["mydatabase"] 

mycol=mydb["customer"]

## Drop collection

mycol.drop()  #The "customer" collection deleted
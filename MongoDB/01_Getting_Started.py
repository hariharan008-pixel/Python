import pymongo  # Python distribution containing tools for working with MongoDB

# To create a database in MongoDB, start by creating a MongoClient object, 
# then specify a connection URL with the correct ip address and the name of the database you want to create.

myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # It is a class that allows for making "Connections" to a MongoDB
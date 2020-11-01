import pymongo 
from pymongo import MongoClient

# Create database and apply credentials

cluster = MongoClient("mongodb+srv://<db_name>:<password>@cluster0.elcej.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["<db_name>"]

collection = db["<db_name>"]

# Insert data 

'''post1 = {"_id": 1, "name": "Jay", "score": 10}
post2 = {"_id": 2, "name": "Lim", "score": 15}

collection.insert_many([post1, post2])'''  

'''results = list(collection.find())
print(results)'''

# Print all the results

'''results = collection.find()

for result in results:
    print(result)'''


# Use find_one to get single document from db

'''results = collection.find_one({"_id": 0})
print(results)'''

# Query db

'''results = collection.find({"_id": 0})

for result in results:
    print(result)
    print(result["_id"])'''

# Delete data

'''results = collection.delete_one({"_id":1})'''

# It will delete all data entry be careful

'''results = collection.delete_many({})'''

# Update data

'''results = collection.update_one({"_id":1}, {"$set":{"name":"Remz"}})'''

# Through update data can be added as well in the same field 

'''results = collection.update_one({"_id":1}, {"$set":{"greetings":"Hello"}})'''

# Dynamicly update data

change_name = {"name": "Jameson"}

collection.update_one({"_id":1}, {"$set":change_name})

results = collection.find_one({"_id": 1})
print(results)
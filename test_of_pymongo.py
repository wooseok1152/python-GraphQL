from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.for_graphql_CRUD

## insert

# db.users.insert_one({"name" : "choi", "age" : 28})
# db.users.insert_one({"name" : "kim", "age" : 30})

# select

print("* select users :")
users = list(db.users.find())
print(users, "\n")

print("* select user who is choi :")
user = list(db.users.find({"name" : "choi", "age" : 28}))[0]
print(user, "\n")
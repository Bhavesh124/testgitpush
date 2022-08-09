import pymongo
client=pymongo.MongoClient("mongodb+srv://Bhavesh:bhavesh123@cluster0.r9joiru.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)

d={
    "name":"Bhavesh",
    "email":"bhavesh@gmail.com",
    "surname":"chavan"
}
d={
    "name":"Bhavesh",
    "email":"bhavesh@gmail.com",
    "surname":"chavan"
}
d={
    "name":"Bhavesh",
    "email":"bhavesh@gmail.com",
    "surname":"chavan"
}
db1 = client['test']
coll = db1['test']
coll.insert_one(d )


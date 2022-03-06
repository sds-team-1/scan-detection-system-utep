# DatabaseHelper 
from pprint import pprint
from pymongo import MongoClient

class SDSDatabaseHelper:
    url = "mongodb://localhost:27017"

    def __init__(self):
        client = MongoClient(self.url)
        db = client.SDS
        serverStatusResult = db.command("serverStatus")
        pprint(serverStatusResult)

    def insertObject(self, id, object):
        object["_id"] = id
        client = MongoClient(self.url)
        db = client.SDS
        db.sds.insert_one(object)

    def insertObject(self, object):
        client = MongoClient(self.url)
        db = client.SDS
        db.sds.insert_one(object)

    def getObject(self, id):
        client = MongoClient(self.url)
        db = client.SDS
        return db.sds.find_one({"_id": id})

    def getObjects(self):
        client = MongoClient(self.url)
        db = client.SDS
        return db.sds.find()

    def getObjects(self, query):
        client = MongoClient(self.url)
        db = client.SDS
        return db.sds.find(query)

    def getObjects(self, query, projection):
        client = MongoClient(self.url)
        db = client.SDS
        return db.sds.find(query, projection)

    def getObjects(self, query, projection, sort):
        client = MongoClient(self.url)
        db = client.SDS
        return db.sds.find(query, projection, sort)

    def getObjects(self, query, projection, sort, limit):
        client = MongoClient(self.url)
        db = client.SDS
        return db.sds.find(query, projection, sort, limit)

    def deleteObjects(self, query):
        client = MongoClient(self.url)
        db = client.SDS
        db.sds.delete_many(query)

    def deleteSingle(self, id):
        client = MongoClient(self.url)
        db = client.SDS
        db.sds.delete_one({"_id": id})

    def updateObject(self, id, object):
        client = MongoClient(self.url)
        db = client.SDS
        db.sds.update_one({"_id": id}, {"$set": object})

    

    

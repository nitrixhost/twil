import pymongo
from pymongo import MongoClient

#authentication
def auth():
    try:
        return pymongo.MongoClient()
    except pymongo.errors.ConnectionFailure:
         print("Failed to connect to server")

#insert collection
def insert():
    print("insert")

#update collection
def update():
    print("update")

#delete collection
def delete():
    print("delete")

#find collection
def find():
    print("find")

#get collection
def get(namadatabase,collectionname):
    client = auth()
    db = client[namadatabase]
    collection = db[collectionname].find()
    return collection

    
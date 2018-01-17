import pymongo
from pymongo import MongoClient
import sys

namadatabase = "sms"
collectionuser = "users"
collectionsms = "collectionsms"

#authentication
def auth():
    try:
        kon = pymongo.MongoClient()
    except pymongo.errors.ConnectionFailure as detail:
        return {"success":"no","reason":detail}

    return kon

def konek():
    client = auth()
    db = client[namadatabase]
    return db

#insert collection
def insertSms(id):
    db = konek()
    db[collectionsms].insert(id)

def getSms(ligin):
    db = konek()
    collection = db[collectionsms].find({"token":ligin.get('user_id')})
    return collection 

def getSmsBySid(sid):
    db = konek()
    collection = db[collectionsms].find({"sid":sid})
    return collection

def insertUser(id):
    db = konek()
    db[collectionuser].insert(id)

def authUser(username,password):
    db = konek()
    cari = db[collectionuser].find({"username":username,"password":password})
    return cari
    
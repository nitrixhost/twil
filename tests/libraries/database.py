import pymongo
from pymongo import MongoClient
import sys

namadatabase = "sms"
collectionuser = "users"
collectionsms = "collectionsms"
kontak = "kontak"


class Auth:

    def auths(self):
        try:
            kon = pymongo.MongoClient()
        except pymongo.errors.ConnectionFailure as detail:
            raise ConnectionError("Koneksi error")

        return kon

    def konek(self):
        try:
            client = self.auths()
        except ConnectionError as detail:
            return detail

        db = client[namadatabase]
        return db


class Sms(Auth):

    def insertSms(self,id):
        db = self.konek()
        db[collectionsms].insert(id)

    def getSms(self,ligin):
        db = self.konek()
        collection = db[collectionsms].find({"token":ligin.get('user_id')})
        return collection

    def getSmsBySid(self,sid):
        db = self.konek()
        collection = db[collectionsms].find(sid)
        return collection


class User(Auth):

    def insertUser(self,id):
        db = self.konek()
        db[collectionuser].insert(id)

    def authUser(self,username,password):
        db = self.konek()
        cari = db[collectionuser].find({"username":username,"password":password})
        return cari


class Kontak(Auth):

    def insertKontak(self,param):
        db = self.konek()
        db[kontak].insert(param)

    def getKontakCategory(self,param):
        db = self.konek()
        cari = db[kontak].find({"token":param})
        return cari

    
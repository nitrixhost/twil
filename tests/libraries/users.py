from libraries.database import User
import secrets

user = User()

def addUser(username,password):
    token = secrets.token_urlsafe(32)
    user.insertUser({"username":username,"password":password,"token":token})

def authUser(username,password):
    suci = user.authUser(username,password)
    kon = list(suci)
    if not kon:
        return None
    else:
        for po in kon:
            return po.get('token')
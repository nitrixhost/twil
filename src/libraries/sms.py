import libraries.database
import json


#sending sms
def auth(authid,token):
    users = database.get("sms","users")
    for val in users:
        if val['balance'] == '0':
            return 0;
        else:
            return 1;

#sending sms
def sendsms(authid,token):
    auths = auth(authid,token)
    if auths == 0:
        return json.dumps({"status":"no","reason":"saldo tidak mencukupi"})
    else:
        print("sukses")
    
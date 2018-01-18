import twilio
from libraries.database import Sms
from twilio.rest import Client
from twilio.base import exceptions
import datetime
import json
from decimal import Decimal

account = "ACa1c851e917151177d17af5555bae6e9f"
token = "74ff1859dbc50bba3bb3d99474afa4b8"
froms = "+15005550006"

client = Client(account,token)
sms = Sms()


#convert datetime object
def convertdate(obk):
    if isinstance(obk,datetime.datetime):
        return obk.__str__()
    elif isinstance(obk,Decimal):
        return obk.__str__()


#insert sendsms resource response into database
def _todata(sids,login):
    dinam = {"sid":sids.sid,"from":sids.from_,"to":sids.to,"status":sids.status,"body":sids.body,
    "date_created":json.dumps(sids.date_created,default=convertdate),"date_sent":json.dumps(sids.date_sent,default=convertdate),
    "price":json.dumps(sids.price,default=convertdate),"error_code":sids.error_code,"error_message":sids.error_message,"num_segments":sids.num_segments,
    "num_media":sids.num_media,"date_updated":json.dumps(sids.date_updated,default=convertdate),"direction":sids.direction,"account_sid":sids.account_sid,
    "uri":sids.uri,"token":login.get('user_id')}
    sms.insertSms(dinam)

#getsms from id
def getsms(args):
    try:
        message = client.messages(args).fetch()
    except twilio.base.exceptions.TwilioRestException as details:
        return {"success":"no","reason":details.msg}

    hasil = {"sid":message.sid,"from":message.from_,"to":message.to,"status":message.status,"body":message.body,
    "date_created":json.dumps(message.date_created,default=convertdate),"date_sent":json.dumps(message.date_sent,default=convertdate),
    "price":json.dumps(message.price,default=convertdate),"error_code":message.error_code,"error_message":message.error_message,
    "num_segments":message.num_segments,"num_media":message.media,"date_updated":json.dumps(message.date_updated,default=convertdate),
    "direction":message.direction,"account_sid":message.account_sid,"uri":sids.uri}
    return hasil

#sending sms
def sendsms(args,login):
    try:
        message = client.messages.create(to=args['to'],from_=froms,body=args['body'])
    except twilio.base.exceptions.TwilioRestException as details:
        return {"success":"no","reason":details.msg}
    except twilio.base.exceptions.TwilioException as deon:
        return {"success":"no","reason":deon.msg}

    _todata(message,login)
    return {"success":"ok"}
    

#get all messages
def getallsms(ligin):
    getter = sms.getSms(ligin)
    collection = list(getter)
    for po in collection:
        yield {"sid":po.get('sid'),"from":po.get('from'),"to":po.get('to'),"body":po.get('body'),"status":po.get('status')}


#get sms by id
def getSmsBySid(sid):
    param = {"token":sid.get('user_id')}
    result = sms.getSmsBySid(param)
    return result
    

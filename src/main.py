from flask import Flask
from flask_restful import Resource,Api
from flask_restful.reqparse import RequestParser
from flask import jsonify
import libraries.database
import libraries.users
import libraries.sms
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sosd124/343as2338n'
api = Api(app,prefix='/v0.1')


#messages requirements
mes = RequestParser(bundle_errors=True)
mes.add_argument("to",type=str,required=True, help="field to required")
mes.add_argument("body",type=str,required=True, help="field body required")

class User(object):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "User(id='%s')" % self.id

def getallsms():
    getter = libraries.database.getSms()
    collection = list(getter)
    for po in collection:
        yield {"sid":po.get('sid'),"from":po.get('from'),"to":po.get('to'),"body":po.get('body'),"status":po.get('status')}

def authUser(username,password):
    data = libraries.users.authUser(username,password)
    return data

def verify(username,password):
    kun = authUser(username,password)
    if not (username and password):
        return False
    if not kun:
        return False
    else:
        return User(id=kun)

def identity(payload):
    user_id = payload['identity']
    return {"user_id":user_id}


jwt = JWT(app,verify,identity)
    

class GetMessage(Resource):
    @jwt_required()
    def get(self,sid):
        getter = libraries.database.getSmsBySid(sid)
        return getter

class Messages(Resource):
    @jwt_required()
    def post(self):
        arguments = mes.parse_args()
        lihat = libraries.sms.sendsms(arguments)
        return lihat

class MessageList(Resource):
    @jwt_required()
    def get(self):
        sam = getallsms()
        collection = list(sam)
        return jsonify(collection)


api.add_resource(GetMessage,'/messages/<sid>')
api.add_resource(Messages,'/messages')
api.add_resource(MessageList,'/messages')



if __name__ == '__main__':
    app.run(debug=True)
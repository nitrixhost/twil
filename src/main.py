from flask import Flask
from flask_restful import Resource,Api
from flask_restful.reqparse import RequestParser
from flask import jsonify
import libraries.users
import libraries.sms
import libraries.kontak
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sosd124/343as2338n'
api = Api(app,prefix='/v0.1')

#messages requirements
mes = RequestParser(bundle_errors=True)
mes.add_argument("to",type=str,required=True, help="field to required")
mes.add_argument("body",type=str,required=True, help="field body required")
kon = RequestParser(bundle_errors=True)
kon.add_argument("name",type=str,required=True, help="Name is required")
kon.add_argument("telp",type=int,required=True, help="Telp is required")
kon.add_argument("category",type=str,required=True, help="Category is required")
kok = RequestParser(bundle_errors=True)
kok.add_argument("category",type=str,required=True, help="category is required")

class User(object):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "User(id='%s')" % self.id

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
        getter = libraries.sms.getSmsBySid(sid)
        return getter

class Messages(Resource):
    @jwt_required()
    def post(self):
        arguments = mes.parse_args()
        login = dict(current_identity)
        lihat = libraries.sms.sendsms(arguments,login)
        return lihat

class MessageList(Resource):
    @jwt_required()
    def get(self):
        ligin = dict(current_identity)
        sam = libraries.sms.getallsms(ligin)
        collection = list(sam)
        return jsonify(collection)

class Kontak(Resource):
    @jwt_required()
    def post(self):
        argument = kon.parse_args()
        user = dict(current_identity)
        kona = libraries.kontak.insertKont(argument,user)
        return kona


class KontakCategory(Resource):
    @jwt_required()
    def get(self):
        user = dict(current_identity)
        kon = libraries.kontak.getCategory(user)
        collect = list(kon)
        return jsonify(collect)

    @jwt_required()
    def post(self):
        args = kok.parse_args()
        user = dict(current_identity)
        kon = libraries.kontak.getCategorybyName(args,user)
        collect = list(kon)
        return jsonify(collect)


class AddKontakByFile(Resource):
    @jwt_required()
    def post(self):
        user = dict(current_identity)


api.add_resource(GetMessage,'/messages/<sid>')
api.add_resource(Messages,'/messages')
api.add_resource(MessageList,'/messages')
api.add_resource(Kontak, '/kontak')
api.add_resource(AddKontakByFile,'/kontak/addfile')
api.add_resource(KontakCategory, '/kontak/category')



if __name__ == '__main__':
    app.run(debug=True)
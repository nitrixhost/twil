from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api = Api(app, prefix='/v0.1')

users = [{"email":"kuku@gmail.com","name":"kuku","id":1}]

sub = RequestParser(bundle_errors=True)
sub.add_argument("name",type=str, required=True, help="name is required")
sub.add_argument("email",required=True)
sub.add_argument("id",type=int,required=True,help="please add id")

def get_user(id):
    for x in users:
        if x.get('id') == int(id):
            return x

class SubscriberCollection(Resource):
    def get(self):
        return users

    def post(self):
        args = sub.parse_args()
        users.append(args)
        return {"msg":"subscriber added","data":args}, 201

class Subscriber(Resource):
    def get(self,id):
        user = get_user(id)
        if not user:
            return {"error":"user not found"}

        return user

    def put(self,id):
        args = sub.parse_args()
        user = get_user(id)
        if user:
            users.remove(user)
            users.append(args)
        
        return args

    def delete(self,id):
        user = get_user(id)
        if user:
            users.remove(id)

        return {"message":"deleted"}, 204


api.add_resource(SubscriberCollection,'/subscribers')
api.add_resource(Subscriber,'/subscriber/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
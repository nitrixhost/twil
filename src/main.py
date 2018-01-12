from flask import Flask, jsonify
from flask import request
from flask import abort
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

auth = HTTPBasicAuth()
@auth.get_password
def get_password(username):
    if username == "mimi":
        return 'python'
    return None

@auth.error_handler
def unauthorize():
    return jsonify({'error':'Unauthorized access'})


@app.route('/v0.1/messages/send',methods=['POST'])
@auth.login_required
def send():
    return "send"

@app.route('/v0.1/messages/history',methods=['GET'])
@auth.login_required
def history():
    return "history"

@app.route('/v0.1/contacts/category',methods=['GET'])
def category():
    return "category"

@app.route('/v0.1/contacts/category/list',methods=['GET'])
def catlist():
    return "categorylist"

@app.route('/v0.1/contacts/category/add',methods=['POST'])
def addcategory():
    return "addcategory"

@app.route('/v0.1/messages/search',methods=['GET'])
def searchmessages():
    return "searchmessages"

@app.route('/v0.1/contacts/category/search',methods=['GET'])
def searchcategory():
    return "searchcategory"


if __name__ == '__main__':
    app.run(debug=True)
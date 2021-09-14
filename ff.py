from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Users(Resource):

    pass

api.add_resource(Users, '/users')

class User(Resource):
    pass

api.add_resource(User,'/users/<userid>')

if __name__ == '__main__':
    app.run()

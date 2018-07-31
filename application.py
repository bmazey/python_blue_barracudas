import uuid
from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_sqlalchemy import SQLAlchemy

# what's happening
# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/

application = Flask(__name__)
api = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)

item = api.model('item', {
    'name': fields.String(required=True, description='item name'),
    'description': fields.String(required=True, description='item description'),
    'Price': fields.String(required=True, description='item price'),
    'Size': fields.String(required=True, description='item size'),
    'Color': fields.String(required=True, description='item color'),
    'Avail': fields.String(required=True, description='item availability'),
})

rumor_id = api.model('rumor_id', {
    'id': fields.String(readOnly=True, description='unique identifier of an item'),
    'name': fields.String(required=True, description='item name'),
    'description': fields.String(required=True, description='item description'),
    'Price': fields.String(required=True, description='item price'),
    'Size': fields.String(required=True, description='item price'),
    'Color': fields.String(required=True, description='item price'),
    'Avail': fields.String(required=True, description='item price'),
})


@api.route("/items")
class Items(Resource):
    @staticmethod
    def get():
        items = []
        shirt1 = {'Price': 35, 'Size': 2, 'Color': 'black', 'Avail': True, 'ID': 20384}
        items.append(shirt1)
        shirt2 = {'Price': 40, 'Size': 4, 'Color': 'red', 'Avail': True, 'ID': 20465}
        items.append(shirt2)
        shirt3 = {'Price': 27, 'Size': 6, 'Color': 'blue', 'Avail': True, 'ID': 20567}
        items.append(shirt3)
        return items


@api.route("/items/<string:color>")
class Color(Resource):
    def get(self, color):
        clothes = Items.get()
        return [shirt for shirt in clothes if shirt['Color'] == color]


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()

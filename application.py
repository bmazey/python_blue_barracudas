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
    things = [
        {'Price': 35,
         'Size': 2,
         'Color': 'black',
         'Avail': True,
         'ID': 20384
         }
    ]


def create_item():


@api.route("/items/price/ <Boolean: avl>")
class Items(Resource):
    things = [
        {
        }
    ]


@api.route("/items/price/ <int: prc>")
class Items(Resource):
    things = [
        {
        }
    ]


@api.route("/items/colors/<String: clr>")
class Items(Resource):
    things = [
        {
        }
    ]


@api.route("/items/size/<String: sz>")
class Items(Resource):
    things = [
        {
        }
    ]


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()

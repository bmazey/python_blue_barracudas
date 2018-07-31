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

item_id = api.model('rumor_id', {
    'id': fields.String(readOnly=True, description='unique identifier of an item'),
    'name': fields.String(required=True, description='item name'),
    'description': fields.String(required=True, description='item description'),
    'Price': fields.String(required=True, description='item price'),
    'Size': fields.String(required=True, description='item size'),
    'Color': fields.String(required=True, description='item color'),
    'Avail': fields.String(required=True, description='item availability'),
})


class Item(db.Model):
    id = db.Column(db.Text(80), primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.String(20), unique=False, nullable=False)
    size = db.Column(db.String(20), unique=False, nullable=False)
    color = db.Column(db.String(20), unique=False, nullable=False)
    avail = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return '<Rumor %r>' % self.content


def create_item(data):
    id = str(uuid.uuid4())
    name = data.get('name')
    description = data.get('description')
    item = Item(id=id, name=name, description=description)
    db.session.add(item)
    db.session.commit()
    return item


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


@api.route("/items/price/ <Boolean: avl>")
class ItemAvlRoute(Resource):
    @api.marshal_with(item_id)

    ]

    @api.route("/items/price/ <int: prc>")


class ItemPriceRoute(Resource):
    things = [
        {
        }
    ]


@api.route("/items/colors/<String: clr>")
class ItemColorRoute(Resource):
    things = [
        {
        }
    ]


@api.route("/items/size/<String: sz>")
class ItemSizeRoute(Resource):
    things = [
        {
        }
    ]


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()

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

    @api.expect(item)
    @api.marshal_with(item_id)
    def post(self):
        new_item = create_item(request.json)
        return Item.query.filter(Item.id == new_item.id)


@api.route("/items/<string:color>")
class Color(Resource):
    def get(self, color):
        clothes = Items.get()
        return [shirt for shirt in clothes if shirt['Color'] == color]


@api.route("/items/price/<string:avl>")
class Avail(Resource):
    def get(self, avl):
        clothes = Items.get()
        return [shirt for shirt in clothes if shirt['avl'] is True]


@api.route("/items/price/<string:prc>")
class ItemPriceRoute(Resource):
    def get(self, prc):
        clothes = Items.get()
        return [shirt for shirt in clothes if shirt['prc'] == prc]


@api.route("/items/size/<string:sz>")
class ItemSizeRoute(Resource):
    def get(self, sz):
        clothes = Items.get()
        return [shirt for shirt in clothes if shirt['sz'] == sz]


@api.route("/rumor/<string:id>")
class ItemIdRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, id):
        return Item.query.filter(Item.id == id)


def configure_db():
    db.create_all()
    db.session.commit()


# for testing only!
def get_app():
    return application


def main():
    configure_db()
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()

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

ns = api.namespace('api', description='Store where you can add your own items and search through them')

items_list = []

item = api.model('item', {
    'name': fields.String(required=True, description='item name'),
    'description': fields.String(required=True, description='item description'),
    'price': fields.Float(required=True, description='item price'),
    'size': fields.Integer(required=True, description='item size'),
    'color': fields.String(required=True, description='item color'),
    'availability': fields.Boolean(required=True, description='item availability'),
})

item_id = api.model('item_id', {
    'id': fields.Integer(readOnly=True, description='unique identifier of an item'),
    'name': fields.String(required=True, description='item name'),
    'description': fields.String(required=True, description='item description'),
    'price': fields.Float(required=True, description='item price'),
    'size': fields.Integer(required=True, description='item size'),
    'color': fields.String(required=True, description='item color'),
    'availability': fields.Boolean(required=True, description='item availability'),
})


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    price = db.Column(db.Float(80), unique=False, nullable=False)
    size = db.Column(db.Integer, unique=False, nullable=False)
    color = db.Column(db.String(80), unique=False, nullable=False)
    availability = db.Column(db.Boolean, unique=False, nullable=False)

    def __repr__(self):
        return '<Rumor %r>' % self.content


identifier = 0


def id_creator():
    global identifier
    identifier += 1
    return identifier


def create_item(data):
    identifier = id_creator()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    size = data.get('size')
    color = data.get('color')
    availability = data.get('availability')
    itm = Item(id=identifier, name=name, description=description, price=price, size=size, color=color,
               availability=availability)
    db.session.add(itm)
    db.session.commit()
    return itm


@ns.route("/items")
class Items(Resource):
    @api.marshal_with(item_id)
    def get(self):
        return Item.query.all()

    @api.expect(item)
    @api.marshal_with(item_id)
    def post(self):
        new_item = create_item(request.json)
        items_list.append(new_item)
        return Item.query.filter(Item.id == new_item.id).one()


@ns.route("/items/color/<string:color>")
class ItemColorRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, color):
        return Item.query.filter(Item.color == color)


@ns.route("/items/name/<string:name>")
class ItemNameRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, name):
        return Item.query.filter(Item.name == name)


@ns.route("/items/availability/<string:availability>")
class ItemAvailabilityRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, avl):
        return Item.query.filter(str(Item.availability) == avl)


@ns.route("/items/price/<int:price>")
class ItemPriceRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, prc):
        return Item.query.filter(str(Item.price) == prc)


@ns.route("/items/size/<int:size>")
class ItemSizeRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, sz):
        return Item.query.filter(str(Item.size) == sz)


@ns.route("/rumor/<int:id>")
class ItemIdRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, ident):
        return Item.query.filter(str(Item.id) == ident)


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

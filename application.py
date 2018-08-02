from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_sqlalchemy import SQLAlchemy

# what's happening
# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/

# simple flask app definitions
application = Flask(__name__)
api = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)

# renames namespace
ns = api.namespace('api', description='Store where you can add your own items and search through them')

'''
json marshaller (object <-> json)
'''
# input item
item = api.model('item', {
    'name': fields.String(required=True, description='item name'),
    'description': fields.String(required=True, description='item description'),
    'price': fields.Float(required=True, description='item price'),
    'size': fields.Integer(required=True, description='item size'),
    'color': fields.String(required=True, description='item color'),
    'availability': fields.String(required=True, description='item availability'),
})

# item with ID
item_id = api.model('item_id', {
    'id': fields.Integer(readOnly=True, description='unique identifier of an item'),
    'name': fields.String(required=True, description='item name'),
    'description': fields.String(required=True, description='item description'),
    'price': fields.Float(required=True, description='item price'),
    'size': fields.Integer(required=True, description='item size'),
    'color': fields.String(required=True, description='item color'),
    'availability': fields.String(required=True, description='item availability'),
})


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    price = db.Column(db.Float(80), unique=False, nullable=False)
    size = db.Column(db.Integer, unique=False, nullable=False)
    color = db.Column(db.String(80), unique=False, nullable=False)
    availability = db.Column(db.String(50), unique=False, nullable=False)

    def __repr__(self):
        return '<Rumor %r>' % self.content


# id variable
identifier = 0


# increments ID by one
def id_creator():
    global identifier
    identifier += 1
    return identifier


# creates an item by taking info from client
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


'''
API controllers
'''


@ns.route("/items")
class Items(Resource):
    @api.marshal_with(item_id)
    # gets all items
    def get(self):
        return Item.query.all()

    @api.expect(item)
    @api.marshal_with(item_id)
    # creates item
    def post(self):
        new_item = create_item(request.json)
        return Item.query.filter(Item.id == new_item.id).one()


# returns 418 teapot error
@ns.route('/teapot')
@api.response(418, 'Category not found.')
class Teapot(Resource):
    def get(self):
        return None, 418


# deletes an item
@ns.route("/items/delete/<int:id>")
class Delete(Resource):
    @api.marshal_with(item_id)
    # deletes items by id
    def delete(self, id):
        del_item = Item.query.filter(Item.id == id).one()
        db.session.delete(del_item)
        db.session.commit()
        return del_item


# updates description of an item
@ns.route("/items/patch/<int:id>/<string:new_description>")
class ItemDescriptionUpdate(Resource):
    @api.marshal_with(item_id)
    def patch(self, id, new_description):
        this_item = Item.query.filter(Item.id == id).one()
        this_item.description = new_description
        db.session.add(this_item)
        db.session.commit()
        return this_item


# returns the item that the id corresponds to
@ns.route("/items/id/<int:id>")
class ItemIdRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, id):
        return Item.query.filter(Item.id == id).one()


# returns all items with that color
@ns.route("/items/color/<string:color>")
class ItemColorRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, color):
        return Item.query.filter(Item.color == color).all()


# returns item with corresponding name
@ns.route("/items/name/<string:name>")
class ItemNameRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, name):
        return Item.query.filter(Item.name == name).all()


# returns item with corresponding availability
@ns.route("/items/availability/<string:availability>")
class ItemAvailabilityRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, availability):
        return Item.query.filter(Item.availability == availability).all()


# returns item with corresponding prices
@ns.route("/items/price/<float:price>")
class ItemPriceRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, price):
        return Item.query.filter(Item.price == price).all()


# returns items that cost less than max
@ns.route("/items/price/max/<float:max>")
class ItemMaxPriceRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, max):
        return Item.query.filter(Item.price <= max).all()


# returns items that cost more than min
@ns.route("/items/price/min/<float:min>")
class ItemMinPriceRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, min):
        return Item.query.filter(Item.price >= min).all()


# returns item within the price range
@ns.route("/items/price/range/<float:max>/<float:min>")
class ItemMinPriceRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, max, min):
        return Item.query.filter(min <= Item.price, max >= Item.price).all()


# returns item with corresponding size
@ns.route("/items/size/<int:size>")
class ItemSizeRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, size):
        return Item.query.filter(Item.size == size).all()


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

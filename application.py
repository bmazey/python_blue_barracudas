from flask import Flask
from flask_restplus import Resource, Api

# what's happening
# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
application = Flask(__name__)
api = Api(application)


@api.route("/hello")                   # Create a URL route to this resource
class HelloWorld(Resource):            # Create a RESTful resource
    def get(self):                     # Create GET endpoint
        return {'hello': 'bitches'}


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

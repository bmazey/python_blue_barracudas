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
    def get(self):
        things = [
            {'Price': 35,
                'Size': 2,
                'Color': 'black',
                'Avail' : True,
                'ID': 20384
        }
        ]
        return things

def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()

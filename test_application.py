from unittest import TestCase
from application import get_app


class AppDBTests(TestCase):
    def setUp(self):
        self.application = get_app()
        self.client = self.application.test_client()

    # def tearDown(self):
    #     """
    #     Ensures that the database is emptied for next unit test
    #     """
    #     self.app = Flask(__name__)
    #     db.init_app(self.app)
    #     with self.app.app_context():
    #         db.drop_all()

    def test_simple_get(self):
        response = self.client.get('/items')
        print(response.get_json())
        self.assertTrue(200, response.status_code)

    def test_id_get(self):
        response = self.client.get("/items/id/<int:id>")
        print(response.get_json())
        self.assertTrue(200, response.status_code)

    def test_name_get(self):
        response = self.client.get("/items/name/<string:name>")
        print(response.get_json())
        self.assertTrue(200, response.status_code)

    def test_price_get(self):
        response = self.client.get("/items/price/<int:price>")
        print(response.get_json())
        self.assertTrue(200, response.status_code)

    def test_size_get(self):
        response = self.client.get("/items/size/<int:size>")
        print(response.get_json())
        self.assertTrue(200, response.status_code)

    def test_color_get(self):
        response = self.client.get("/items/color/<string:color>")
        print(response.get_json())
        self.assertTrue(200, response.status_code)

    def test_availability_get(self):
        response = self.client.get("/items/availability/<string:availability>")
        print(response.get_json())
        self.assertTrue(200, response.status_code)

    def test_delete(self):
        response = self.client.get("/items/delete/<int:id>")
        print(response.get_json())
        self.assertTrue(200, response.status_code)

    def test_patch(self):
        response = self.client.get("/items/delete/<int:id>/<string:new_description>")
        print(response.get_json())
        self.assertTrue(200, response.status_code)

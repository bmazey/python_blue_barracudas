from unittest import TestCase
from application import get_app


class AppDBTests(TestCase):
    def setUp(self):
        self.application = get_app()
        self.client = self.application.test_client()

    # tests get all items
    def test_simple_get(self):
        response = self.client.get('/items')
        self.assertTrue(200, response.status_code)

    # tests getting item with corresponding id
    def test_id_get(self):
        response = self.client.get("/items/id/<int:id>")
        self.assertTrue(200, response.status_code)

    # tests getting item with corresponding name
    def test_name_get(self):
        response = self.client.get("/items/name/<string:name>")
        self.assertTrue(200, response.status_code)

    # tests getting item with corresponding price
    def test_price_get(self):
        response = self.client.get("/items/price/<int:price>")
        self.assertTrue(200, response.status_code)

    # tests getting item with corresponding size
    def test_size_get(self):
        response = self.client.get("/items/size/<int:size>")
        self.assertTrue(200, response.status_code)

    # tests getting item with corresponding color
    def test_color_get(self):
        response = self.client.get("/items/color/<string:color>")
        self.assertTrue(200, response.status_code)

    # tests getting item with corresponding availability
    def test_availability_get(self):
        response = self.client.get("/items/availability/<string:availability>")
        self.assertTrue(200, response.status_code)

    # tests if item is deleted
    def test_delete(self):
        response = self.client.get("/items/delete/<int:id>")
        self.assertTrue(200, response.status_code)

    # tests if description is updated
    def test_patch(self):
        response = self.client.get("/items/delete/<int:id>/<string:new_description>")
        self.assertTrue(200, response.status_code)

    # tests 418 teapot error
    def test_teapot(self):
        response = self.client.get("/teapot")
        self.assertTrue(418, response.status_code)

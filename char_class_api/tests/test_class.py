from flask import url_for, Response
from flask_testing import TestCase
from application import app


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_class(self):
               
        response = self.client.get(url_for('name'))
        self.assertEqual(response.status_code, 200)

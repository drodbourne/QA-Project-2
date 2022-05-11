from flask import url_for, Response, request, redirect, render_template
from flask_testing import TestCase
from application import app
import requests ,json


class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):
  
    def test_attribute(self):

        char_name = "Half Elf"
        char_class = "Ranger"
        
        response = self.client.post(url_for('attribute'), json = {"Name": char_name, "Class": char_class})

        self.assertEqual(response.status_code, 200)
        self.assertIn("+6 to Bow & Arrow", response.data.decode())
            

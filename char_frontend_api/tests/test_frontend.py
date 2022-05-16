from application import app, db
from application.models import Character
from datetime import date
import requests_mock 
import requests ,json

from flask import render_template, redirect, url_for, request
from flask_testing import TestCase



# Create the base class
class TestBase(TestCase):
    def create_app(self):
        
        return app

    

    


class TestViews(TestBase):
  
    def test_home(self):
        # mock values
        char_name = "Half Elf"
        char_class = "Ranger"
        
        with requests_mock.Mocker() as m:
            m.get("http://char_name_api:5000/get_name", text=char_name)
            m.get("http://char_class_api:5000/get_class", text=char_class)
            m.post("http://char_attribute_api:5000/get_attribute", json = {"Name": char_name, "Class": char_class})
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn("Half Elf", response.data.decode())
            self.assertIn("Ranger", response.data.decode())
         


      










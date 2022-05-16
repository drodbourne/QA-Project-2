from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import Character
import requests ,json
import datetime

db.create_all()

@app.route('/', methods = ['GET'])
def home():
    char_name = requests.get('http://char_name_api:5000/get_name')
    char_class = requests.get('http://char_class_api:5000/get_class')
    char_attribute = requests.post('http://char_attribute_api:5000/get_attribute', json = {"Name": char_name.text, "Class": char_class.text})
    char_db = Character(char_name = char_name.text, char_class = char_class.text, char_attribute = char_attribute.text)
    db.session.add(char_db)
    db.session.commit()
    prev5 = Character.query.order_by(Character.id.desc()).limit(5).all()
    return render_template('index.html', char_name = char_name.text, char_class = char_class.text, char_attribute = char_attribute.text, prev5 = prev5 )

#@app.route('/history', methods=['GET'])
#def history():
 #   events_history = Events.query.all()
  #  return render_template('history.html', events_history = events_history)

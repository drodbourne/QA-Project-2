from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

db = SQLAlchemy(app)

from application import routes

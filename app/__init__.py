from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


db = SQLAlchemy(app)
app.secret_key = 'hi'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://rox:fred116$@localhost/rox'
db = SQLAlchemy(app)
from app import views

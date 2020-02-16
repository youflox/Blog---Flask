from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SECRET_KEY'] = '028456eecf014c7d03b208306f0fcea5'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flask_blog import routes

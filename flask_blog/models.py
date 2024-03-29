from datetime import datetime
from flask_blog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default = 'default.jpeg')
    password = db.Column(db.String(60), nullable= False)
    posts = db.relationship('Post', backref = 'author', lazy = True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable = False)
    date_posted = db.Column(db.DateTime, nullable  = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable =  False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

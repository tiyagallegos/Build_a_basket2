from . import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    posts = db.relationship('Post', backref='author', lazy=True)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_name = db.Column(db.String(60), nullable=False)
    total_members = db.Column(db.Integer, nullable=False)
    adults = db.Column(db.Integer, nullable=False)
    kids = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(20), nullable=False)
    needs = db.Column(db.Text, nullable=False)
    comments = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
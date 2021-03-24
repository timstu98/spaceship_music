from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
# from app import login

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    date = db.Column(db.DATE)

    # def __repr__(self):
    #     return f'{self.name} ({self.year_of_birth})'
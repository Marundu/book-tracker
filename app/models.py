from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):

    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(100), index=True, unique=True)
    username=db.Column(db.String(100), index=True, unique=True)
    password_hash=db.Column(db.String(128))
    about_me=db.Column(db.String(140))
    books=db.relationship('Book', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User: Username {0}, Email {1}'.format(self.username, self.email)

    def set_password(self, password):
        self.password_hash=generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Book(db.Model):

    __tablename__='books'

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100))
    author=db.Column(db.String(50))
    # category=db.Column(db.String(50))
    added_on=db.Column(db.DateTime, index=True, default=datetime.utcnow)
    done=db.Column(db.Boolean, default=False)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __init__(self, title, author, added_on, done, user_id):
        self.title=title
        self.author=author
        self.added_on=added_on
        self.done=done
        self.user_id=user_id

    def __repr__(self):
        # return '<Book: Title - {0}, Author - {1}, Category - {2}>'.format(self.title, self.author, self.category)
        return '<Book: Title - {0}, Author - {1}>'.format(self.title, self.author)

# class Category(db.Model):

    # __tablename__='categories'

#     id=db.Column(db.Integer, primary_key=True)
#     category=db.Column(db.String(30))
#     book_id=db.Column(db.Integer, db.ForeignKey('books.id'))
#     user_id=db.Column(db.Integer, db.ForeignKey('users.id'))

#     def __repr__(self):
#         return '<Category: {0}>'.format(self.category)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

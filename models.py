from app import db

class Book(db.Model):

    __tablename__='books'

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100))
    author=db.Column(db.String(50))
    done=db.Column(db.Boolean, default=False)
    category=db.Column(db.String(50))
    #  category_id=db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __init__(self, title, author, category, done):
        self.title=title
        self.author=author
        self.category=category
        self.done=False

    def __repr__(self):
        return '<Book: {0}>'.format(self.title)

# class Category(db.Model):

#     __tablename__='categories'

#     id=db.Column(db.Integer, primary_key=True)
#     category=db.Column(db.String(20))
#     books=db.relationship('Book', backref='category', lazy='dynamic')

#     def __init__(self, category):
#         self.category=category

#     def __repr__(self):
#         return '<Category: {0}>'.format(self.category)

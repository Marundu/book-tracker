from app import db

class Books(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    book_title=db.Column(db.String(100))
    author=db.Column(db.String(50))
    done=db.Column(db.Boolean, default=False)
    
    def __init__(self, book_title, author):
        self.book_title=book_title
        self.author=author
        self.done=False
    
    def __repr__(self):
        return '<Book: {0}>'.format(self.book_title)

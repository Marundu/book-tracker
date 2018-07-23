from app import db

class Book(db.Model):
  
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100))
    author=db.Column(db.String(50))
    category=db.Column(db.String(20))
    done=db.Column(db.Boolean, default=False)
    
    def __init__(self, title, author, category):
        self.title=title
        self.author=author
        self.category=category
        self.done=False
    
    def __repr__(self):
        return '<Book: {0}>'.format(self.title)

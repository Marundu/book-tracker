from app import db
from models import Book

# drop existing database tables

print 'Dropping existing database tables...'
db.drop_all() 

# create the database and the database tables

print 'Creating database tables...'
db.create_all() 

# insert book data

book1=Book('Book One', 'Author One', 'Category One')
book2=Book('Book Two', 'Author Two', 'Category Two')
book3=Book('Book Three', 'Author Three', 'Category Three')

# add users to db

print 'Inserting book data...'
db.session.add_all([book1, book2, book3])

# commit the changes
db.session.commit()

print 'Done!'

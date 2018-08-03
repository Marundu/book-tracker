from app import db
from models import Book#, Category

# drop existing database tables

print 'Dropping existing database tables...'
db.drop_all()

# create the database and the database tables

print 'Creating database tables...'
db.create_all()

# insert book data

# cat1=Category('Category One')
# cat2=Category('Category Two')
# cat3=Category('Category Three')

# title, author, category, done

book1=Book('Book One', 'Author One', 'Biography', False)
book2=Book('Book Two', 'Author Two', 'Fiction', True)
book3=Book('Book Three', 'Author Three', 'Essays', True)

# add books to db

print 'Inserting book data...'
db.session.add_all([book1, book2, book3])

# print 'Inserting category data...'
# db.session.add_all([cat1, cat2, cat3])

# commit the changes
db.session.commit()

print 'Done!'

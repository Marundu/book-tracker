from flask import request
from flask import render_template
from flask import redirect

from app import app, db
from models import Book

@app.route('/')
def books_list():
    books=Book.query.all()
    return render_template('list2.html', books=books)

@app.route('/book', methods=['POST'])
def add_book():
    title=request.form['title']
    author=request.form['author']
    category=request.form['category'] # drop down of preset categories
    done=False
    #if not title and not author and not category:
        #return 'Error'

    book=Book(title, author, category, done)

    db.session.add(book)
    db.session.commit()
    return redirect('/')

@app.route('/done/<int:book_id>')
def read_book(book_id):
    book=Book.query.get(book_id)

    if not book:
        return redirect('/')
    if book.done:
        book.done=False
    else:
        book.done=True

    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    book=Book.query.get(book_id)
    if not book:
        return redirect('/')

    db.session.delete(book)
    db.session.commit()
    return redirect('/')

@app.route('/add_category', methods=['POST'])
def add_category():
    category=request.form['category']
    category=Category(category)

    db.session.add(category)
    db.session.commit()

    return redirect('/')

@app.route('/categories')
def view_categories(category_id):
    categories=Category.query.all()

    return render_template('categories.html', categories=categories)

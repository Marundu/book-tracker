from flask import request
from flask import render_template
from flask import redirect

from app import app, db
from models import Books

@app.route('/')
def books_list():
    books=Books.query.all()
    return render_template('list.html', books=books)

@app.route('/book', methods=['POST'])
def add_book():
    book_title=request.form['book_title']
    author=request.form['author']
    if not book_title and not author:
        return 'Error'
    
    book=Books(book_title, author)
    
    db.session.add(book)
    db.session.commit()
    return redirect('/')

@app.route('/done/<int:book_id>')
def read_book(book_id):
    book=Books.query.get(book_id)
    
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
    book=Books.query.get(book_id)
    if not book:
        return redirect('/')
    
    db.session.delete(book)
    db.session.commit()
    return redirect('/')

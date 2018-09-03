from app import app, db
from app.forms import EditProfileForm, RegisterForm, LoginForm
from app.models import Book, User

from datetime import datetime

from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import current_user, login_user, login_required, logout_user

from werkzeug.urls import url_parse

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
@login_required
def books():
    books=Book.query.all()
    return render_template('books.html', books=books)

@app.route('/add_book', methods=['POST'])
@login_required
def add_book():
    title=request.form['title']
    author=request.form['author']
    category=request.form['category'] # drop down of preset categories
    added_on=datetime.utcnow()
    done=False
    #if not title and not author and not category:
        #return 'Error'

    book=Book(title, author, category, added_on, done)

    db.session.add(book)
    db.session.commit()
    return redirect(url_for('books'))

@app.route('/done/<int:book_id>')
@login_required
def read_book(book_id):
    book=Book.query.get(book_id)

    if not book:
        return redirect('/')
    if book.done:
        book.done=False
    else:
        book.done=True

    db.session.commit()
    return redirect(url_for('books'))

@app.route('/delete/<int:book_id>')
@login_required
def delete_book(book_id):
    book=Book.query.get(book_id)
    if not book:
        return redirect('/')

    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('books'))

# @app.route('/add_category', methods=['POST'])
# @login_required
# def add_category():
#     category=request.form['category']
#     category=Category(category)

#     db.session.add(category)
#     db.session.commit()

#     return redirect(url_for('books'))

# @app.route('/categories')
# @login_required
# def view_categories(category_id):
#     categories=Category.query.all()

#     return render_template('categories.html', categories=categories)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('books'))
    form=RegisterForm()
    if form.validate_on_submit():
        new_user=User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()

        flash('Karibu, reader!')

        #login_user(new_user)
        return redirect(url_for('books'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('books'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Incorrect credentials')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page=url_for('books')
        return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Until the next time, reader!')
    return redirect(url_for('index'))

@app.route('/user_profile')
@login_required
def user_profile():
    return render_template('user_profile.html')

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form=EditProfileForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.about_me=form.about_me.data
        db.session.commit()
        flash('Your changes have been saved!')
        return redirect(url_for('user_profile'))

    elif request.method=='GET':
        form.username.data=current_user.username
        form.about_me.data=current_user.about_me
    return render_template('edit_profile.html', form=form)

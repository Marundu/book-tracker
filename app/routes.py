from app import app, db

from app.forms import (
    BookForm, 
    CategoryForm, 
    EditBookForm, 
    EditProfileForm, 
    RegisterForm, 
    LoginForm,
)

from app.models import Book, User, Category

from datetime import datetime

from flask import (
    flash, 
    redirect, 
    render_template,
    request,
    url_for,
)

from flask_login import (
    current_user, 
    login_user, 
    login_required, 
    logout_user, 
)

from werkzeug.urls import url_parse


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
@login_required
def books():
    page=request.args.get('page', 1, type=int)
    
    books=Book.query.filter_by(user_id=current_user.id).paginate(
        page, app.config['BOOKS_PER_PAGE'], False)
    
    next_url=url_for('books', page=books.next_num) \
        if books.has_next else None
    
    prev_url=url_for('books', page=books.prev_num) \
        if books.has_prev else None    
    
    return render_template('books.html', books=books.items, next_url=next_url, prev_url=prev_url)


@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    form=BookForm()
    if request.method=='POST':
        book=Book(
            title=form.title.data,
            author=form.author.data,
            category=form.category.data, # categories.QuerySelect Something Something Logic,
            user_id=current_user.id
            )

        db.session.add(book)
        db.session.commit()
        flash('Book added!', 'success')
        return redirect(url_for('books'))
    else:
        # flash('ERROR. The book was not added.', 'error')
        flash('ERROR. The book was not added.') # This logic needs work

    return render_template('add_book.html', form=form)


@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    form=EditBookForm()
    book=Book.query.get(book_id)
    if request.method=='POST':
        book.title=form.title.data
        book.author=form.author.data
        db.session.commit()
        flash('Your changes have been saved!', 'info')
        return redirect(url_for('books'))

    elif request.method=='GET':
        form.title.data=book.title
        form.author.data=book.author
    return render_template('edit_book.html', form=form)  


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
        flash('Book read!', 'success')

    db.session.commit()
    return redirect(url_for('books'))


@app.route('/delete_book/<int:book_id>')
@login_required
def delete_book(book_id):
    book=Book.query.get(book_id)
    if not book:
        return redirect('/')

    db.session.delete(book)
    db.session.commit()
    flash('Book deleted!', 'info')

    return redirect(url_for('books'))


@app.route('/categories')
@login_required
def categories():
    # categories=Category.query.all(user_id=current_user.id)
    categories=Category.query.all()
    return render_template('categories.html', categories=categories)


@app.route('/add_category', methods=['GET', 'POST'])
@login_required
def add_category():
    form=CategoryForm()
    if form.validate_on_submit():
        category=Category(
            category=((form.category.data).lower()).capitalize(),
            user_id=current_user.id
            )
        # category=(category.lower()).capitalize()
        db.session.add(category)
        sb.session.commit()
        flash('Category added!', 'info')

        return redirect(url_for('categories'))

    return render_template('categories.html', categories=categories, form=form)


@app.route('/delete_category/<int:category_id>', methods=['GET', 'POST'])
@login_required
def delete_category(category_id):
    category=Category.query.get(category_id, user_id=current_user.id)
    if not category:
        return redirect('/categories')

    db.session.delete(category)
    db.session.commit()
    flash('Category deleted!', 'info')

    return redirect(url_for('categories'))


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

        flash('Karibu, reader!', 'success')

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
            flash('Incorrect username or password!', 'error')
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
    flash('Until the next time, reader!', 'info')
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
        flash('Your changes have been saved!', 'info')
        return redirect(url_for('user_profile'))

    elif request.method=='GET':
        form.username.data=current_user.username
        form.about_me.data=current_user.about_me
    return render_template('edit_profile.html', form=form)


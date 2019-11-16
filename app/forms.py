from datetime import datetime
from flask_wtf import FlaskForm

from wtforms import (
    BooleanField, 
    PasswordField, 
    StringField, 
    SubmitField, 
    TextAreaField,
) 

from wtforms.validators import (
    DataRequired, 
    Email, 
    EqualTo, 
    Length,
) 

from wtforms.ext.sqlalchemy.fields import QuerySelectField

from app.models import User


class RegisterForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired(), Email()])
    username=StringField('Username', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=8, max=40)])
    confirm=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Register')

    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please pick a different username.')

    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please pick a different email address.')


class LoginForm(FlaskForm):
    # email=StringField('Email', validators=[DataRequired(), Email()])
    username=StringField('Username', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    remember_me=BooleanField('Remember Me?')


class EmailForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired(), Email(), Length(min=8, max=40)])


class PasswordForm(FlaskForm):
    password=PasswordField('Password', validators=[DataRequired()])
    confirm=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


class EditProfileForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired()])
    about_me=TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit=SubmitField('Submit')


class BookForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    author=StringField('Author', validators=[DataRequired()])
    #category=StringField('Category', validators=[DataRequired()])
    category=QuerySelectField('Category', allow_blank=True)#, validators=[DataRequired()])
    added_on=StringField('Added On', validators=[DataRequired()], default=datetime.utcnow())
    done=BooleanField('Done?', validators=[DataRequired()], default=False)
    submit=SubmitField('Add Book')


class EditBookForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    author=StringField('Author', validators=[DataRequired()])
    submit=SubmitField('Edit Book')


class CategoryForm(FlaskForm):
    category=StringField('Category', validators=[DataRequired()])
    submit=SubmitField('Add Category')


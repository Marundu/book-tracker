from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired(), Email(), Length(min=8, max=40)])
    username=StringField('Username', validators=[DataRequired(), Length(min=8, max=40)])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=8, max=40)])
    confirm=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

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

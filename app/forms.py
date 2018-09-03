from app.models import User
from flask_wtf import Form
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(Form):
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

class LoginForm(Form):
    # email=StringField('Email', validators=[DataRequired(), Email()])
    username=StringField('Username', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    remember_me=BooleanField('Remember Me?')

class EmailForm(Form):
    email=StringField('Email', validators=[DataRequired(), Email(), Length(min=8, max=40)])

class PasswordForm(Form):
    password=PasswordField('Password', validators=[DataRequired()])
    confirm=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

class EditProfileForm(Form):
    username=StringField('Username', validators=[DataRequired()])
    about_me=TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit=SubmitField('Submit')

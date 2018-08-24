import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG=True
    APPLICATION_DIR=os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'books.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.environ.get('SECRET_KEY') or '6&p>(x)im84varwt2<l0'

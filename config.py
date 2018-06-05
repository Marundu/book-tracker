import os

class Config(object):
    DEBUG=True
    APPLICATION_DIR=os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI='sqlite:///{0}/books.db'.format(APPLICATION_DIR)
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.urandom(30)

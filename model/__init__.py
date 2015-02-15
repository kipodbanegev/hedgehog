from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
from flask import url_for

from hashids import Hashids
hashids = None

def decodehash(hash):
    return hashids.decode(hash)

db = SQLAlchemy()
app = None

def inithash(salt):
    global hashids
    hashids = Hashids(salt, min_length=11)

def init():
    db.init_app(app)

def create_db():
    with app.app_context():
	db.create_all()
	db.session.commit()
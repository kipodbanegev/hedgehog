from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required

db = SQLAlchemy()
app = None

def init():
    db.init_app(app)

def create_db():
    with app.app_context():
	db.create_all()
	db.session.commit()
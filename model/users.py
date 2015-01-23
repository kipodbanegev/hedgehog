from flask.ext.login import LoginManager
from datetime import datetime
from model import *

class Role(db.Entity, RoleMixin):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 80, unique=True)
    description = Optional(str, 255)
    users = Set("User")

class User(db.Entity, UserMixin):
    id = PrimaryKey(int, auto=True)
    email = Required(str, 255, unique=True)
    password = Required(str, 255)
    active = Required(bool, default=False)
    confirmed_at = Required(datetime, default=lambda: datetime.now())
    roles = Set(Role)

# Flask-Login
login_manager = LoginManager()
# Flas-Security
user_datastore = PonyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

def init(app):
    # Flask-Login
    login_manager.init_app(app)

def create(email, password):
    with db_session:
	user_datastore.create_user(email=email, password=password)
	commit()

@login_manager.user_loader
def load_user(userid):
    with db_session:
	return User.get(id=userid)
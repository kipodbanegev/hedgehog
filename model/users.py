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

user_datastore = PonyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
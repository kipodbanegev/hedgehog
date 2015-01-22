from pony.orm import *
from flask.ext.security import Security, PonyUserDatastore, \
    UserMixin, RoleMixin, login_required

app = None

db = Database()

def connect(a, host, user, password, dbname):
    app = a
    db.bind("postgres", host=host, user=user, password=password, database=dbname)
    #sql_debug(True)
    db.generate_mapping(create_tables=True)


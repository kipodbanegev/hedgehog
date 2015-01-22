from model import *

class Event(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    authorized = Required(bool, default=False)

def insert(name):
    with db_session:
        e = Event(name = name)
        commit()
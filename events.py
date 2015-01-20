from pony.orm import *

db = Database()

def connect(host, user, password, dbname):
    db.bind("postgres", host=host, user=user, password=password, database=dbname)
    sql_debug(True)
    db.generate_mapping(create_tables=True)

class Event(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    authorized = Required(bool, default=False)

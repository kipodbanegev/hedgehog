from model import *

class Event(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name        = db.Column(db.String(80))
    description = db.Column(db.String(255))
    place       = db.Column(db.String(255))
    date        = db.Column(db.DateTime())

def insert(name, description, place, date):
    event = Event(name=name, description=description, place=place, date=date)
    dbsession = db.session()
    dbsession.add(event)
    dbsession.commit()
    pass
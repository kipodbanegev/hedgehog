from model import *
from datetime import datetime
from users import User

# Define models
events_places = db.Table('events_places',
    db.Column('event_id', db.Integer(), db.ForeignKey('event.id')),
    db.Column('place_id', db.Integer(), db.ForeignKey('place.id')))

class Place(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name        = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))

class Event(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name        = db.Column(db.String(80))
    description = db.Column(db.String(255))
    place       = db.relationship('Place', secondary=events_places,
    		    backref=db.backref('Events'))
    date        = db.Column(db.DateTime())
    user_id = db.deferred(db.Column(db.Integer, db.ForeignKey(User.id), nullable=False))

def insert(name, description, place, date):
    dbsession = db.session()

    # convert 14/02/2015 14:15
    print date
    date = datetime.strptime(date, '%d/%m/%Y %H:%M')

    if not dbsession.query(db.exists().where(Place.name==place)).scalar():
        # add place
	place = Place(name=place)
        dbsession.add(place)
        dbsession.commit()
    else:
	place = Place.query.filter_by(name=place).first()
	#place = dbsession.query(Place).filter(name=place).first()

    # add event
    event = Event(
	name=name,
	description=description,
	place=[place],
	date=date,
	user_id = current_user.id
    )
    dbsession.add(event)
    dbsession.commit()
    pass
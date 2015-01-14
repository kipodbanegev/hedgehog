class event:
    # event name as string
    name = ""
    # event place as string
    place = ""
    # date in datetime
    date  = None
    # original representation of the date in unicode
    datestr = ""

import psycopg2

conn = None
cur = None

def connect(host, user, password, dbname):
    try:
	global conn, cur
	conn = psycopg2.connect("dbname='"+dbname+"' user='"+user+"' host='"+host+"' password='"+password+"'")
	cur = conn.cursor()
    except:
        print "I am unable to connect to the database"

def disconnect():
    cur.close()
    conn.close()

def insert(e):
    cur.execute("""INSERT INTO events (event_name) VALUES ('%s');""" % e.name)
    # Make the changes to the database persistent
    conn.commit()

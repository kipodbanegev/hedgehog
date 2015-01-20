#!/usr/bin/env python
import os
from datetime import datetime

# flask
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

# jinja2
import jinja2

# ConfigParser
import ConfigParser, os

# Pony
from pony.orm import *

# local events managment library
import events

# home view
@app.route("/")
def home():
    return render_template('index.min.html', active='home')

# About view
@app.route("/about")
def about():
    return render_template('about.min.html', active='about')

# Submit event view
@app.route("/event/submit/", methods=['GET', 'POST'])
def submit_event():
    if request.method == 'GET':
    	return render_template('submit_event.min.html')
    if request.method == 'POST':
	name    = request.form['event_name']
	with db_session:
	    e = events.Event(name = name)	
	    commit()
	#e.place   = request.form['event_place']
	#e.datestr    = request.form['event_date']
	#e.date    = datetime.strptime(request.form['event_date'], '%d/%m/%Y %H:%M')
	return '<html><body>thank you! <strong style="color:red;">' + str(e.name) + '</strong> had been added and waiting for approval. click <a href="/">here</a> to return to the kipod site.</body></html>'

# main
if __name__ == "__main__":
    # load config file
    config = ConfigParser.ConfigParser()
    config.read('site.cfg')
    dbhost = config.get('Database', 'host', 0)
    dbuser = config.get('Database', 'user', 0)
    dbpass = config.get('Database', 'password', 0)
    dbname = config.get('Database', 'dbname', 0)
    events.connect(dbhost, dbuser, dbpass, dbname)

    hhfolder = os.path.dirname(os.path.abspath(__file__))
    # Custom jinja2 folder (Default - templates)
    my_loader = jinja2.ChoiceLoader([
	app.jinja_loader,
	jinja2.FileSystemLoader([hhfolder+'/build',]),
    ])
    app.jinja_loader = my_loader
    # If you enable debug support the server will reload itself on code changes, 
    # and it will also provide you with a helpful debugger if things go wrong.
    app.debug = True
    # start server
    app.run(host='0.0.0.0')

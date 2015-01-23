#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from datetime import datetime

# flask
from flask import Flask, render_template, url_for, request, redirect, abort
app = Flask(__name__)

# jinja2
import jinja2

# ConfigParser
import ConfigParser, os
# load config file
config = ConfigParser.ConfigParser()
config.read('site.cfg')
dbhost = config.get('Database', 'host', 0)
dbuser = config.get('Database', 'user', 0)
dbpass = config.get('Database', 'password', 0)
dbname = config.get('Database', 'dbname', 0)
secret_key = config.get('Session', 'secret_key', '')
if secret_key=='':
    sys.exit("Empty secrey_key in site.cfg")
app.secret_key = secret_key

# local events managment library
import model
from model import events, users

# pony
from pony.orm import *

# Flask-Login
from flask.ext.login import LoginManager, login_user, logout_user
model.connect(app, dbhost, dbuser, dbpass, dbname)

# Flask-Security
from flask.ext.security import Security, current_user, login_required
users.init(app)

# Flask-WTF
from flask_wtf import Form
from wtforms import TextField, PasswordField, validators
from wtforms.validators import Required

# home view
@app.route("/")
def home():
    return render_template('index.min.html', active='home')

# About view
@app.route("/about")
def about():
    return render_template('about.min.html', active='about')

class LoginForm(Form):
    email = TextField('email', [validators.Required()])
    password = PasswordField('password', [validators.Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        user = users.User.get(email=self.email.data)
        if user is None:
            self.email.errors.append(u'משתמש לא קיים')
            return False
        #if not user.check_password(self.password.data):
        #    self.password.errors.append('משתמש וססמה לא מתאימים')
        #    return False
        self.user = user
        return True

#@users.login_manager.user_loader
@app.route("/user/create/", methods=['GET', 'POST'])
def user_create():
    # redirect home if already authenticated
    if current_user.is_authenticated():
	return redirect(url_for('home'))
    if request.method == 'GET':
        # return user_create.html page
	return render_template('user_create.min.html')
    if request.method == 'POST':
	email    = request.form['email']
	password    = request.form['password']
	with db_session:
	    # check if user exist
	    user = users.User.get(email=email)
	    if not user is None:
		url = url_for("login")
		next = request.args.get("next") or ''
		if next!='':
		    url = url + u"?next="+next
		error = u"כתובת דואר אלקטרוני זו כבר בשימוש. <a href='"+url+u"'>התחבר</a>"
	        return render_template('user_create.min.html', error=error)
	    # create user and fetch it
	    users.create(email, password)
	    user = users.User.get(email=email)
    	    # login and validate the user...
    	    login_user(user)
        return redirect(request.args.get("next") or url_for("home"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
	return render_template('login.min.html', next=request.args.get("next") or '', active="login")
    email    = request.form['email']
    password    = request.form['password']
    next = request.form['next'] or ''
    with db_session:
        # check if user exist
        user = users.User.get(email=email)
        if user is None:
            return render_template('login.min.html', error=u"כתובת דואר זו אינה רשומה במערכת", next=next)
	if user.password == password:
	    # everything ok
	    login_user(user)
    	    return redirect(next or url_for("home"))
    return render_template('login.min.html', error=u"ההתחברות נכשלה", next=next)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

# Submit event view
#@users.login_manager.user_loader
@db_session
@app.route("/event/submit/", methods=['GET', 'POST'])
def submit_event():
    if request.method == 'GET':
	if not current_user.is_authenticated():
	    return redirect(url_for('user_create')+"?next="+url_for('submit_event'))
    	return render_template('submit_event.min.html')
    if request.method == 'POST':
	name    = request.form['event_name']
	events.insert(name)
	#e.place   = request.form['event_place']
	#e.datestr    = request.form['event_date']
	#e.date    = datetime.strptime(request.form['event_date'], '%d/%m/%Y %H:%M')
	return '<html><body>thank you! <strong style="color:red;">' + str(name) + '</strong> had been added and waiting for approval. click <a href="/">here</a> to return to the kipod site.</body></html>'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.min.html')

# main
if __name__ == "__main__":
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

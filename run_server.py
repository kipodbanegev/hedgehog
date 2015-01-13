#!/usr/bin/env python
import os
from flask import Flask, render_template, url_for
import jinja2
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.min.html', active='home')

@app.route("/about")
def about():
    return render_template('about.min.html', active='about')

@app.route("/event/submit/")
def submit_event():
    return render_template('submit_event.min.html')

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
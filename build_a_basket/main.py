#this file will handle CRUD operations
from flask import Blueprint, render_template, url_for

#first init the main file as part of flask app
main = Blueprint('main', __name__)
#blueprint way to org files in flask all function will be accessed
#thru blueprint thru main i.e. main.index, etc

#need decorator for all flask functions
#overwrites functionality for app

@main.route('/')
def index(): 
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')

@main.route('/about')
def about():
    return render_template('about.html')

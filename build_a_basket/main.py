#this file will handle CRUD operations
from flask import Blueprint, render_template

#first init the main file as part of flask app
main = Blueprint('main', __name__)
#blueprint way to org files in flask all function will be accessed
#thru blueprint thru main i.e. main.index, etc

#need decorator for all flask functions
#overwrites functionality for app

@main.route('/')
def index(): 
    return 'Build a Basket!'

@main.route('/profile')
def profile():
    return 'View all your posts here!'

@main.route('/about')
def about():
    return 'About Build-A-Basket!'

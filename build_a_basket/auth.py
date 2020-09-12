#this file will handle auth
from flask import Blueprint, render_template, url_for

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.rout('/signup', methods=['POST']) #get is default
def signup_post():
    

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return 'See you next time'
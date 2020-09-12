#this file will handle auth
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return 'Signup New user!'

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/logout')
def logout():
    return 'See you next time'
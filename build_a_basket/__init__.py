#initial file that runs
from flask import Flask

#basic structure of how to create an app 
#only single instances go in init.py i.e. db, app creation etc
def create_app():
    app = Flask(__name__)

    return app




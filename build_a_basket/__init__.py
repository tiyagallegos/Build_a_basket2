#how to run the app FLASK_APP=build_a_basket auto look for create and 
#initial file that runs on the command flask run
from flask import Flask

#basic structure of how to create an instatnce of flask app 
#only single instances go in init.py i.e. db, app creation etc
def create_app():
    app = Flask(__name__)

#import instance (main/crud) of the blueprint, and register it
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


#import instance (auth) of the blueprint, and register it
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app




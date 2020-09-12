#how to run the app FLASK_APP=build_a_basket auto look for create and 
#initial file that runs on the command flask run
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()

#basic structure of how to create an instatnce of flask app 
#only single instances go in init.py i.e. db, app creation etc
def create_app():
    app = Flask(__name__)

    migrate = Migrate(app, db)
#config app
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

#initialize the app
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
#flask login will know how to find specific user
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
#import instance (auth) of the blueprint, and register it
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

#import instance (main/crud) of the blueprint, and register it
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app




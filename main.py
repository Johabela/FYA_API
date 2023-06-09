from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



db = SQLAlchemy()
ma = Marshmallow()


def create_app():
     #initialize app
    app = Flask(__name__)
   
    app.config.from_object("config.app_config")

    #initialize the app and Marshmallow 
    db.init_app(app)
    ma.init_app(app)


    from command.db import db_cmd
    app.register_blueprint (db_cmd)

    from controller import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint (controller)
   

    return app 



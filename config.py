import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @property # creates and get and setter method for the property 
    def SQLALCHEMY_DATABASE_URI(self):
        db_url = os.environ.get("DATABASE_URL")

        if not db_url:
            raise ValueError("DATABASE_URL is not set") #-> 

        return db_url

class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    pass


environment = os.environ.get("FLASK_DEBUG")

if environment:
    app_config = DevelopmentConfig() # -> connecting from Main to app configuration on config.py 
else:
    app_config = ProductionConfig()
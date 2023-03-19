from main import db
from flask import Blueprint
from model.studio import Studio
from model.artist import Artist 
from model.style import Style
from model.artist_style import ArtistStyle

db_cmd = Blueprint("db", __name__)



#CLI Commands 
@db_cmd.cli.command('create')
def create_db():
    db.create_all()
    print ('Tables are created')

@db_cmd.cli.command('drop')
def drop_db():
    db.drop_all()
    print ('Tables are dropped')


#Pending to create seed command and finish to create the table Location  

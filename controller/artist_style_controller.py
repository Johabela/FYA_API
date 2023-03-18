# artist and studio fk will be in this table 
# User can only see relevant information , artist name, styles and year of practicing 

# only relevant information 



from flask import Blueprint, request
from model.artist_style import ArtistStyle
from schema.artist_styles_schema import artist_style_schema, artist_styles_schema
from model.artist import Artist
from main import db

bp_artist_style = Blueprint('artist_style', __name__, url_prefix="/artist_styles")

@bp_artist_style.route("/", methods=["GET"])
def get_artist_styles():
    artist_styles = ArtistStyle.query.all()
    return artist_styles_schema.dump(artist_styles)


@bp_artist_style.route("/<int:id>", methods=["GET"])
def get_artist_style(id):
    artist_style = ArtistStyle.query.get(id)

    if not artist_style:
        return { "message":" The artist doesn't have any styles"}

    return artist_style_schema.dump(artist_style)


@bp_artist_style.route("/", methods=["POST"])
def create_artist_style():

    # try: 
    artist_style_fields = artist_style_schema.load(request.json)
    artist_style = ArtistStyle(**artist_style_fields)

    db.session.add(artist_style)
    db.session.commit()
    
    # except: 
    #     return {"message": " This style already exists " }
 
# #  try: 
#     artist_style_fields = artist_style_schema(request.json)

# # User can only see relevant information , artist name, styles and year of practicing 

#     #Search artist information 
#     artist = Artist.query.get(artist_style_fields["artist_id"])

#     #match primary key 
#     if artist ==  artist_style_fields ["artist_style_id"]:
#      return {"message": "You cannot see the information"}

    
#     # artist_style_fields = artist_style_schema.load(request.json)
#     # artist_style = ArtistStyle(**artist_style_fields)

#     db.session.add(artist_style)
#     db.session.commit()
    
#  except: 
#       return {"message": " You are missing information  " }
    
    return artist_style_schema.dump(artist_style)



        
  

    
    
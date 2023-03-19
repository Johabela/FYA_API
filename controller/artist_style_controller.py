from flask import Blueprint, request
from model.artist_style import ArtistStyle
from schema.artist_styles_schema import artist_style_schema, artist_styles_schema
from model.artist import Artist
from main import db

bp_artist_style = Blueprint('artist_style', __name__, url_prefix="/artist_styles")


# The GET routes endpoint
@bp_artist_style.route("/", methods=["GET"])
def get_artist_styles():
    artist_styles = ArtistStyle.query.all()

    return artist_styles_schema.dump(artist_styles)


@bp_artist_style.route("/<int:id>", methods=["GET"])
def get_artist_style(id):
    artist_style = ArtistStyle.query.get(id)

    # handling error 
    if not artist_style:
        return { "message":" The artist doesn't have any styles"}

    return artist_style_schema.dump(artist_style)

# The POST route endpoint
@bp_artist_style.route("/", methods=["POST"])
def create_artist_style():

    try: 
        artist_style_fields = artist_style_schema.load(request.json)
        artist_style = ArtistStyle(**artist_style_fields)

        db.session.add(artist_style)
        db.session.commit()

    # handling error 
    except: 
        return {"message": " The style already exists " }
 
    
    return artist_style_schema.dump(artist_style)




    
    
from flask import Blueprint, request
from model.artist import Artist
from model.studio import Studio
from schema.artists_schema import artist_schema, artists_schema
from main import db


bp_artist = Blueprint('artist', __name__, url_prefix="/artists")

@bp_artist.route("/", methods=["GET"])
def get_artists():
    artists = Artist.query.all()
    return artists_schema.dump(artists)


@bp_artist.route("/<int:id>", methods=["GET"])
def get_artist(id):
    artist = Artist.query.get(id)

    if not artist:
        return { "message":" Wrong Route "}

    return artist_schema.dump(artist)


@bp_artist.route("/", methods=["POST"])
def create_artist():
    # try: 
    artist_fields = artist_schema.load(request.json)
    artist = Artist(**artist_fields) 


    db.session.add(artist)
    db.session.commit()
    # except: 
    #     return {"message": " This artist already exists " }
    
    return artist_schema.dump(artist)



        
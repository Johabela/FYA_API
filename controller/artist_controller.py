from flask import Blueprint, request
from model.artist import Artist_Model
from schema.artists_schema import artist_schema, artists_schema
from main import db

blue_print_artist = Blueprint('artist', __name__, url_prefix="/artists")

@blue_print_artist.route("/", methods=["GET"])
def get_artists():
    artists = Artist_Model.query.all()
    return artists_schema.dump(artists)



@blue_print_artist.route("/<int:id>", methods=["GET"])
def get_artist(id):
    artist = Artist_Model.query.get(id)

    if not artist:
        return { "message":" Wrong Route "}

    return artist_schema.dump(artist)


@blue_print_artist.route("/", methods=["POST"])
def create_artist():
    # try: 
    artist_fields = artist_schema.load(request.json)
    artist = Artist_Model(**artist_fields) 
    studio = artist_fields["studio_id"]
    # artist = Artist_Model(
    #     artist_name=artist_fields["artist name"],
    #     verified = artist_fields["verified"],
    #     description = artist_fields["description"],
    #     work_agreement = artist_fields["work_agreement"],        
    #     url_instagram = artist_fields ["url_ instagram"],
    #     studio_id = artist_fields["studio_id"],
    # )

    # artist.studio_id = artist_fields ["studio_id"]
    db.session.add(artist)
    db.session.commit()
    # except: 
    #     return {"message": " This artist already exists " }
    
    return artist_schema.dump(artist)



        

    
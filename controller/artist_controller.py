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
    
    # artists_data =[]

    # # fix this !!! 

    # for artists in artists:
    #     artists_data = {
    #          "id": artists.id,
    #          "name": artists.artist_name,
    #          "url_instagram": artists.url_instagram, 
    #          "studio" : artists.studio.studio_name 
    #     }

        # artists_data.append(artists_data)

   

  


@bp_artist.route("/<int:id>", methods=["GET"])
def get_artist(id):
    artist = Artist.query.get(id)
    artist_data =[]


    artist_data = {
            "id": artist.id,
            "name": artist.artist_name,
             "description": artist.description,
            "url_instagram": artist.url_instagram, 
            "studio" : artist.studio.studio_name 
    }

        # if not artist:
        #  return { "message":" Wrong Route "}
        
    return (artist_data)


    # someData = {}
    # someData.artistName = artist.name
    return artist_schema.dump(artist)
    # return someData


@bp_artist.route("/", methods=["POST"])
def create_artist():
    try: 
        artist_fields = artist_schema.load(request.json)
        artist = Artist(**artist_fields) 


        db.session.add(artist)
        db.session.commit()
    except: 
        return {"message": " This artist already exists " }
    
    return artist_schema.dump(artist)



        
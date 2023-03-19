from flask import Blueprint, request, json , jsonify
from model.studio import Studio
from model.artist import Artist 
from schema.studios_schema import studio_schema, studios_schema
from main import db

bp_studio = Blueprint('studio', __name__, url_prefix="/studios")

# The GET routes endpoint
@bp_studio.route("/", methods=["GET"]) 
def get_studios():
    studios = Studio.query.all()
    
    return studios_schema.dump(studios)


@bp_studio.route("/<int:id>", methods=["GET"])
def get_studio(id):
    studio = Studio.query.get(id)

    # handling error 
    if not studio:
        return { "message":" Wrong Route "}

    return studio_schema.dump(studio)

# The POST routes endpoint
@bp_studio.route("/", methods=["POST"])
def create_studio():
    try: 
        studio_fields = studio_schema.load(request.json)
        studio = Studio(**studio_fields)

        db.session.add(studio)
        db.session.commit()
    
    # handling error 
    except: 
        return {"message": " The studio already exists " }
    
    return studio_schema.dump(studio)


        
  

    
    
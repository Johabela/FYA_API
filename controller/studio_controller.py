from flask import Blueprint, request, json, jsonify
from model.studio import Studio_Model
from schema.studios_schema import studio_schema, studios_schema
from main import db

blue_print_studio = Blueprint('studio', __name__, url_prefix="/studios")

@blue_print_studio.route("/", methods=["GET"])
def get_studios():
    studios= Studio_Model.query.all()
    return studios_schema.dump(studios)


@blue_print_studio.route("/<int:id>", methods=["GET"])
def get_studio(id):
    studio = Studio_Model.query.get(id)

    if not studio:
        return { "message":" Wrong Route "}

    return studio_schema.dump(studio)


@blue_print_studio.route("/", methods=["POST"])
def create_studio():
    try: 
        studio_fields = studio_schema.load(request.json)
        studio = Studio_Model(**studio_fields)

        db.session.add(studio)
        db.session.commit()
        
    except: 
        return {"message": " This studio already exists " }
    
    return studio_schema.dump(studio)



        
  

    
    
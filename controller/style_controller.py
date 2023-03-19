from flask import Blueprint, request, json, jsonify
from model.style import Style
from model.artist_style import ArtistStyle
from schema.artist_styles_schema import artist_styles_schema, artist_style_schema
from schema.styles_schema import style_schema, styles_schema
from main import db

bp_style = Blueprint('style', __name__, url_prefix="/styles")


# The GET routes endpoint
@bp_style.route("/", methods=["GET"])
def get_styles():
    styles= Style.query.all()
    return styles_schema.dump(styles)


@bp_style.route("/<int:id>", methods=["GET"])
def get_style(id):
    style = Style.query.get(id)


    # handling error 
    if not style:
        return {"message":" Wrong Route"}

    return style_schema.dump(style)

# The POST routes endpoint

@bp_style.route("/", methods=["POST"])
def create_style():

    # try: 
    style_fields = style_schema.load(request.json)
    style = Style(**style_fields)

    db.session.add(style)
    db.session.commit()

    # handling error 
    # except: 
    #     return {"message": "The style already exists"}
    
    return style_schema.dump(style)



        
  

    
    
from flask import Blueprint, request, json, jsonify
from model.style import Style
from schema.styles_schema import style_schema, styles_schema
from main import db

bp_style = Blueprint('style', __name__, url_prefix="/styles")

@bp_style.route("/", methods=["GET"])
def get_styles():
    styles= Style.query.all()
    return styles_schema.dump(styles)


@bp_style.route("/<int:style_id>", methods=["GET"])
def get_style(style_id):
    style = Style.query.get(style_id)

    if not style:
        return { "message":" Wrong Route "}

    return style_schema.dump(style)


@bp_style.route("/", methods=["POST"])
def create_style():
    try: 
        style_fields = style_schema.load(request.json)
        style = Style(**style_fields)

        db.session.add(style)
        db.session.commit()
    
    except: 
        return {"message": " This style already exists " }
    
    return style_schema.dump(style)



        
  

    
    
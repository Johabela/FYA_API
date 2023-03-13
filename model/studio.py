
from main import db


class Studio_Model(db.Model):
    ___tablename__ = "studios"

    id = db.Column(db.Integer(), primary_key=True) 

    studio_name = db.Column(db.String(), nullable=False , unique=True)
    description = db.Column(db.String ())
    website = db.Column(db.String ())















    # artists = db.relationship("Artist_Model", backref="studios", lazy=True)

    # artists = db.relationship("Artist_Model", lazy ="select",
    #     backref = db.backref("studios", lazy="joined"))


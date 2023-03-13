
from main import db



class Artist_Model(db.Model):
    ___tablename__ = "artists" 

    id = db.Column(db.Integer(), primary_key=True) 

    artist_name = db.Column(db.String(), nullable=False, unique=True)
    verified = db.Column(db.Boolean())
    description = db.Column(db.String ())
    work_agreement = db.Column(db.String())
    url_instagram = db.Column(db.String ())
 

    studio_id = db.Column(db.Integer, db.ForeignKey("studios.id"), nullable= False)

    studio = db.relationship("Studio_Model", backref="artists")

from main import db



class Style(db.Model):
    ___tablename__ = "style"

    id = db.Column(db.Integer(), primary_key=True) 

    style_name = db.Column(db.String(), nullable=False , unique=True)
    description = db.Column(db.String ())

    # artist_style_id = db.Column(db.Integer, db.ForeignKey("artist_style.id"), nullable=False)

    # artist_style = db.relationship("ArtistStyle", backref="styles", lazy=True)

 
    # style = db.relationship("Style", backref="style", lazy=True)
    
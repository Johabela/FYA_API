
from main import db



class ArtistStyle(db.Model):
    ___tablename__ = "artist_style"

    id = db.Column(db.Integer(), primary_key=True) 

    years_of_practice = db.Column(db.Integer())
 

# Getting artist FK and styles FK

    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"), nullable=False)
    style_id = db.Column(db.Integer, db.ForeignKey("style.id"), nullable=False)





















  
    # artist = db.relationship("Artist", backref="artist_style")
    # style = db.relationship("Style", backref="artist_style")

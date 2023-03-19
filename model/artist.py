from main import db


class Artist(db.Model):
    ___tablename__ = "artists"  #-> Table name Artist 


    # Artist primary key 
    id = db.Column(db.Integer(), primary_key=True) 

    # Artist attributes 
    artist_name = db.Column(db.String(), nullable=False, unique=True)
    verified = db.Column(db.Boolean())
    description = db.Column(db.String ())
    work_agreement = db.Column(db.String())
    url_instagram = db.Column(db.String ())

    # Defining studio_if foreign key 
    studio_id = db.Column(db.Integer, db.ForeignKey("studio.id"), nullable=False)
  
    # Establish relationship between studio and artist 
    studio = db.relationship("Studio", backref="artists")

    # Establish relationship between artist_style and artist 
    artist_style = db.relationship("ArtistStyle", backref="artist")

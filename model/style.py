from main import db



class Style(db.Model):
    ___tablename__ = "styles" #-> Table name style 

    # Style primary key 
    id = db.Column(db.Integer(), primary_key=True) 

    # Style attributes 
    style_name = db.Column(db.String(), nullable=False , unique=True)
    description = db.Column(db.String ())


    # Establish relationship between artist_style and style 
    artist_style = db.relationship("ArtistStyle", backref="styles", lazy=True)

 
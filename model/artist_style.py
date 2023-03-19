from main import db



class ArtistStyle(db.Model):
    ___tablename__ = "artist_style" #-> Table name artist_style 


    # Artist_style primary key 
    id = db.Column(db.Integer(), primary_key=True) 

    # Artist_style attribute
    years_of_practice = db.Column(db.Integer())
 

    # Getting artist FK and styles FK
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"), nullable=False)
    style_id = db.Column(db.Integer, db.ForeignKey("style.id"), nullable=False)














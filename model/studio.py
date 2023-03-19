from main import db


class Studio(db.Model):
    ___tablename__ = "studios" #-> Table name Studio

    # Studio primary key 
    id = db.Column(db.Integer(), primary_key=True) 


    # Studio attributes 
    studio_name = db.Column(db.String(), nullable=False , unique=True)
    description = db.Column(db.String ())
    website = db.Column(db.String())

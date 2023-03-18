from main import db


class Studio(db.Model):
    ___tablename__ = "studios"

    id = db.Column(db.Integer(), primary_key=True) 

    studio_name = db.Column(db.String(), nullable=False , unique=True)
    description = db.Column(db.String ())
    website = db.Column(db.String())


    artist = db.relationship("Artist", backref="artist", lazy=True)


    # artist = db.relationship('Artist', backref="artist", lazy=True, uselist=False)






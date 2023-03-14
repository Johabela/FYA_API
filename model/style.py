
from main import db



class Style(db.Model):
    ___tablename__ = "style"

    style_id = db.Column(db.Integer(), primary_key=True) 

    style_name = db.Column(db.String(), nullable=False , unique=True)
    description = db.Column(db.String ())


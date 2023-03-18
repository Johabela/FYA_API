from main import ma 
from model.style import Style

# the code didn't have the below line, pay attention
from marshmallow import EXCLUDE



class StyleSchema(ma.Schema):
    class Meta: 
        fields = ("id", "style_name",  "description", "artist_style", "artist_style_id")

        load_only =["artist_style_id"]
    
    artist_style = ma.Nested("ArtistStyleSchema")

style_schema = StyleSchema()
styles_schema = StyleSchema(many=True)



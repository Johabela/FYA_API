from main import ma 



class StudioSchema(ma.Schema):
    class Meta: 
        fields = ("id", "studio_name", "description", 
                  "website", "artist")


    artist = ma.List(ma.Nested("ArtistSchema", exclude=("studio",)))

studio_schema = StudioSchema()
studios_schema = StudioSchema(many=True)





















# from marshmallow import fields

# the code didn't have the below line, pay attention
# from marshmallow import EXCLUDE
  
    
    # artist = ma.List(ma.Nested("Artist_Schema", exclude=("description",)))
    # artist =fields.Nested("ArtistSchema")
        
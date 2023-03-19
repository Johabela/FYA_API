from main import ma 


#creating the Schema with Marshmallow 
class StudioSchema(ma.Schema):
    class Meta: 
        fields = ("id", "studio_name", "description", 
                  "website", "artist")
        
    load_only = ["studio_id"]

    artist = ma.List(ma.Nested("ArtistSchema", exclude=("studio",)))

#single schema 
studio_schema = StudioSchema()

#Multiple schema 
studios_schema = StudioSchema(many=True)





















# from marshmallow import fields

# the code didn't have the below line, pay attention
# from marshmallow import EXCLUDE
  
    
    # artist = ma.List(ma.Nested("Artist_Schema", exclude=("description",)))
    # artist =fields.Nested("ArtistSchema")
        
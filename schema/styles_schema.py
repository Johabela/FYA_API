from main import ma 

#creating the Schema with Marshmallow 
class StyleSchema(ma.Schema):
    class Meta: 
        fields = ("id", "style_name",  "description", "artist_style")

        load_only =["style_id"]
    
   
    artist_style = ma.Nested("ArtistStyle")
   
#single schema 
style_schema = StyleSchema()

#Multiple schema 
styles_schema = StyleSchema(many=True)



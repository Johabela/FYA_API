from main import ma 


#creating the Schema with Marshmallow 
class ArtistStyle(ma.Schema):
    class Meta: 
        fields = ("id", "years_of_practice", "artist_id", "style_id", "artist", "style")

        load_only =["artist", "style"]
    
#create a reference 
    artist = ma.Nested("ArtistSchema")
    style = ma.Nested("StyleSchema")

        
#single schema 
artist_style_schema = ArtistStyle()

#Multiple schema 
artist_styles_schema = ArtistStyle(many=True)





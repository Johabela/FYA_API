from main import ma 




class ArtistStyle(ma.Schema):
    class Meta: 
        fields = ("id", "years_of_practice", "artist_id", "style_id", "artist", "style")

        # "description"

        load_only =["artist", "style"]
    
#create a reference 

    artist = ma.Nested("ArtistSchema")
    style = ma.Nested("StyleSchema")
        

artist_style_schema = ArtistStyle()
artist_styles_schema = ArtistStyle(many=True)



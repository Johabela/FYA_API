from main import ma 


class ArtistSchema(ma.Schema):
    class Meta: 
        fields = ("id", "artist_name", "verified",  "description", 
                  "work_agreement", "url_instagram", "studio", "studio_id", "years_of_practice"  )
        
        load_only = ["studio_id"]
            

    # composite schema  - > display studio information 
    studio = ma.Nested("StudioSchema")
    

        
artist_schema = ArtistSchema()
artists_schema = ArtistSchema(many=True)





















# from model.artist import  Artist_Model
# from marshmallow import EXCLUDE
# from marshmallow import fields
 
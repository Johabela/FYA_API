from main import ma 
from model.style import Style_Model

# the code didn't have the below line, pay attention
from marshmallow import EXCLUDE



class StyleSchema(ma.Schema):
    class Meta: 
        fields = ("style_id", "style_name",  "description")
    
        

style_schema = StyleSchema()
styles_schema = StyleSchema(many=True)



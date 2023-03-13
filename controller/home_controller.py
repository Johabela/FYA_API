# /index.html 
# /home routs for the app 

from flask import Blueprint


blue_print_home = Blueprint('home', __name__, url_prefix="/")

@blue_print_home.get("/")
def get_home_page():
    return {"message":"Home"}





from controller.artist_controller import bp_artist
from controller.studio_controller import bp_studio
from controller.style_controller import bp_style
from controller.artist_style_controller import bp_artist_style

#all blueprints created need to be stored here 

registerable_controllers = [
    bp_artist, 
    bp_studio, 
    bp_style,
    bp_artist_style,

]


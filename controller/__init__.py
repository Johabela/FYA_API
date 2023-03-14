# from controller.home_controller import blue_print_home
from controller.artist_controller import bp_artist
from controller.studio_controller import bp_studio
from controller.style_controller import bp_style


registerable_controllers = [
    bp_artist, 
    bp_studio, 
    bp_style,

]


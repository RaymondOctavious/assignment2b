# created by raymond octavious
# created on october 2, 2017
# created for isc3u
# created for weekly assignement 
# this assignment calculates the height of the object since it was dropped, in seconds

import ui


def calculate_button_touch_up_inside(sender):
    #constants
    
    GRAVITY = 9.81
    HALF = 0.5
    CLIFF = 100
    
    #variable
    
    seconds = float(view['seconds_textfield'].text)
   
    height = CLIFF - HALF * GRAVITY * seconds ** 2 
    
    view['answer_label'].text = 'The Height of the object is : {0}m above the ground'.format(height)
    
    
    

view = ui.load_view()
view.present('full_screen')

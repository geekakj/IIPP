################################################
####         Mini-Project # 3
### An Introduction to interactive programming 
##              in "Python"
#
#          "Stopwatch: The Game"
##
###
####
################################################

import simplegui

#####################################
###  Definition for global variables
#####################################

timer_tens_of_sec = 0
num_total_stops = 0
num_succes_stops = 0
is_ticking = False

#####################################

#####################################
###    Helper Functions
#####################################

def format(t):
    """
    Helper function that converts time in tenths
    of seconds into formatted string A:BC.D
    """
    time_str = ""
    A = 0
    B = 0
    temp = 0
    if t >= 600:
        A = t/600
    
    temp = t % 600
    
    if temp >= 100:
        B = temp / 100
        temp = temp % 100
    else:
        B = 0
        
    time_str = str(A) + ":" + str(B) + str(temp * 0.1)
    return time_str
        
######################################    

######################################
### Event Handlers for Buttons
######################################

#######################
# Start Button
#######################

def start_timer():
    timer.start()
    global is_ticking
    is_ticking = True

#######################

#######################
# Stop Button
#######################

def stop_timer():    
    global is_ticking,num_total_stops,num_succes_stops,timer_tens_of_sec
    if is_ticking:
        num_total_stops += 1
        if timer_tens_of_sec % 10 == 0:
            num_succes_stops += 1  
    timer.stop()
    is_ticking = False

#######################

#######################
# Reset Button
#######################

def reset_timer():
    global is_ticking,timer_tens_of_sec,num_total_stops,num_succes_stops
    if is_ticking:
        timer.stop()
        is_ticking = False
        
    timer_tens_of_sec = 0
    num_total_stops = 0
    num_succes_stops = 0
        
#######################

####################################
### Event Handler for timer
####################################

def timer_handler():
    global timer_tens_of_sec
    timer_tens_of_sec += 1
    print timer_tens_of_sec

####################################

####################################
### Draw Handler
####################################

def draw(canvas):
    global timer_tens_of_sec
    canvas.draw_text(format(timer_tens_of_sec), (100, 200), 50, 'Red', 'serif')
    canvas.draw_text(str(num_succes_stops) + "/" + str(num_total_stops), (325, 50), 30, 'White', 'serif')

####################################
    
#################
# Frame Creation
#################

frame = simplegui.create_frame("Stopwatch",400,400,300)

#################

####################################
### Registration for Event Handlers
####################################

frame.set_draw_handler(draw)

start_button = frame.add_button("Start",start_timer,150)
stop_button = frame.add_button("Stop",stop_timer,150)
reset_button = frame.add_button("Reset",reset_timer,150)

timer = simplegui.create_timer(100,timer_handler)

#################################
### Start frame
### Enjoy the Game !!!
#################################

frame.start()
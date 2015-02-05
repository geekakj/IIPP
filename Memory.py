################################################
#########    Mini-Project # 5
######
####              MEMORY
######
#########
################################################

import simplegui
import random

turn_count = 0

exposed = []
for num in range(16):
        exposed.append(False)

idx = []
first = 0
second = 0

left = range(8)
right = range(8)
deck = left + right
  

# helper function to initialize globals
def new_game(): 
    global state,turn_count,exposed
    state = 0
    
    turn_count = 0
    
    random.shuffle(deck)
    
    for num in range(16):
        exposed[num] = False
    

     
# define event handlers
def mouseclick(pos):
    global state,first,second,turn_count
    if state == 0:
        state = 1
        first = pos[0]//50
        
        if exposed[first] == False:
            exposed[first] = True
    elif state == 1:
        state = 2
        
        second = pos[0]//50
        
        if exposed[second] == False:
            exposed[second] = True
    else:        
        if (deck[first] != deck[second]):
            exposed[first] = False
            exposed[second] = False
                  
        turn_count = turn_count + 1   
         
        first = pos[0]//50
        
        if exposed[first] == False:
            exposed[first] = True
            
        state = 1   
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global state,first,second
    
    x,y = 5,75
    a = [0,0]
    b = [0,100]
    c = [50,0]
    d = [50,100]
    for num in deck:
        canvas.draw_polygon([a,b,c,d],100,"Green")
        canvas.draw_line(c,d,2,"Red")
        a = c
        b = d
        c[0] = c[0] + 50
        d[0] = d[0] + 50
        
    for idx in range(16):
        if exposed[idx] == True:
            canvas.draw_line([idx*50 + 25,0],[idx*50 + 25,100],50,"Black")       
            canvas.draw_text(str(deck[idx]),(idx*50 + 5,75),80,"White")       


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
label.set_text("Turns = " + str(turn_count))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
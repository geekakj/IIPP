##################################################
#####          Mini-Project 4
###  Implementation of classic arcade game Pong
###
#####
##################################################

import simplegui
import random

##################################################
#### Global Variables Initialization
##################################################

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = HEIGHT/2.0
paddle2_pos = HEIGHT/2.0
paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0

###################################################

###################################################
####   Helper Functions
###################################################

def spawn_ball(direction):
    """
    Initialization function for spawning of ball
    """
    global ball_pos, ball_vel 
    
    ball_pos = [WIDTH/2 ,HEIGHT/2]
    ball_vel = [0,0]
    
    if direction == RIGHT:
        ball_vel = [random.randrange(120,240)/60.0, -random.randrange(60,180)/60.0]
    else:
        ball_vel = [-random.randrange(120,240)/60.0,-random.randrange(60,180)/60.0] 
        
####################################################        
       
####################################################
####    Event Handlers Definition
####################################################

def new_game():
    """
    Function to start/restart a new game
    """
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    
    score1 = 0
    score2 = 0
    
    spawn_ball(RIGHT)
    
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2 
    
    paddle1_vel = 0
    paddle2_vel = 0
    
###--------------------------------------------------    

def draw(canvas):
    """
    Draw Handler function
    """
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,RIGHT,LEFT,paddle1_vel,paddle2_vel
 
        
    #### Drawing mid line and gutters
    
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
       
    #### -----------------------------    
    
    ### Ball position
    
    #### 1. General equation for ball motion
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1] 
    
    #### ------------------------------------
    
    #### 2. Tackling collision with upper and 
    ####    lower canvas boundaries
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]  
        
    #### ------------------------------------

    #### 3. Collision with paddles 
        
    if (ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS)) and \
       ((ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT)) and \
       (ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT))):
            ball_vel[0] = -(1.1 * ball_vel[0])
    elif ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS) and \
        ((ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT)) and \
        (ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT))):
            ball_vel[0] = -(1.1 * ball_vel[0])
    
    #### -------------------------------------
    #### 4. Collision with Gutters
    
    elif ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        score2 += 1
        spawn_ball(RIGHT)
    elif ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        score1 += 1
        spawn_ball(LEFT)  
    
    #### --------------------------------------
            
    #### Draw ball
    
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"Black","Orange")
    
    #### Updating Paddle's vertical position
    
    if (paddle1_pos + paddle1_vel) >= HALF_PAD_HEIGHT and \
       (paddle1_pos + paddle1_vel) <= (HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    
    if (paddle2_pos + paddle2_vel) >= HALF_PAD_HEIGHT and \
       (paddle2_pos + paddle2_vel) <= (HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
    
    #### Drawing paddles
    
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT ],PAD_WIDTH,"Red")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH,paddle2_pos + HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH,paddle2_pos - HALF_PAD_HEIGHT],PAD_WIDTH,"Green")
    
    #### Drawing scores
    canvas.draw_text(str(score1), (200, 100), 40, 'Red')
    canvas.draw_text(str(score2), (380, 100), 40, 'Green')
    
###------------------------------------------------    
        
def keydown(key):
    """
    Key Down Handler function
    """
    
    global paddle1_vel, paddle2_vel
       
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += 10 
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 10 
        
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 10
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += 10
        
###--------------------------------------------------        
       
def keyup(key):
    """
    Key Up Handler Function
    """
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel -= 10
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel += 10
        
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel += 10
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel -= 10
        
###---------------------------------------------------

########################################################

########################################################
##### Frame Creation
########################################################

frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

#### Introduction of Reset Button

reset_button = frame.add_button("Restart",new_game,100)


#### start frame

new_game()
frame.start()

########################################################

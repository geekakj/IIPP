# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# Global variable upper_limit to obtain exact minimum
# number of guesses required to win for a particular
# range from 0 to upper_limit

upper_limit = 100

# Counter to track guesses which remain to win

remaining_guesses = 0

secret_number = 0

# helper function to start and restart the game
def new_game():    
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0,upper_limit)
    global remaining_guesses
    remaining_guesses = int(math.ceil(math.log(upper_limit,2)))
    
    print ""
    print "New Game. Range is from 0 to " + str(upper_limit) + "."
    print "Number of remaining guesses is",remaining_guesses

# define event handlers for control panel
def range100():
    """
    Button Handler to change the range
    from [0,100)
    """
    
    global upper_limit
    upper_limit = 100
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randrange(0,100)
    new_game()  

def range1000():
    """
    Button Handler to change the range
    from [0,1000)
    """
    
    global upper_limit
    upper_limit = 1000
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number = random.randrange(0,1000)
    new_game()
    
def input_guess(guess):
    """
    Input handler for User Input
    """
    
    print ""
    
    guess_int = int(guess)
    print "Guess was",guess_int
    
    global remaining_guesses
    remaining_guesses = remaining_guesses - 1  
    print "Number of remaining guesses is",remaining_guesses  
           
    # main game logic goes here	
    
    if ((guess_int > secret_number) and (remaining_guesses > 0)):
        print "Lower!"
    elif((guess_int < secret_number) and (remaining_guesses > 0)):    
        print "Higher!"
    elif((guess_int == secret_number) and (remaining_guesses >= 0)):
        print "Correct!"
        new_game()
    else:
        print "You ran out of guesses.The number was",secret_number
        new_game()
   
# create frame

frame = simplegui.create_frame("Guess The Number",300,300)

# register event handlers for control elements and start frame

frame.add_button("Range : 0-100",range100,150)
frame.add_button("Range : 0-1000",range1000,150)
frame.add_input('Guess The Number', input_guess,150)

frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

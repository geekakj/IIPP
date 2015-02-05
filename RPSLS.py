# Rock-paper-scissors-lizard-Spock template

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """
    Converts names to their corresponding numbers
    """
    if name == "rock":
        return 0
    elif name == "Spock":   
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Invalid name"
        
def number_to_name(number):
    """
    Converts numbers to their corresponding names
    """
    if number == 0:
        return "rock"
    elif number == 1:   
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Invalid number"
    
def rpsls(player_choice): 
    """
    Rock-paper-scissors-lizard-Spock
    main function
    """
    print ""

    print "Player chooses",player_choice

    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0,5)

    comp_choice = number_to_name(comp_number)
    
    print "Computer chooses",comp_choice

    difference = (comp_number - player_number)%5

    if ((difference == 1) or (difference == 2)):
        print "Computer wins!"
    elif ((difference == 3) or (difference == 4)):
        print "Player wins!"
    else:
        print "Player and computer tie!"
        

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")





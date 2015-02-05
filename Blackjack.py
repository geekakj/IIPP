# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
option = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            
##############################################
# define hand class
##############################################

class Hand:
    def __init__(self):
        """
        create Hand object
        """
        self.card_list = []	

    def __str__(self):
        """
        return a string representation of a hand
        """
        retstr = "Hand contains "
        cardstr = ""
        for card in self.card_list:
            cardstr += card.get_suit() + card.get_rank() + " "
        return retstr + cardstr

    def add_card(self, card):
        """
        add a card object to a hand
        """
        self.card_list.append(card)	

    def get_value(self):
        """
        compute the value of the hand
        """
        hand_value = 0
        is_ace_present = False
        for card in self.card_list:
            hand_value += VALUES[card.rank]
            if card.rank == 'A':
                is_ace_present = True
                
        if is_ace_present and (hand_value + 10) <= 21:
            return (hand_value + 10)
        else:
            return hand_value        
   
    def draw(self, canvas, pos):
        """
        draw a hand on the canvas, use the draw method for cards
        """
        for i in range(len(self.card_list)):
            card_loc = [pos[0] + i*CARD_SIZE[0],pos[1]]
            self.card_list[i].draw(canvas,card_loc)
 
    
######################################
    
######################################
##   define deck class 
######################################

class Deck:
    def __init__(self):
        """
        create a Deck object
        """
        self.card_lst = []
        for suit in SUITS:
            for rank in RANKS:
                self.card_lst.append(Card(suit,rank))

    def shuffle(self):
        """
        shuffle the deck 
        """
        random.shuffle(self.card_lst)

    def deal_card(self):
        """
        deal a card object from the deck
        """        
        return self.card_lst.pop(-1)        
    
    def __str__(self):
        """
        return a string representing the deck
        """
        retstr = "Deck contains "
        cardstr = ""
        for card in self.card_lst:
            cardstr += card.get_suit() + card.get_rank() + " "
        return retstr + cardstr

#######################################

game_deck = Deck()
player_hand = Hand()
dealer_hand = Hand()

#######################################
### define event handlers for buttons
#######################################

def deal():
    global outcome, in_play,game_deck,player_hand,dealer_hand,score,option
      
    if in_play :
        outcome = "You Lose"
        score -= 1
        in_play = False
        option = "New Deal?"
        return
    
    if not in_play:
        option = "Hit or Stand ?"
        outcome = ""
          
        game_deck = Deck()
        game_deck.shuffle()
        print game_deck
    
        player_hand = Hand()
        dealer_hand = Hand()
    
        player_hand.add_card(game_deck.deal_card())
        player_hand.add_card(game_deck.deal_card())
    
        dealer_hand.add_card(game_deck.deal_card())
        dealer_hand.add_card(game_deck.deal_card())
    
        print "Player Hand:",player_hand
        print "Dealer Hand:",dealer_hand
    
        in_play = True

def hit():
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
     
    global player_hand,game_deck,outcome,in_play,score,option
    
    if in_play and player_hand.get_value() <= 21:
        player_hand.add_card(game_deck.deal_card())
        
    if in_play and player_hand.get_value() > 21:
        outcome = "You are busted"
        in_play = False
        score -= 1
        option = "New Deal?"
        
        
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    global outcome,dealer_hand,game_deck,score,option,in_play
    
    if player_hand.get_value() > 21:
        print "You are already busted"        
        return
    
    while in_play and dealer_hand.get_value() < 17:
        dealer_hand.add_card(game_deck.deal_card())
            
    if in_play and dealer_hand.get_value() >= 17:
        outcome = "You Win"
        in_play = False
        score += 1
        option = "New Deal?"
    else:
        if in_play and (dealer_hand.get_value() >= player_hand.get_value()):
            outcome = "You Lose"
            in_play = False
            score -= 1
            option = "New Deal?"
        else:
            outcome = "You Win"
            in_play = False
            score += 1
            option = "New Deal?"
    

# draw handler    
def draw(canvas):
    global player_hand,dealer_hand,outcome,score,in_play
    
    canvas.draw_text("Blackjack",[CARD_CENTER[0] - 10,CARD_CENTER[1] - 10],40,"Aqua")
    
    canvas.draw_text("Dealer",[CARD_CENTER[0],CARD_CENTER[1] + 150],30,"Black")
    
    dealer_hand.draw(canvas,[CARD_CENTER[0],CARD_CENTER[1] + 175])
    if in_play:
        card_loc = CARD_BACK_CENTER
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [CARD_CENTER[0]+ CARD_SIZE[0]/2,CARD_CENTER[1] + CARD_SIZE[1]/2 + 175], CARD_BACK_SIZE)        
    else:
        dealer_hand.draw(canvas,[CARD_CENTER[0],CARD_CENTER[1] + 175])
    
    canvas.draw_text("Player",[CARD_CENTER[0],CARD_CENTER[1] + 350],30,"Black")
    player_hand.draw(canvas,[CARD_CENTER[0],CARD_CENTER[1] + 400])
    
    scorestr = "Score = " + str(score)
    canvas.draw_text(scorestr,[CARD_CENTER[0] + 400,CARD_CENTER[1] + 10],30,"White")
    canvas.draw_text(option,[CARD_CENTER[0] + 200,CARD_CENTER[1] + 350],30,"Yellow")
    canvas.draw_text(outcome,[CARD_CENTER[0] + 200,CARD_CENTER[1] + 150],30,"Yellow")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
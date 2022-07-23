#########################################################
#
# Virtual deck of cards to use - cardsV0.py
#
# Always include a header with name, date and purpose.
#
#########################################################
#import functions here
import random

#########################################################
# the magic happens ...
# insert your functions here - start with one function to check a hand for
# black jack, pairs, eights, ... and return a True or a False
# do not include input and output in your functions, only
# in your main program. This sample checks for an Ace
#########################################################
def checkFlush(hand):
    #add code to check for a flush
    return (False)

#########################################################
# Add a card to a hand given the current deck
#########################################################
def addCard(deck, hand):
    #Get a card off the top of the deck
    card = deck.pop(0)

    #append it to the given hand
    hand.append(card)

#########################################################
# Dispose of a card from a hand
#########################################################
def deleteCard(hand, index):
    hand.pop(index)


#########################################################
# Main routine starts here. You need to include the code below to initialize your deck.
# Please keep the representation of the deck (players, cards and hands) the same for now
# so that I can run your functions against "the deck". Pass in any arguments that are needed
# for the function, do not rely on global variables.
#########################################################

#initialize the suits and labels
suits = ["clubs", "diamonds", "hearts", "spades"]
labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#populate the cards
cards = []
for suit in suits:
    for label in labels:
        cards.append([label, suit])

#shuffle the deck
random.shuffle(cards)

#get the number of players (p) and the number of cards (n)
p = int(input("How many players? "))
n = int(input("How many cards? "))

#set up p players, each with a hand of n cards - value 0 for now
hands = []
for i in range(1,p+1):
    hand = []
    #put in player name
    hand.append("Player "+str(i))
    for j in range(1, n+1):
        hand.append(0)
    hands.append(hand)

#deal out the p hands with n cards each, handing one card at a time to each player
for i in range (0, n):
    for j in range (0, p):
        #take card off top of deck, deal to each player
        card = cards.pop(0)
        hands[j][i+1]=card

#show the cards for each player
for i in range (0, p):
    print(hands[i])

###Exercise 1: Print the first card of the first player


###Exercise 2: Add a card to the second player and print the second player's hand before and after


###Exercise 3: Delete the 2nd card from the second player and print the second player's hand before and after


###Exercise 4: Call a function ######################
#Call a function that takes a hand and checks for something,
#returning True or False. It should take a "hand" (hands[i])
#as an argument and return True or False. Print out which player
#and if they have what you are checking for
for i in range (0,p):
    check = checkFlush(hands[i])
    if (check):
        print(hands[i][0], "'s hand meets this condition", hands[i], sep="")


###Exercise 5: Create your own function and call it

#################
#Created By: Sunny Jain
#February 24th, 2021
#Last Modified: February 24th, 2021
#Function: This program will play-paper-scissors with the user. It will ask them how many times they want to play, ask them their choice, and
#then generate a response. At the end of the game, the program will provide some statistics, and tell the user who won at the end.

#Initializations:

#Sike this program will actually test some stuff for me.

def checkFullHouse(hand):
    allCards = [] #This is the list that I will put all the card numbers into
    for x in range (1, len(hand)):
        tempNum = hand[x][0]
        allCards.append(tempNum) #Now I have put all card numbers into the list
    #print(allCards)
    for y in allCards: #This loop will replace all occurances of letters with their numerical value in the deck
        if y == "A":
            allCards[allCards.index(y)] = 1
        elif y == "J":
            allCards[allCards.index(y)] = 11
        elif y == "Q":
            allCards[allCards.index(y)] = 12
        elif y == "K":
            allCards[allCards.index(y)] = 13
        else:
            allCards[allCards.index(y)] = int(allCards[allCards.index(y)]) #Turning all the numbers into integers so that they can be worked with
    #print(allCards)
    allCards.sort()
    #print(allCards)
    occurx3 = [] #Creating new lists to store the occurances of repeating numbers
    occurx2 = []
    for z in range(1, 14): #This will cycle through all the cards and see if they occur a certain number of times
        occurance = allCards.count(z)
        if occurance >= 3:
            occurx3.append(z)
        elif occurance == 2:
            occurx2.append(z)
        else:
            continue
    #print(occurx3)
    #print(occurx2)
    #Next comes the part where I use all the above information to decide if the player has a full house or not
    if len(occurx3) == 0 or len(occurx2) == 0:
        #print("false")
        return(False)
    
    if len(occurx3) >= 1 and len(occurx2) >= 1:
        answer = max(occurx3)
        global finalAnswer
        finalAnswer = []
        finalAnswer.append(answer)
        finalAnswer.append(hand[0])
        return(finalAnswer) 
        

checkFullHouse(['Player 1', ['10', 'clubs'], ['3', 'hearts'], ['Q', 'spades'],
                ['8', 'diamonds'], ['4', 'diamonds'], ['K', 'hearts'],
                ['5', 'spades'], ['5', 'diamonds'], ['5', 'diamonds'], ['K', 'diamonds']])


for x in range (0, p):
    answer = checkFullHouse(hands[x])
    if answer == False:
        print("No,", hands[x][0], "does not have a full house in their hand.")
    else:
        print("Yes,", hands[x][0], "has a full house in their hand.")
        bigList = []
        bigList.append(finalAnswer)
        
print(bigList)


for y in bigList:
    smallList = []
    smallList.append(bigList[y][1])
print(smallList)

answer = smallList.index(max(smallList))

result = bigList[answer][1]

print('')

print(result, "is the final winner.")

def checkFlush(hand):
    suit = hand[1][1]
    for i in range (1, len(hand)):
        if (hand[i][1] == suit):
            continue
        else:
            return (False)
    return (True)

def yourFunction(hand):
    for i in range (1, len(hand)):
        if (hand[i][0] == "A"):
            return(True)
    return(False)

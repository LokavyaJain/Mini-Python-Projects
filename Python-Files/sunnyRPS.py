#################
#Created By: Sunny Jain
#February 24th, 2021
#Last Modified: February 24th, 2021
#Function: This program will play-paper-scissors with the user. It will ask them how many times they want to play, ask them their choice, and
#then generate a response. At the end of the game, the program will provide some statistics, and tell the user who won at the end.

#Initializations:
def space():
    print('')

userWins = 0
compWins = 0
userRock = 0
compRock = 0
userPaper = 0
compPaper = 0
userScissors = 0
compScissors = 0
rockWins = 0
paperWins = 0
scissorsWins = 0
tie = 0
import random

print('Welcome, User!')
space()
print('This program will play the game Rock-Paper-Scissors with you. You will be allowed to decide how many times you play. '
      'At the end, you will be given some statistics, and you will be told whether or not you won.')
space()
print("Let's begin!")
space()
while True:
    try:
        howManyTimesToPlay = int(input('How many rounds of rounds Rock-Paper-Scissors would you like to play? Please provide a positve integer as '
                           'your answer. '))
        space()
    except:
        space()
        print('Please provide a positive integer as your answer.')
        space()
        continue
    if howManyTimesToPlay == 0:
        space()
        print('Please provide a positive integer as your answer.')
        space()
        continue
    else:
        break
print('You have chosen to play', howManyTimesToPlay, 'rounds.')
space()

#11 = rock
#12 = paper
#13 = scissors

for y in range (0, howManyTimesToPlay):
    space()
    space()
    choice = str.lower(input('Rock, paper, or Scissors? Please provide a response. '))
    space()
    while (choice == 'paper' and choice == 'rock' and choice == 'scissors'):
        break
    while (choice != 'paper' and choice != 'rock' and choice != 'scissors'): 
        space()
        choice = str.lower(input('Please provide a valid response of either Rock, Paper, or Scissors '))
        space()
        if (choice == 'paper' or choice == 'rock' or choice == 'scissors'):
            break
        else:
            continue
    #else: #((choice != 'rock') or (choice != 'paper') or (choice != 'scissors')):
        #space()
        #choice = str.lower(input('Please provide a valid response of either Rock, Paper, or Scissors '))
        #space()
        #continue
    if choice == ('rock'):
        userRock = (userRock + 1)
        compResponse = random.randint(11, 13)
        if compResponse == (11):
            print('The computer chose Rock!')
            space()
            print('This round resulted in a TIE!')
            tie = (tie + 1)
            compRock = (compRock + 1)
        if compResponse == (12):
            print('The computer chose Paper!')
            space()
            print('You LOSE this round!')
            compWins = (compWins + 1)
            compPaper = (compPaper + 1)
        if compResponse == (13):
            print('The computer chose Scissors!')
            space()
            print('You WIN this round!')
            userWins = userWins + 1
            compPaper = (compPaper + 1)
            rockWins = (rockWins + 1)
        continue
    if choice == ('paper'):
        userPaper = (userPaper + 1)
        compResponse = random.randint(11, 13)
        if compResponse == 11:
            print('The computer chose Rock!')
            space()
            print('You WIN this round!')
            userWins = (userWins + 1)
            compRock = (compRock + 1)
            paperWins = (paperWins + 1)
        if compResponse == 12:
            print('The computer chose Paper!')
            space()
            print('This round resulted in a TIE!')
            tie = (tie + 1)
            compPaper = (compPaper + 1)
        if compResponse == 13:
            print('The computer chose Scissors!')
            space()
            print('You LOSE this round!')
            compWins = (compWins + 1)
            compScissors = (compScissors + 1)
        continue
    if choice == ('scissors'):
        userScissors = (userScissors + 1)
        compResponse = random.randint(11, 13)
        if compResponse == 11:
            print('The computer chose Rock!')
            space()
            print('You LOSE this round!')
            compWins = (compWins + 1)
            compScissors = (compScissors + 1)
        if compResponse == 12:
            print('The computer chose Paper!')
            space()
            print('You WIN this round!')
            scissorsWins = (scissorsWins + 1)
            userWins = (userWins + 1)
            compPaper = (userPaper + 1)
        if compResponse == 13:
            print('The computer chose Scissors!')
            space()
            print('This round resulted in a TIE!')
            tie = (tie + 1)
            compScissors = (compScissors + 1)
        continue

#The following are the results of the program.
if userRock == 0 and userPaper == 0:
    space()
    print(howManyTimesToPlay, 'rounds of Rock-Paper-Scissors were played.')
    space()
    print('These are your statistics:')
    print(' -You chose rock 0 times.')
    print(' -You chose Paper 0 times.')
    print(' -You chose Scissors', userScissors, 'time(s) (', int((userScissors / howManyTimesToPlay)*100), "%) and won", int((scissorsWins /userScissors)*100), '% of the time.')
    print(' -Overall after', howManyTimesToPlay, 'rounds, you won', userWins, 'times, the computer won', compWins, 'times, and tied', tie, 'times.')
    space()
    if (userWins > compWins):
        print('Wow, bravo! You beat the computer this time!')
    if (userWins < compWins):
        print('Unfortunately, the computer beat you this game. Better luck next time!')
    if (userWins == compWins):
        print('Oh wow! This game resulted in a tie!')
    space()
    input('Press enter to finish')
    
elif userPaper == 0 and userScissors == 0:
    space()
    print(howManyTimesToPlay, 'rounds of Rock-Paper-Scissors were played.')
    space()
    print('These are your statistics:')
    print(' -You chose Rock', userRock, 'time(s) (', int((userRock / howManyTimesToPlay)*100), "%) and won", int((rockWins /userRock)*100), '% of the time.')
    print(' -You chose Paper 0 times.')
    print(' -You chose Scissors 0 times.')
    print(' -Overall after', howManyTimesToPlay, 'rounds, you won', userWins, 'times, the computer won', compWins, 'times, and tied', tie, 'times.')
    space()
    if (userWins > compWins):
        print('Wow, bravo! You beat the computer this time!')
    if (userWins < compWins):
        print('Unfortunately, the computer beat you this game. Better luck next time!')
    if (userWins == compWins):
        print('Oh wow! This game resulted in a tie!')
    space()
    input('Press enter to finish')
    
elif userRock == 0 and userScissors == 0:
    space()
    print(howManyTimesToPlay, 'rounds of Rock-Paper-Scissors were played.')
    space()
    print('These are your statistics:')
    print(' -You chose rock 0 times.')
    print(' -You chose Paper', userPaper, 'time(s) (', int((userPaper / howManyTimesToPlay)*100), "%) and won", int((paperWins /userPaper)*100), '% of the time.')
    print(' -You chose scissors 0 times.')
    print(' -Overall after', howManyTimesToPlay, 'rounds, you won', userWins, 'times, the computer won', compWins, 'times, and tied', tie, 'times.')
    space()
    if (userWins > compWins):
        print('Wow, bravo! You beat the computer this time!')
    if (userWins < compWins):
        print('Unfortunately, the computer beat you this game. Better luck next time!')
    if (userWins == compWins):
        print('Oh wow! This game resulted in a tie!')
    space()
    input('Press enter to finish')

elif userRock == 0:
    space()
    print(howManyTimesToPlay, 'rounds of Rock-Paper-Scissors were played.')
    space()
    print('These are your statistics:')
    print(' -You chose rock 0 times.')
    print(' -You chose Paper', userPaper, 'time(s) (', int((userPaper / howManyTimesToPlay)*100), "%) and won", int((paperWins /userPaper)*100), '% of the time.')
    print(' -You chose Scissors', userScissors, 'time(s) (', int((userScissors / howManyTimesToPlay)*100), "%) and won", int((scissorsWins /userScissors)*100), '% of the time.')
    print(' -Overall after', howManyTimesToPlay, 'rounds, you won', userWins, 'times, the computer won', compWins, 'times, and tied', tie, 'times.')
    space()
    if (userWins > compWins):
        print('Wow, bravo! You beat the computer this time!')
    if (userWins < compWins):
        print('Unfortunately, the computer beat you this game. Better luck next time!')
    if (userWins == compWins):
        print('Oh wow! This game resulted in a tie!')
    space()
    input('Press enter to finish')

elif userPaper == 0:
    space()
    print(howManyTimesToPlay, 'rounds of Rock-Paper-Scissors were played.')
    space()
    print('These are your statistics:')
    print(' -You chose Rock', userRock, 'time(s) (', int((userRock / howManyTimesToPlay)*100), "%) and won", int((rockWins /userRock)*100), '% of the time.')
    print(' -You chose Paper 0 times.')
    print(' -You chose Scissors', userScissors, 'time(s) (', int((userScissors / howManyTimesToPlay)*100), "%) and won", int((scissorsWins /userScissors)*100), '% of the time.')
    print(' -Overall after', howManyTimesToPlay, 'rounds, you won', userWins, 'times, the computer won', compWins, 'times, and tied', tie, 'times.')
    space()
    if (userWins > compWins):
        print('Wow, bravo! You beat the computer this time!')
    if (userWins < compWins):
        print('Unfortunately, the computer beat you this game. Better luck next time!')
    if (userWins == compWins):
        print('Oh wow! This game resulted in a tie!')
    space()
    input('Press enter to finish')

elif userScissors == 0:
    space()
    print(howManyTimesToPlay, 'rounds of Rock-Paper-Scissors were played.')
    space()
    print('These are your statistics:')
    print(' -You chose Rock', userRock, 'time(s) (', int((userRock / howManyTimesToPlay)*100), "%) and won", int((rockWins /userRock)*100), '% of the time.')
    print(' -You chose Paper', userPaper, 'time(s) (', int((userPaper / howManyTimesToPlay)*100), "%) and won", int((paperWins /userPaper)*100), '% of the time.')
    print(' -You chose Scissors 0 times.')
    print(' -Overall after', howManyTimesToPlay, 'rounds, you won', userWins, 'times, the computer won', compWins, 'times, and tied', tie, 'times.')
    space()
    if (userWins > compWins):
        print('Wow, bravo! You beat the computer this time!')
    if (userWins < compWins):
        print('Unfortunately, the computer beat you this game. Better luck next time!')
    if (userWins == compWins):
        print('Oh wow! This game resulted in a tie!')
    space()
    input('Press enter to finish')
        
else:
    space()
    print(howManyTimesToPlay, 'rounds of Rock-Paper-Scissors were played.')
    space()
    print('These are your statistics:')
    print(' -You chose Rock', userRock, 'time(s) (', int((userRock / howManyTimesToPlay)*100), "%) and won", int((rockWins /userRock)*100), '% of the time.')
    print(' -You chose Paper', userPaper, 'time(s) (', int((userPaper / howManyTimesToPlay)*100), "%) and won", int((paperWins /userPaper)*100), '% of the time.')
    print(' -You chose Scissors', userScissors, 'time(s) (', int((userScissors / howManyTimesToPlay)*100), "%) and won", int((scissorsWins /userScissors)*100), '% of the time.')
    print(' -Overall after', howManyTimesToPlay, 'rounds, you won', userWins, 'times the computer won', compWins, 'times, and tied', tie, 'times.')
    space()
    if (userWins > compWins):
        print('Wow, bravo! You beat the computer this time!')
    if (userWins < compWins):
        print('Unfortunately, the computer beat you this game. Better luck next time!')
    if (userWins == compWins):
        print('Oh wow! This game resulted in a tie!')
    space()
    input('Press enter to finish')







###############
#Created by: Sunny Jain
#Febraury 24th, 2021
#Last Modified: February 24th, 2021
#Function: These are the pseudocode instructions for a program that will play rock paper scissors with a user for as many
#games as they wish, generate a response, tell them who won, and give them statistics at the end.
#
##Initialize the counters -> userWins = 0
#-> comp wins, userWins
#->comprock = 0, userrocks = 0
#->comppaper = 0, user paper = 0
#->compscissors = 0, user scissors = 0
#Import the random function -> import random
#
#Welcome the user
#Tell them what the program is about -> print('This program will...')
#
#How many times they will play -> x = int(input('How many times would you like to play?'))
#Use a while true loop to test if they respond with a number
#-> While true:
#   ->try: x
#-> Except:
#   ->their response != int print ('please provide a whole integer as your answer')
#-> Else: Break
#
#tell them how many times they are playing -> print ('You will play', x ,' times')
#
#Make sure to add spaces after the input prompt
#
#Define what each number means (this is a note)
#eg. -> 1 = rock
#
#Create the actual algorithm that will be used to run each possible result
#^Put this into a for loop so that it repeats as many times as the user wants.
#First, create a for loop for how many times they want to play the game.
#-> For y in range (1, x): (this is how many times the game will be played. Everything will stay within this.)
#       put in the rock/paper/scissors prompt -> question()
#       ^Add a while loop to check if they give a valid answer to the question:
#           ->while ('choice == paper and choice == rock etc.'):
#               break the while loop -> break
#           create another while loop if the answer is not corect                                  #I also made some changes here
#           -> While (choice != paper and etc.+
#           ,   prompt them to proide a valid answer
#               Create another conditional to check if the answer to that is correct
#               ->if choice == paper: Break
#               ->else: continue
#       if the user response = rock
#           increase the counter for what they picked for later statistics -> userRock+1
#           computerReaction = random.randint(1, 3) (each number will have a definition of either rock paper or scissors)
#           Write if statements for each computer response. (for example, if I get 1 from the randint function, i will return with rock)
#               Within this, write the things you will say -> You won,lost, etc
#               depending on who wins, change either the win or loss counter -> (userwins + 1) or (compWins +1)
#               also change the amount of user responses and computer responses -> computerrock+1
#               ^This is based on what the computer randomly responds with.
#           after all of this is done, put a continue function so that the for loop moves onto the next value
#       if the user response = paper
#           do the same as the rock response
#       if the user response = scissors
#           do the same as the rock response
#
#
#Put all the statistics for the round -> print(x, 'rounds of RPC were played')
#THIS IS A CHANGE I HAD TO MAKE TO MY PSUEDOCODE:
#^ Create seperate cases for if rock paper or scissors arent chosen, and put them
#into elif statements. Do this because division with 0 is not possible. There
#Will be 6 of these
#
#do the math: print(' - Rock was chosen', user rock, 'times....')
#do the math for paper and scissors.
#check if its a tie, win or loss for user based on userwins/ compwins
#   make it a conditional and then print who won -> if userwins > compwins: etc.
#
#say thank you for playing
#
#Put an promp so that the program doesnt instantly end -> print('press enter to finish')

############
#Written by Sunny Jain
#Created: February 19th, 2021
#Last Modified: February 21st, 2021
#This program will ask you a yes or no question, and then generate a random response

print('This program will ask you a yes or no question, and then generate a response.')
print("")

def numbers():

    question = input('Please enter a question that can be answered with yes or no. ')
    print('')

    import random

    question = random.randint(1, 10)

    if question == 1:
        print("Answer: I am uncertain. Please give me another moment to come up with an answer.")
        print("")
        print('...')
        print("Okay, I'm ready now. Lets go.")
        print('...')
        print('')
        numbers()
    if question == 2:
        print("Answer: Sorry, I'm on lunch break. Ask me again later.")
        print('')
        print('...')
        print("Okay, I'm ready now. Lets go.")
        print('...')
        print('')
        numbers()
    if question == 3:
        print("Answer: I would most certainly say YES.")
    if question == 4:
        print("Answer: YES, and I'd bet my life on it!")
    if question == 5:
        print("Answer: No matter what, the answer will always be YES!")
    if question == 6:
        print("Answer: The answer is obviously YES. There's no doubt about it!")
    if question == 7:
        print("I don't know about you, but I'm saying NO...")
    if question == 8:
        print("NO, certainly not!")
    if question == 9:
        print("NO, I certainly wouldn't put my money on it!")
    if question == 10:
        print('No, it could never be possilbe')

def afterHours():
    
        afterwards = input('Type "again" and press enter to play again, or type anything else and press enter to end the program.')
        if afterwards == ("again"):
              print('')
              print('')
              numbers()
        
def end():
  print('')
  numbers()
  print('')
  afterHours()

x = True

numbers()

while x == True:
 print('')
 afterwards = input('Type "again" and press enter to play again, or type anything else and press enter to end the program.')
 if afterwards == ("again"):
              print('')
              print('')
              numbers()
 else:
              break


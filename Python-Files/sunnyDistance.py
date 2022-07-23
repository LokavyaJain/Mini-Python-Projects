###########
#Sunny Jain
#Created on: March 2nd, 2021
#Last Modified: March 2nd, 2021
#Purpose: This program will take the input of two coordinates from a user, and then output the distance between them using...
#... the distance formula and functions.


import math


#This is the function that will actually perform the formula using input: 

def engine(x1, y1, x2, y2):
    formula = float(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    return formula

#The following is the main program
    #This is the introduction where I tell the user what's going on

print('Hello user!')
print('This program will calculate the distance between two coordinates of your choice.')
print('The formula used is as follows:')
print('   The distance between coordinates (x1, y1) and (x2, y2) is sqrt((x2 - x1)**2 + (y2 - y1)**2)).')
print()
print()
      
    #This is where I ask the user their coordinates

valuex1 = float(input('Please provide ONLY the value of x in your FIRST coordinate (x1): '))
valuey1 = float(input('Please provide ONLY the value of y in your FIRST coordinate (y1): '))
print('Your starting point is', (valuex1, valuey1))
print()
valuex2 = float(input('Please provide ONLY the value of x in your SECOND coordinate (x2): '))
valuey2 = float(input('Please provide ONLY the value of y in your SECOND coordinate (y2): '))
print('Your ending point is', (valuex2, valuey2))

    #This part is where I use all my previous input to provide an answer using a function

answer = engine(valuex1, valuey1, valuex2, valuey2)

print()
print()
print('The distance between', '(' + (str(valuex1)) + ',' + (str(valuey1)) + ')', 'and', '(' + (str(valuex2)) + ',' + (str(valuey2)) + ')', 'is', answer)
print()
input('Press enter to finish')

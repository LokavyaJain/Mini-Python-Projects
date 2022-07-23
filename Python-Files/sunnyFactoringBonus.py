################
#Written by Sunny Jain
#Created: February 19th, 2021
#Last Modified: April 14th, 2021
#This program allows the user to define the values of a, b, and c in the quadratic function (ax^2 + bx + c), and factors it completely.

import sys #I will need this later on if a funciton is not factorable 

def space(): #Ignore this, I made this when I realized that I wouldn't have to put quotes in print() when I wanted a space
    print('') 

print('This program allows the user to define the values of a, b, and c in the quadratic function (ax^2 + bx + c = 0), and factors it.')
space()

print('Please define the values for a, b, and c in the quadratic function (ax^2 + bx + c = 0).')
space()


a = int(input('What value would you like to give variable a? '))
b = int(input('What value would you like to give variable b? '))
c = int(input('What value would you like to give variable c? '))
space()

print('Your quadratic function is...')
print(a, "x^2 + ", '(', b, ')', 'x + ', '(', c, ')')

#This will find the gcf of all three numbers and factor them
for x in range(1, max(a, b, c)+1):
    if a%x == 0:
        if b%x == 0:
            if c%x == 0:
                factoredValue = x


space()
print("Once the gcf is removed, your number is: ")
print(factoredValue, '(', a/factoredValue, "x^2 + ", '(', b/factoredValue, ')', 'x + ', '(', c/factoredValue, ')', ')')
space()

a = int(a/factoredValue)
b = int(b/factoredValue)
c = int(c/factoredValue)
if c < 0:
    co = c
if c > 0:
    co = int(0-c)


if a < 0:
    ao = a
if a > 0:
    ao = int(0-a)

#At this point, the lowest common denominator has been removed

#Now I will take the factored part of c and find its factors
#I will also add them to a list from which I can use later to find the answer

pairsC = []
potentialPairsC = []


if c > 0:
 for y in range(co, c+1):
    for z in range(co, c+1):
        potentialPairsC = []
        if (y*z) == c:
            potentialPairsC.append(y)
            potentialPairsC.append(z)
            pairsC.append(potentialPairsC)
        if (y*z != c):
            continue
elif c < 0:
 for y in range(1, (c - 1), -1):
    for z in range(1, (c - 1), -1):
        potentialPairsC = []
        if (y*z*(-1)) == c:
            potentialPairsC.append(y)
            potentialPairsC.append(z*(-1))
            pairsC.append(potentialPairsC)
        if (y*z != c):
            continue

#I will now take the factored form of a and find its factors
#Similarly to before, I will add the factors to a list

pairsA = []
potentialPairsA = []

if a > 0:
 for y in range(ao, a+1):
    for z in range(ao, a+1):
        potentialPairsA = []
        if (y*z) == a:
            potentialPairsA.append(y)
            potentialPairsA.append(z)
            pairsA.append(potentialPairsA)
        if (y*z != a):
            continue
elif a < 0:
 for y in range(1, (a - 1), -1):
    for z in range(1, (a - 1), -1):
        potentialPairsA = []
        if (y*z*(-1)) == a:
            potentialPairsA.append(y)
            potentialPairsA.append(z*(-1))
            pairsA.append(potentialPairsA)
        if (y*z != a):
            continue

#Now I will use the "criss cross" method to find the values of x
#I will multiply elements from both lists and see if the equal to the values of c

finalPairsOne = [] #This is the list in which I will add my final answer
finalPairsTwo = []

for n in pairsA:
    
    for m in pairsC:
        multiplyOne = (n[0]*m[1])
        multiplyTwo = (n[1]*m[0])
        if ((multiplyOne + multiplyTwo) == (b)):
            finalPairsOne.append(n[0])
            finalPairsOne.append(m[0])
            finalPairsTwo.append(n[1])
            finalPairsTwo.append(m[1])
        else:
            continue

factoredValue = str(factoredValue) #Turning this into a string so that it can be concatonated

if ((len(finalPairsOne) == 0) or (len(finalPairsTwo) == 0)):
    print("Your equation cannot be factored any further.")
    print()
    input("Press enter to finish")
    sys.exit()

xOne = (finalPairsOne[-2])
xTwo = (finalPairsTwo[-2])
yOne = (finalPairsOne[-1])
yTwo = (finalPairsTwo[-1])

if yOne < 0 and yTwo > 0:
    xOne = str(finalPairsOne[-2]) #Turning these all into strings so that they can be concatonated
    xTwo = str(finalPairsTwo[-2])
    yOne = str(finalPairsOne[-1])
    yTwo = str(finalPairsTwo[-1])

    #The next 10 lines are present for formatting purposes so that we get our answer in the desired format
    if factoredValue == "1":
        factoredValue = ""
    if xOne == "1":
        xOne = ''
    if xOne =='-1':
        xOne = '-'
    if xTwo == "1":
        xTwo = ''
    if xTwo == "-1":
        xTwo = "-"
 
    print()
    print("Your final answer is:")
    print(factoredValue + "(" + xOne + "x " + yOne + ")(" + xTwo + "x + " + yTwo + ")")
    
    
elif yTwo < 0 and yOne > 0:
    xOne = str(finalPairsOne[-2])
    xTwo = str(finalPairsTwo[-2])
    yOne = str(finalPairsOne[-1])
    yTwo = str(finalPairsTwo[-1])

    #The next 10 lines are present for formatting purposes so that we get our answer in the desired format
    if factoredValue == "1":
        factoredValue = ""
    if xOne == "1":
        xOne = ''
    if xOne =='-1':
        xOne = '-'
    if xTwo == "1":
        xTwo = ''
    if xTwo == "-1":
        xTwo = "-"

    print()
    print("Your final answer is:")
    print(factoredValue + "(" + xOne + "x + " + yOne + ")(" + xTwo + "x " + yTwo + ")")

elif yOne < 0 and yTwo < 0:
    xOne = str(finalPairsOne[-2])
    xTwo = str(finalPairsTwo[-2])
    yOne = str(finalPairsOne[-1])
    yTwo = str(finalPairsTwo[-1])

    #The next 10 lines are present for formatting purposes so that we get our answer in the desired format
    if factoredValue == "1":
        factoredValue = ""
    if xOne == "1":
        xOne = ''
    if xOne =='-1':
        xOne = '-'
    if xTwo == "1":
        xTwo = ''
    if xTwo == "-1":
        xTwo = "-"

    print()
    print("Your final answer is:")
    print(factoredValue + "(" + xOne + "x " + yOne + ")(" + xTwo + "x " + yTwo + ")")

else:
    xOne = str(finalPairsOne[-2])
    xTwo = str(finalPairsTwo[-2])
    yOne = str(finalPairsOne[-1])
    yTwo = str(finalPairsTwo[-1])

    #The next 10 lines are present for formatting purposes so that we get our answer in the desired format
    if factoredValue == "1":
        factoredValue = ""
    if xOne == "1":
        xOne = ''
    if xOne =='-1':
        xOne = '-'
    if xTwo == "1":
        xTwo = ''
    if xTwo == "-1":
        xTwo = "-"

    print()
    print("Your final answer is:")
    print(factoredValue + "(" + xOne + "x + " + yOne + ")(" + xTwo + "x + " + yTwo + ")")

print()

input("Press enter to finish.")


    


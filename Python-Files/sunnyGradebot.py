##########
# Written by Sunny Jain
# Created: February 19th, 2021
# Last Modified: February 21st, 2021
# This program will help a user calculate their grade and percent on a test.

# Leave space after input question

print('This program will help a user calculate their grade and percent on a test.')
print('')

mark = int(input("What is your test mark? "))

print("")
outOf = int(input("What is your test out of? "))
#loop this part. 
while (outOf == 0):
    print('')
    print("Please provide a valid answer.")
    print('')
    outOf = int(input("What is your test out of? "))  
    
print('')

#loop this
while (mark > outOf):
    print("")
    print("The mark you have provided is higher than the highest possible"
          "test score. Please provide a valid answer")
    print("")
    outOf = int(input("What is your test out of? "))
    print("")
percentage = float((mark/outOf)*100)
print("Your percentage grade is", percentage, "%")

if (percentage >= 86):
    print("You got an A! Excellent job!")
if (73 <= percentage < 86):
    print("You got a B! Good job!")
if (67 <= percentage < 73):
    print("You got a C+. There\'s much room for improvement!")
if (60 <= percentage < 67):
    print("You got a C. Spend more time studying next time. You can do it!")
if (50 <= percentage < 60):
    print("You got a C-. spend more time studying and give it your")
    print ("full focus! You can do it!")
if (0 <= percentage <50):
    print("You got an F. Spend more time studying, and give it "
          "your full focus. If you need help, ask your teacher! You can do it!")
print('')

input("Press enter to finish")


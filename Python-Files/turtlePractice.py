import turtle

screen = turtle.getscreen()

mainc = turtle.Turtle()

mainc.right(90) #This is the angle it turns
mainc.forward(100) #This is the distance it goes
mainc.left(90) 
mainc.backward(100)

mainc.rt(90)
mainc.fd(100)
mainc.lt(90)
mainc.bk(100)

mainc.up
mainc.forward(360)
mainc.down
mainc.bk(90)

mainc.penup()
mainc.goto(10,10)
mainc.home()
mainc.pendown()

a = mainc

a.fd(100)
a.rt(90)
a.fd(100)
a.rt(90)
a.fd(100)
a.rt(90)
a.fd(100)
a.rt(90)

a.fd(120)
a.rt(90)
a.fd(200)
a.rt(90)
a.fd(120)
a.rt(90)
a.fd(200)
a.rt(90)

a.circle(60) #The number within the brackets is the radius of the circle.

a.dot(20) #The number in brackets is the diameter of the dot.
 
turtle.bgcolor("blue") #Make sure to use the american spelinga and use the full word turtle not the variable

turtle.title('Turtle Practice') #Put this at the start of the program otherwise it will not change anything until end (initializations)

#The following changes the size of the physical turtle
a.shapesize(1, 5, 10)
a.shapesize(10, 5, 1)
a.shapesize(1,10,5)
a.shapesize(10,1,5)
#These numbers are the perameters for the turtle size
#Stretch length
#Strecth width
#Outline width

#The following chages the size of the actual pen drawing
a.pensize(5)
a.fd(100)

#The following changes the size and colour of the actual turtle.
a.shapesize(3,3,3)
a.fillcolor("red")

#The following changes the colour of the pen/outline
a.pencolor('green')
a.fd(100)

#the following allows you to change both with one command
a.color("green", "red") #The first colour is for the pen, the second one is for the fill

a.begin_fill() #I'm telling the program that i'm going to be drawins a cosed shape that I need to be filled in
a.fd(100)
a.lt(120)
a.fd(100)
a.lt(120)
a.fd(100)
a.lt(120)
a.end_fill() #I'm indicating that i'm finished filling my circle in with this command 

#The following changes the actual turtle shape
a.shape('turtle')
a.bk(100)
a.shape('arrow')
a.fd(100)
a.shape('circle')
a.bk(100)
a.shape('square')
a.fd(100)
a.shape('triangle')
a.bk(100)
a.shape('classic')
a.fd(100)
a.shape('circle')
a.bk(100)

#The following changes the speed of teh turtle
a.speed(1)
a.fd(100)
a.speed(10)
a.fd(100)
#0 is the slowest speed, 10 is the highest speed

#How to have multiple commands in one line
a.pen(pencolor="purple", fillcolor="orange", pensize = 10, speed=9)
a.begin_fill()
a.circle(90)
a.end_fill()
#Change everything in one line instead of changing every single thing individually

#This is how you pick the pen up and down
a.fd(100)
a.rt(90)
a.penup()
a.fd(100)
a.rt(90)
a.pendown()
a.fd(100)
a.rt(90)
a.penup
a.fd(10)
a.pendown()

#How to undo stuff
a.undo()
#type this three times to undo the last three commands

#This is how to clear the screen
a.clear() #This will cear the screen, but not change anyting (eg. variables, position, size)
#^This only erases that specific turtle

#This is how to reset the whole thing
a.reset()
#^This will clear the screen, and reset the turtle to its default perameters
#^You will also e sent to the home position

a.stamp()
8#These numbers are the location or stamp ID for the stamp
a.fd(100)
a.stamp()
9
a.fd(100)
#To remove a praticular stamp, you do this:
a.clearstamp(8)

#This is how to clone the turtle:
b = a.clone() #Create a new variable for that clone
a.color("magenta")
b.color("red")
a.circle(100)
b.circle(60)

for x in range(4): #This repeats it 4 times
    a.fd(100)
    a.rt(90)

#The following is how I change the size of my stage/window
height = 360 #This is a variable so don't use it anywhere else
width = 360
screen = Screen()
screen.screensize(width, height)




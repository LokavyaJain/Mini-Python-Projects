#####
#Sunny Jain
#Created on: March 5th, 2021
#Purpose: Functions for team day

#distance

def distance(x1, x2, x3, y1, y2, y3):
    side1 = float(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    side2 = float(math.sqrt((x2 - x3)**2 + (y2 - y3)**2))
    side3 = float(math.sqrt((x1 - x3)**2 + (y1 - y3)**2))
    return (side1, side2, side3)

##############
#Sunny Jain
#Created on: March 2, 2021
#Last Modified: March 2, 2021
#This program will perform a set of math equations on different numbers using 3 functions.


#This is the part where I define the variables. Will not yet be executed, just defined.
def f(x):
    x1 = (x - 1)
    return x1
def g(x):
    x2 = (x*2)
    return x2
def h(x):
    x3 = ((3*x) + 1)
    return x3


#This is the main program where I print the answers for these equations.
print('This program will perform some math functions.')
print()
print()

print('f(10) =', f(10))
print()
print('g(6) =', g(6))
print()
print('h(3) =', h(3))
print()
print('f(g(2)) =', f(g(2)))
print()
print('g(h(10)) =', g(h(10)))
print()
print('f(g(h(11))) =', f(g(h(11))))

print()
print()
input('Press enter to finish.')

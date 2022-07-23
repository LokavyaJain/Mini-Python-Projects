#########
#Sunny Jain
#Created on: March 2nd, 2021
#Last Modified: March 2nd, 2021
#This program will recite Old Macdonald multiple times using functions, with diffirent animals and sounds each time.


#This is the main function. It will not do anyting until I call it.

def mainTrack(x, y):
    print("Old Macdonald had a farm, e-i-e-i-o!")
    print('And on this farm there was a', x + ', e-i-e-i-o!')
    print('With a', y, y, 'here and a', y, y, 'there,')
    print('Here a', y + ', there a', y + ', everywhere a', y, y + '!')
    print('Old MacDonald had a farm, e-i-e-i-o!')
    print()


#this is the main program. Here I will give x and y values to represent animals and noises. There will be...
#...4 total verses.

mainTrack('duck', 'quack')
mainTrack('cow', 'moo')
mainTrack('mutalisk', 'woosh')
mainTrack('snake', 'hiss')


#i'm just adding this so that the actual program does not instanly end. 

input('Press enter to finish.')

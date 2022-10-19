# Interface creator
# Paul Ambrose 18/10/2022
# Program to create re-usable code for creating interfaces for python programs

# modules
import os
import datetime

# introduction
print("Interface Code Creator")

# get basic parameters
buttonNumber = input("How many buttons would you like? >> ")
windowWidth = input("How wide would you like your interface to be? >> ")
windowHeight = input("How tall would you like your interface to be? >> ")
fileName = input("What would you like to call the file? >> ")
filePath = os.getcwd() + "\output"

# https://www.w3schools.com/python/python_datetime.asp
dateStamp = datetime.datetime.now()
formattedDate = dateStamp.strftime("%y%m%d")

# created textfile
# https://www.pythontutorial.net/python-basics/python-create-text-file/
with open(filePath + '\interface_' + fileName + formattedDate + ".py", 'w') as f:

    # populate textfile
    f.write('#' + "filename = " + fileName + '\n'
            '#' + "Paul Ambrose -" + formattedDate + '\n\n'

            'import pygame\n'
            'from pygame.locals import *\n'
            'from SimpleButton import *\n'
            'import sys\n\n'

            'GRAY = (200, 200, 200)' + '\n'
            'WINDOW_WIDTH = ' + windowWidth + '\n'
            'WINDOW_HEIGHT = ' + windowHeight + '\n'
            'FRAMES_PER_SECOND = 30' + '\n\n'

            'pygame.init()\n'
            'window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))\n'
            'clock = pygame.time.Clock()\n\n'
            )
f.close()

for buttons in range(1, int(buttonNumber)):
    print("Test")

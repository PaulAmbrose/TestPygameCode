# Interface creator
# Paul Ambrose 18/10/2022
# Program to create re-usable code for creating interfaces for python programs

# modules
import os
import datetime
print("Interface Code Creator")

buttonNumber = input("How many buttons would you like? >> ")
windowWidth = input("How wide would you like your interface to be? >> ")
windowHeight = input("How tall would you like your interface to be? >> ")
fileName = input("What would you like to call the file? >> ")
filePath = os.getcwd() + "\output"

dateStamp = datetime.datetime.now()
formattedDate = dateStamp.strftime("%y%m%d")

with open(filePath + '\interface_' + fileName + formattedDate + ".py", 'w') as f:

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

counter = 1
vPosition = 25
for buttons in range(0, int(buttonNumber)):

    buttonName = input(
        "What would you like to call button " + str(counter) + " ? >> ")

    with open(filePath + '\interface_' + fileName + formattedDate + ".py", 'a') as f:
        f.write('oButton' + str(counter) + ' = SimpleButton(window, (' + str(vPosition) + ', 30),\n'
                '\t\t\t\t\timages/buttonAUp.png,\n'
                '\t\t\t\t\timages/buttonADown.png)\n')
    counter = counter + 1
    vPosition = vPosition + 100
f.close()

with open(filePath + '\interface_' + fileName + formattedDate + ".py", 'a') as f:
    f.write('\nwhile True:\n\n'

            'for event in pygame.event.get():\n'
            'if event.type == pygame.QUIT:\n'
            '\t\tpygame.quit()\n'
            '\t\tsys.exit()\n\n'
            )
f.close()

counter = 1
for buttons in range(0, int(buttonNumber)):

    with open(filePath + '\interface_' + fileName + formattedDate + ".py", 'a') as f:
        f.write('if oButton + str(counter).handleEvent(event):\n'
                '\tpass\n')
    counter = counter + 1
f.close()

with open(filePath + '\interface_' + fileName + formattedDate + ".py", 'a') as f:
    f.write('window.fill(GRAY)\n')
f.close()

counter = 1
for buttons in range(0, int(buttonNumber)):

    with open(filePath + '\interface_' + fileName + formattedDate + ".py", 'a') as f:
        f.write('if oButton + str(counter).draw():\n')
    counter = counter + 1
f.close()    # 10 - Draw all window elements

with open(filePath + '\interface_' + fileName + formattedDate + ".py", 'a') as f:
    f.write('pygame.display.update()\n'
            'clock.tick(FRAMES_PER_SECOND)\n')
f.close()

# pygame demo 6(b) - using the flakes class, bounce many flakess

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
from flakes import *  # bring in the flakes class code

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds, etc.
flakesList = []
# 5 - Loop forever
while True:

    # 6 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 7 - Initialize variables
    # Each time through the loop, create a flakes object
    oflakes = flakes(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    # append the new flakes to the list of flakess
    flakesList.append(oflakes)

    # 8 - Do any "per frame" actions
    for oflakes in flakesList:
        oflakes.update()  # tell each flakes to update itself

   # 9 - Clear the window before drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements
    for oflakes in flakesList:
        oflakes.draw()   # tell each flakes to draw itself

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

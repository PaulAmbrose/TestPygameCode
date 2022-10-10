# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_FLAKES = 3

# 3 - Initialize the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 5 - Initialize variables
flakeList = []
for oFlake in range(0, N_FLAKES):
    # Each time through the loop, create a Ball object
    oFlake = pygame.draw.circle(window, WHITE, (250, 50), 30, 0)
    flakeList.append(oFlake)  # append the new Ball to the list of Balls

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    for oBall in ballList:
        oBall.update()  # tell each Ball to update itself

   # 9 - Clear the window before drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements
    for oBall in ballList:
        oBall.draw()   # tell each Ball to draw itself

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

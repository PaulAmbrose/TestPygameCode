import pygame
from pygame.locals import *
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_FLAKES = 300

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

flakeList = []
for oFlake in range(0, N_FLAKES):
    oFlake = pygame.draw.circle(window, WHITE, (250, 50), 1, 0)
    flakeList.append(oFlake)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for oFlake in flakeList:
        oFlake.update()
    window.fill(BLACK)

    for oFlake in flakeList:
        oFlake.draw()   # tell each Ball to draw itself

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

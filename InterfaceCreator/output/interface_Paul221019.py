#filename = paul
#Paul Ambrose -221019

import pygame
from pygame.locals import *
from SimpleButton import *
import sys

GRAY = (200, 200, 200)
WINDOW_WIDTH = 5
WINDOW_HEIGHT = 5
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()


import pygame
from pygame.locals import *
import random

WHITE = (255, 255, 255)

# flakes class


class flakes():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load('images/flake.png')

        # A rect is made up of [x, y, width, height]
        flakesRect = self.image.get_rect()
        self.width = flakesRect.width
        self.height = flakesRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        # Pick a random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = 0

        # Choose a random speed between -4 and 4, but not zero
        # in both the x and y directions
        speedsList = [1, 2, 3, 4]

        #self.xSpeed = random.choice(speedsList)
        self.xSpeed = 0
        self.ySpeed = random.choice(speedsList)
        #self.ySpeed = 0

    def update(self):
        # Check for hitting a wall.  If so, change that direction.

        # if (self.x < 0) or (self.x >= self.maxWidth):
        #    self.xSpeed = -self.xSpeed

        # if (self.y < 0) or (self.y >= self.maxHeight):
        #    self.ySpeed = -self.ySpeed
        if self.y >= self.maxHeight:
            self.ySpeed = 0

        # Update the flakes's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

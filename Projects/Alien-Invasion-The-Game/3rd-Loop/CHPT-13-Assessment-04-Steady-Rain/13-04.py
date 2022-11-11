"""
13-4. Steady Rain: Modify your code in Exercise 13-3 so that when a row of
raindrops disappears off the bottom of the screen, a new row appears at the
top of the screen and begins to fall.

Author:
https://github.com/Aemilus
"""

import sys

import pygame

from rain import Raindrops

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Raindrops")

raindrops = Raindrops(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((60, 60, 60))

    raindrops.draw(screen)
    raindrops.update()

    pygame.display.flip()

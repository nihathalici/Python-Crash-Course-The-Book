"""
13-3. Raindrops: Find an image of a raindrop and create a grid of raindrops.
Make the raindrops fall toward the bottom of the screen until they disappear.

Source:
https://github.com/Aemilus
"""
import sys
import pygame
from rain import Raindrops

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("CHPT-13-Assessment-03: Raindrops")

raindrops = Raindrops(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((60, 60, 60))

    raindrops.draw(screen)
    raindrops.update()

    pygame.display.flip()
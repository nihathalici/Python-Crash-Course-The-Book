# 14-2. Target Practice: Create a rectangle at the right edge of the screen
# that moves up and down at a steady rate. Then have a ship appear on the
# left side of the screen that the player can move up and down while firing
# bullets at the moving, rectangular target. Add a Play button that starts
# the game, and when the player misses the target three times, end the game
# and make the Play button reappear. Let the player restart the game with
# this Play button.

import sys
from time import sleep
import pygame
import pygame.font
from pygame.sprite import Sprite

class Screen:
    pass

class Ship:
    pass

class Bullet(Sprite):
    pass

class Box:
    pass

class Alien(Sprite):
    pass

class Button:
    pass

if __name__ == "__main__":
    screen = Screen()
    screen.run_game()

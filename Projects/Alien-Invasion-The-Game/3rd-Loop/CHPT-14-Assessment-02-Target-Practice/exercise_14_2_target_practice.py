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
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230, 230, 230)
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()

        self.ship = Ship(self.screen_rect)
        self.bullets = pygame.sprite.Group()

        self.box = Box(self)

        self.missed = 0
        self.game_active = False

        self.play_button = Button(self)
    
    def run_game(self):
        pass

    def ship_update(self):
        pass

    def _check_box_edges(self):
        pass

    def _check_bullet_hit(self):
        pass

    def _check_game_over(self):
        pass







class Ship:
    def __init__(self, screen_rect):
        pass

class Bullet(Sprite):
    def __init__(self, screen):
        pass

    def update(self):
        pass

    def draw_bullet(self):
        pass


class Box:
    def __init__(self, screen):
        pass

    def update(self):
        pass

    def draw_box(self):
        pass


class Alien(Sprite):
    def __init__(self, screen):
        pass

    def update(self):
        pass


class Button:
    def __init__(self, screen):
        pass
    

if __name__ == "__main__":
    screen = Screen()
    screen.run_game()

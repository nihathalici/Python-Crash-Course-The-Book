# Make a game that begins with a rocket in the center of the screen.
# Allow the player to move the rocket up, down, left, or right using the
# four arrow keys. Make sure the rocket never moves beyond any edge of
# the screen.

import pygame

from settings import Settings
from rocket import Rocket
import game_functions as gf

def rocket():
    """Init Pygame and run game functions and main loop"""
    pygame.init()
    r_settings = Settings()
    # Set up window, background, and title bar caption
    screen = gf.window(r_settings.screen_width,
                       r_settings.screen_height,
                       r_settings.caption)
    # Creating rocket object
    rocket = Rocket(r_settings, screen)

    while True:
        # Main game loop
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(r_settings, screen, rocket)

rocket()
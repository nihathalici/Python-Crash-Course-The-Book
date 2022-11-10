# Better Stars: You can make a more realistic star pattern by
# introducing randomness when you place each star. Recall that you can
# get a random number like this:

# from random import randint
# random_number = randint(-10,10)

# This code returns a random integer between –10 and 10. Using your code
# in Exercise 13-1, adjust each star’s position by a random amount.

import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf

def main():
    """Main game function"""
    # Init pygame and settings
    pygame.init()
    g_settings = Settings()

    # Create game window
    screen = gf.new_window(g_settings.screen_width,
                           g_settings.screen_height,
                           g_settings.caption)
    # Create stars group
    stars = Group()

    # Create star grid
    gf.create_star_grid(g_settings, screen, stars)

    # Game loop
    while True:
        gf.check_events()
        gf.update_screen(g_settings, screen, stars)

# Run game
main()







    




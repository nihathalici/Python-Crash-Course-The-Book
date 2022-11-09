"""
Stars: 
Find an image of a star. Make a grid of stars appear on the screen.
"""

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
        # Check events
        gf.check_events()

        # Update screen
        gf.update_screen(g_settings, screen, stars)


# Run game
main()

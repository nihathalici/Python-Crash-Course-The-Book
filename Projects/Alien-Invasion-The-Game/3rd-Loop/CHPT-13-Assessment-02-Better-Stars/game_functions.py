import sys
from random import randint
import pygame
from star import Star

def new_window(screen_width, screen_height, caption):
    """Create new game window"""
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(caption)
    return screen

def check_events():
    """Check for events, then determine what to do"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def get_number_stars_x(g_settings, star_width, spacing):
    """Determine number of stars in a row"""
    available_space_x = (g_settings.screen_width - spacing * star_width)
    number_stars = int(available_space_x / (spacing * star_width)) + 1
    return number_stars

def get_number_rows(g_settings, star_height, spacing):
    """Determine number of rows that fit in screen"""
    available_space_y = (g_settings.screen_height - spacing * star_height)
    number_rows = int(available_space_y / (spacing * star_height)) + 1
    return number_rows

def rand_displace(star):
    min = star.min_displace
    max = star.max_displace
    random_number = randint(min, max)
    return random_number

def create_star(g_settings, screen, stars,
                star_number, row_number, spacing):
    """Create star object"""
    star = Star(g_settings, screen)
    star_width = star.rect.width
    star_height = star.rect.height
    star.rect.x = ((star_width * (spacing - 1)) + spacing * 
                    star_width * star_number) + rand_displace(star)
    star.rect.y = ((star_height * (spacing - 1)) + spacing *
                    star_height * row_number) + rand_displace(star)
    stars.add(star)

def create_star_grid(g_settings, screen, stars):
    """Draw the entire star grid"""
    star = Star(g_settings, screen)
    spacing = star.spacing
    number_stars_x = get_number_stars_x(g_settings, star.rect.width, spacing)
    number_rows = get_number_rows(g_settings, star.rect.height, spacing)

    # Draw grid
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(g_settings, screen, stars, star_number, 
                         row_number, spacing)

def update_screen(g_settings, screen, stars):
    """Functions to run when refreshing screen"""
    # Set background color
    screen.fill(g_settings.bg_color)

    # Draw stars
    stars.draw(screen)

    # Draw fram
    pygame.display.flip()

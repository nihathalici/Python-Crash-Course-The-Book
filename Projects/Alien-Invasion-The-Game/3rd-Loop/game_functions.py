import sys
import pygame

def check_keydown_events(event, rocket):
    """Check keydown events for rocket movements"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    if event.key == pygame.K_DOWN:
        rocket.moving_down = True

def check_keyup_events(event, rocket):
    """Check keyup events for rocket movements"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    if event.key == pygame.K_LEFT:
        rocket.moving_left = False
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    if event.key == pygame.K_DOWN:
        rocket.moving_down = False

def check_events(rocket):
    """Functions for handling events"""
    # Start event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)
        

def window(width, height, caption):
    """Create window using width, height, and caption"""
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def update_screen(r_settings, screen, rocket):
    """Updates the screen and draws changes"""
    # Draw background
    screen.fill(r_settings.bg_color)

    # Draw ship
    rocket.blitme()
    # Refresh screen
    pygame.display.flip()

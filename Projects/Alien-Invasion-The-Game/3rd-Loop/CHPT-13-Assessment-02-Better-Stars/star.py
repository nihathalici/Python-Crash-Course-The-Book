import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Class to construct star objects"""

    def __init__(self, g_settings, screen):
        """Init variables needed"""
        super().__init__()
        # Init settings and screen
        self.g_settings = g_settings
        self.screen = screen

        # Set image and rects
        self.image = pygame.image.load('images/star3.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Set initial position and spacing
        self.spacing = g_settings.star_spacing_factor
        self.rect.x = self.rect.width * (self.spacing - 1)
        self.rect.y = self.rect.height * (self.spacing - 1)

        # Set displacement min and max
        self.min_displace = self.g_settings.star_displacement_factor[0]
        self.max_displace = self.g_settings.star_displacement_factor[1]
    
    def blitme(self):
        """Function to draw star object"""
        self.screen.blit(self.image, self.rect)

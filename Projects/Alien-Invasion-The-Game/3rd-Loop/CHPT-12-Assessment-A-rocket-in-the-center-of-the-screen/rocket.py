import pygame

class Rocket():
    """Stores and manipulates data for Rocket"""

    def __init__(self, r_settings, screen):
        """Initialize values for settings and screen"""
        self.r_settings = r_settings
        self.screen = screen
        # Setting up rocket
        self.image = pygame.image.load('blue_rocket.png')
        # Getting rects to get coordinates to center rocket
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        # Set moving variables to false
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        # Set speed factor and center for movement
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.speed_factor = r_settings.speed_factor


    def update(self):
        """Update position based on movement variables"""
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed_factor
        
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    
    def blitme(self):
        """Draws rocket to screen"""
        self.screen.blit(self.image, self.rect)

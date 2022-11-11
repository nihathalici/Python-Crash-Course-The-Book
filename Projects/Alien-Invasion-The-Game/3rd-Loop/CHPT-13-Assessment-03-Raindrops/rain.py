import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class Raindrop(Sprite):
    image = pygame.image.load("raindrop.png")
    rect = image.get_rect()
    width = rect.width
    height = rect.height
    border = 10
    fall_speed = 1

    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.rect = Raindrop.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.y += Raindrop.fall_speed

class Raindrops(Group):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.raindrops_per_row = int(self.screen.get_rect().width / (Raindrop.border + Raindrop.width))
        for col in range(2):
            for raindrop_number in range(self.raindrops_per_row):
                x = Raindrop.border * (1 + raindrop_number) + Raindrop.width * raindrop_number
                y = Raindrop.border * (1 + col) + Raindrop.height * col
                raindrop = Raindrop(self.screen, x, y)
                self.add(raindrop)

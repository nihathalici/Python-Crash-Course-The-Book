import sys
from time import sleep

import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        # Running the Game in Fullscreen Mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(self.settings.caption)

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make the play button.
        self.play_button_easy = Button(self, "Easy", (350, 400))
        self.play_button_normal = Button(self, "Normal", (600, 400))
        self.play_button_hard = Button(self, "Hard", (850, 400))
        self.play_buttons = []
        self.play_buttons.append(self.play_button_easy)
        self.play_buttons.append(self.play_button_normal)
        self.play_buttons.append(self.play_button_hard)

    def run_game(self):
        """Start the main loop for the game."""
        pass



if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

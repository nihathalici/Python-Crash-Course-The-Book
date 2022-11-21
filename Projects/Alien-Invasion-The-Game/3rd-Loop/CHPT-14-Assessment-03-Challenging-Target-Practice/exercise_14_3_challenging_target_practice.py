# 14-3. Challenging Target Practice: Start with your work from Exercise 14-2
# (page 285). Make the target move faster as the game progresses, and restart
# the target at the original speed when the player clicks Play.

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

        self.speed_scale = 1.0001

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.ship.ship_move_up = True
                    elif event.key == pygame.K_DOWN:
                        self.ship.ship_move_down = True
                    elif event.key == pygame.K_SPACE:
                        new_bullet = Bullet(self)
                        self.bullets.add(new_bullet)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.ship.ship_move_up = False
                    elif event.key == pygame.K_DOWN:
                        self.ship.ship_move_down = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_position = pygame.mouse.get_pos()
                    button_clicked = self.play_button.rect.collidepoint(
                        clicked_position)
                    if not self.game_active and button_clicked:
                        self.box.move_speed = 1
                        self.bullets.empty()
                        self.game_active = True

            if self.game_active:
                self.ship_update()
                self.bullets.update()
                self.box.update()
                self.box.increase_speed()
                self._check_bullet_hit()
                self._check_box_edges()

            self.screen.fill(self.screen_color)
            self.screen.blit(self.ship.image, self.ship.rect)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.box.draw_box()
            if not self.game_active:
                self.play_button.draw_button()
            pygame.display.flip()

    def ship_update(self):
        if self.ship.ship_move_up and self.ship.rect.y > 0:
            self.ship.rect.y -= self.ship.ship_speed
        if self.ship.ship_move_down \
                and self.ship.rect.bottom < self.screen_rect.bottom:
            self.ship.rect.y += self.ship.ship_speed

    def _check_box_edges(self):
        if self.box.rect.bottom >= self.screen_rect.bottom \
                or self.box.rect.top <= 0:
            self.box.move_direction *= -1
            print(self.box.move_direction)

    def _check_bullet_hit(self):
        collision = pygame.sprite.spritecollide(self.box, self.bullets, True)
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
                self.missed += 1
                self._check_game_over()

    def _check_game_over(self):
        if self.missed == 3:
            self.missed = 0
            self.game_active = False


class Ship:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.ship_speed = 1
        self.ship_move_up = False
        self.ship_move_down = False


class Bullet(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = self.screen.ship.rect.midright

    def update(self):
        self.rect.x += int(self.bullet_speed)

    def draw_bullet(self):
        pygame.draw.rect(self.screen.screen, self.bullet_color, self.rect)


class Box:
    def __init__(self, screen):
        self.screen = screen
        self.width = 60
        self.height = 200
        self.color = (0, 0, 255)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topright = self.screen.screen_rect.topright
        self.move_direction = 1
        self.move_speed = 1

    def update(self):
        self.rect.top += self.move_speed * self.move_direction

    def draw_box(self):
        pygame.draw.rect(self.screen.screen, self.color, self.rect)

    def increase_speed(self):
        self.move_speed *= self.screen.speed_scale

class Alien(Sprite):
    def __init__(self, screen):
        self.screen = screen
        super().__init__()
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.screen.alien_move_direction * \
            self.screen.alien_move_vertical_speed


class Button:
    def __init__(self, screen):
        self.screen = screen.screen
        self.screen_rect = screen.screen_rect

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg()

    def _prep_msg(self):
        self.msg_image = self.font.render(
            'Play!', True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


if __name__ == "__main__":
    screen = Screen()
    screen.run_game()

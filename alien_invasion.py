""" This is my version of Eric Matthes' Alien Invastion game, from his book "Python Crash Course"
"""

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Base/overall class to manage game assets and behavior
    """

    def __init__(self):
        """Initialize the game and create game resources
        """
        pygame.init()

        self.settings = Settings()

        # The following sets the screen width and height to the values defined in settings.py
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # self.screen = pygame.display.set_mode( (0,0), pygame.FULLSCREEN)
        # self.settings.screen_width  = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        # Set the screen's caption
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

        # Create the bullets
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        """ Create a fleet of aliens """
        # make an alien.
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Create the first row of aliens
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        # Create an alien. Place it in the row.
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + (2 * alien_width * alien_number)
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def run_game(self):
        """Start the game's main loop"""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            # Redraw the screen during each pass through the loop
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Respond to key presses
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Respond to key releases
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets on the screen and remove bullets that have disappeared
        """
        # Update visible bullets positions
        self.bullets.update()

        # Get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to new screen.
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


# Here's the driver
if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()

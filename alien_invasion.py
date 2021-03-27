"""
This is my version of Eric Matthes Alien Invasion game,
from his book Python Crash Course.
"""

import sys
from time import sleep

import pygame
from pygame.locals import *

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from sbship import SBship


class AlienInvasion:
    """Base/overall class to manage game assets and behavior
    """

    def __init__(self):
        """ Initialize the game and create game resources
        """
        pygame.init()
        self.settings = Settings()

        # The following sets the screen width and height to the values 
        # defined in settings.py
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Set the screen's caption
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.sb_ship = SBship(self)

        # Create the bullets
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Create the "Play" button
        self.play_button = Button(self, "Play")

        self.fps = self.settings.fps
        self.fpsClock = pygame.time.Clock()

    def _start_game(self):
        """ This is the processing required to start a new game """

        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_images()
        self.sb.prep_score()
        self.sb.prep_high_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Reset the game settings to their initial values.
        self.settings.initialize_dynamic_settings()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

    def _create_alien(self, alien_number, row_number):
        """ Create a single alien. Place it in the row."""

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2 * alien_width * alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
        self.aliens.add(alien)

    def _create_fleet(self):
        """ Create a fleet of aliens """

        # make an alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that will fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """ Respond appropriately if any aliens have reached an edge."""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Drop the entire alien fleet down the screen
             and change the fleet's direction."""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    # Keyboard and Play button handlers
    def _check_events(self):
        """ Respond to key presses and mouse events."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.update_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """ Start a new game when the player clicks 'Play'."""
        
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if ((button_clicked) and (not self.stats.game_active)):
            self._start_game()    
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """ Respond to key presses"""

        # Note that we simply reset the 
        # moving_rignt or moving_left flags
        # when the arrow keys are pressed.
        # the actual motion of our ship happens
        # when the arrow keys are released.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q: # Stop the game.
            self.stats.update_high_score()
            sys.exit()
        elif ((event.key == pygame.K_p) and (not self.stats.game_active)): # Start the game.
            self._start_game()    
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keyup_events(self, event):
        """ Respond to key releases
        """

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # Bullet processing
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Update position of bullets on the screen
             and remove old bullets.
        """
        # Update visible bullets positions
        self.bullets.update()

        # Get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # See if any of the bullets fired have hit an
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """ Respond to bullet-alien collisions."""

        # Check for any bullets that have hit aliens.
        #  If so, get rid of both the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # We need to clean up this level and start a new one.
            self._start_new_level()

    def _start_new_level(self):
        """ Destroys the existing bullets, creates a new fleet and increments the 
             current game level.
        """

        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase the level.
        self.stats.level += 1
        self.sb.prep_level()

    def _update_aliens(self):
        """ Check whether fleet is at an edge,
            then update the positions of all the aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """ Respond to the ship being hit by an alien."""

        # Decrement ships_left.
        self.stats.ships_left -= 1

        if self.stats.ships_left >= 0:
            # Decrement ships_left and update scoreboard.
            self.sb.prep_ships()
            
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            # Note that we only create one ship per game,
            # and re-use it up to the value of ship_limit.
            self._create_fleet()
            self.ship.center_ship()

             # Increase the level.
            self.stats.level += 1
            self.sb.prep_level()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """ Check to see whether any aliens have reached
             the bottom of the screen."""

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship were hit.
                self._ship_hit()
                break


    def _update_screen(self):
        """Update images on the screen, and flip to new screen.
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the "Play" button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        """ Start the game's main loop."""

        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            # Redraw the screen during each pass through the loop
            self._update_screen()
            self.fpsClock.tick(self.fps)

# Here's the driver
if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()

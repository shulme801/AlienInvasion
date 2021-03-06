""" This is my version of Eric Matthes' Alien Invastion game, from his book "Python Crash Course"
"""

import sys
import pygame

from settings import Settings
from ship     import Ship

class AlienInvasion:
    """Base/overall class to manage game assets and behavior
    """

    def __init__(self):
        """Initialize the game and create game resources
        """
        pygame.init()

        self.settings = Settings()

        self.screen   = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )

        # Set the screen's caption
        pygame.display.set_caption("Alien Invasion")

        self.ship  = Ship(self)

    def run_game(self):
        """Start the game's main loop
        """
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            # Redraw the screen during each pass through the loop
            self._update_screen()


    def _check_events(self):
        """Respond to keypresses and mouse events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to new screen.
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

# Here's the driver
if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
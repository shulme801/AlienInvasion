""" Scoreboard Ship information -- allows us to use a small image to represent number of ships left
"""

import pygame
from pygame.sprite import Sprite

class SBship(Sprite):
    """ A class to manage the scoreboard ship icon."""

    def __init__(self, ai_game):
        """ Initialize the scoreboard ship icon."""

        # Make sure that ship inherits everything from Sprite by calling 
        #  Sprite's init.
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect.
        self.image   = pygame.image.load('images/falcon-ship_tiny.bmp')
        self.rect    = self.image.get_rect()
        
        # store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

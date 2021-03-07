""" Class to provide all settings needed by AlienInvasion game
"""

class Settings:
    """ A class to hold all settings for Alien Invasion
    """

    def __init__(self):
        """ Initialize the game's settings
        """
        # Screen settings
        self.screen_width    = 1400 #pixels
        self.screen_height   = 800
        self.bg_color        = (230, 230, 230)

        self.ship_speed      = 2.5

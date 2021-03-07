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

        # Ship settings
        self.ship_speed      = 2.5

        # Bullet settings
        self.bullet_speed    = 1.5
        self.bullet_width    = 3
        self.bullet_height   = 15
        self.bullet_color    = (60,60,60)
        self.bullets_allowed = 7
        
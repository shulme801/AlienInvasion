""" Class to provide all settings needed by AlienInvasion game
"""

class Settings:
    """ A class to hold all settings for Alien Invasion
    """

    def __init__(self):
        """ Initialize the game's settings
        """
        # Screen settings
        self.screen_width    = 1200 #pixels
        self.screen_height   = 800
        self.bg_color        = (230, 230, 230)

        # Ship settings
        self.ship_speed      = 5.0
        self.ship_limit      = 3

        # Bullet settings
        self.bullet_speed    = 3.5
        self.bullet_width    = 3
        self.bullet_height   = 15
        self.bullet_color    = (60,60,60)
        self.bullets_allowed = 7

        # Alien settings
        self.alien_speed = 1.5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Display settings
        self.fps = 60
        
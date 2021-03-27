import os.path
from os import path

class GameStats:
    """ Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """ Initialize statistics."""

        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start Alien Invasion in an inactive state.
        self.game_active = False

        self.high_score = self._read_high_score()
        
    def _read_high_score(self):
        high_score_file = 'high_score.txt'
        if (path.isfile(high_score_file)):
            try:
                f = open(high_score_file, "r")
            except EOFError as ex:
                print("Caught the EOF error when opening file {0}".format(str(file)))
                raise ex
            except IOError as eio:
                print("Caught the IOError when opening file {0}".format(str(file)))
                raise eio
            except:
                print("Caught an unknown error with file {0}".format(str(file)))
            else:
                all_time_high = int(f.read())
                f.close()
                return(all_time_high)
        else:
            return(0)
        
    def _write_high_score(self, new_high):
        """ Write the new high score to the high_score.txt file.
        """

        high_score_file = "high_score.txt"

        try:
            f = open(high_score_file, "w")
        except:
            print("Some unknown error while trying to write to empty high_score.txt")
        else:
            f.write(new_high)
            f.close()


    def update_high_score(self):
        """ If the current high score is greater than the all time high score,
            write the current high score to the high_score.txt file.
        """

        old_high = self._read_high_score()
        if self.high_score > old_high:
            self._write_high_score(str(self.high_score))
  
        

    def reset_stats(self):
        """ Initialize statistics that can change during game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
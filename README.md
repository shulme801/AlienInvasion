# AlienInvasion

## Alien Invasion Game

### Adapted from _Python Crash Course_ by Eric Matthes

In ***Alien Invasion***, the player controls a rocket ship that appears at the bottom center of the screen. The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen.  

The player shoots in order to (one hopes) destroy the aliens. If the player shoots all the aliens, a new fleet appears.  This new fleet moves faster than the previous fleet.

If any alien hits the player's ship or reaches the bottom of the screen, the player loses a ship. If the player loses three ships, the game ends.

My version of the game implements Mr. Matthes' suggested extension (p. 301) to add a persistent "All Time High" score.

[Readme text adapted from _Python Crash Course,_ p. 228]

## Tweaks and Tips (in no particular order)

* I used VS Code on my Mac as an IDE for python.  I experimented with pycharm, but found I preferred VS Code for its markdown extensions.  It's not the python IDE that pycharm is, but -- perhaps because I am more used to it -- I found VS code enabled improved productivity.
* But VS Code has a few issues! When I first began this project I received some mysterious errors from pylint, to tell me that "Module pygame has no 'init' member.  Yet, my code ran with no errors.
  * It turns out that this behavior is a security measure designed to alert you to the loading of C extensions that aren't part of the python stdlib (see [Stack Overflow](https://stackoverflow.com/questions/50569453/why-does-it-say-that-module-pygame-has-no-init-member)).
  * The fix suggested in Stack Overflow is this: **white-list the python extension** (e.g. 'pygame') in the python settings.json file that VS Code uses.
    * From the Mac menu, click on File->Preferences->Settings, and scroll down to Python. Once there, pick any of the json links. Edit the json file.
* I didn't like the size and shape of the standard "Ship" image.  It was too small, I felt, and lacked detail and "realism".  So I've used a more detailed free spaceship image from webstockreview.net.  This is the "Falcon" space ship.
* As designed, the "standard" AlienInvasion uses one ship image -- the one loaded into the "Ship" class on startup.  This single image becomes the player's spaceship for fighting aliens (the "combat" ship).  This same image is also desplayed (multiple times) on the upper left hand side of the scoreboard to track the number of unused ships remaining.  
  * This limitation of a single ship image constrains the size of the ship image used for combat.  The combat ship image can be no larger than that which can be displayed multiple times in the scoreboard.
  * When I changed the combat ship image to the Falcon ship, I found that it was too big to display in the scoreboard.  
  * Rather than reduce the size of my combat ship, I built a new class -- SBships -- that contained a miniature image of the Falcon space ship.  I use SBships to represent the number of ships remaining.
  * Moreover, the Scoreboard ship fulfills a completely different function than the combat ship. It makes sense to manage it in a separate class.
* Frames Per Second setting.
  * My development system is an MBP 2019 version, with a 2.4 gHz I5 processor.  When the alien fleet was repositioned, the redrawing of the games window was frequently quite choppy. The computer's processor is fast enough that it redrew the screen too quickly.
  * I fixed this by adding an fpsClock instance attribute to my AlienInvasion class, setting it to pygame.time.Clock() in the init method.
  * I also added a frames per second ("fps") to the Settings class.  
  * Now, immediately after updating the display at the end of the game loop, I call the Clock object's "tick()" method to force a slight pause, if needed.

## License Information

The software and sample data in this repository is licensed under GNU General Public License v3.0. See license.md in this repository. No closed-source or commercial use is allowed.

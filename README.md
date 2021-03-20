# AlienInvasion

## Alien Invasion Game

### Adapted from _Python Crash Course_ by Eric Matthes

In ***Alien Invasion***, the player controls a rocket ship that appears at the bottom center of the screen. The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen.  

The player shoots in order to (one hopes) destroy the aliens. If the player shoots all the aliens, a new fleet appears.  This new fleet moves faster than the previous fleet.

If any alien hits the player's ship or reaches the bottom of the screen, the player loses a ship. If the player loses three ships, the game ends.

[Readme text adapted from _Python Crash Course,_ p. 228]

## Tweaks and Tips (in no particular order)

* I originally used VS Code on my Mac as an IDE for python.  When I first began this project I received some mysterious errors from pylint, to tell me that "Module pygame has no 'init' member.  Yet, my code ran with no errors.
    * It turns out that this behavior is a security measure designed to alert you to the loading of C extensions that aren't part of the python stdlib (see [Stack Overflow](https://stackoverflow.com/questions/50569453/why-does-it-say-that-module-pygame-has-no-init-member)).
  * The fix suggested in Stack Overflow is this: **white-list the python extension** (e.g. 'pygame') in the python settings.json file that VS Code uses.
    * From the Mac menu, click on File->Preferences->Settings, and scroll down to Python. Once there, pick any of the json links. Edit the json file.
* I've added a couple free spaceship images from webstockreview.net.
* Frames Per Second setting.
  My development system is an MBP 2019 version, with a 2.4 gHz I5 processor.  When the alien fleet was repositioned, the redrawing of the games window was frequently quite choppy.
  The computer's processor is fast enough that it redrew the screen too quickly.
  I fixed this by adding an fpsClock instance attribute to my AlienInvasion class, setting it to pygame.time.Clock() in the __init__. 
  I also added a frames per second ("fps") to the Settings class.  Now, immediately after updating the display at the end of the game
  loop, I call the Clock object's "tick()" method to force a slight pause, if needed.
* I'm now using PyCharm (the paid version) under JetBrains' 30 day trial to see whether I prefer it.

## License Information

The software and sample data in this repository is licensed under GNU General Public License v3.0. See license.md in this repository. No closed-source or commercial use is allowed.

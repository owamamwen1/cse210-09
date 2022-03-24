import pygame
import game.shared.gamecontants as gameconstants

from game.shared.point import Point


class KeyboardService:
    """Detects player input. 

    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
    """

    def __init__(self):
        """Constructs a new KeyboardService.

        Args:
        """
        self._dx = 0
        self._dy = 0

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        self._dx = 0
        self._dy = 0

        keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

        if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
            self._dx = -3

        if keys[pygame.K_RIGHT]:
            self._dx = 3

        if keys[pygame.K_UP]:
            self._dy = -3

        if keys[pygame.K_DOWN]:
            self._dy = 3

        direction = Point(self._dx, self._dy)

        return direction

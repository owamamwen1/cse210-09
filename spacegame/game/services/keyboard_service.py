import pygame
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 

    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
    """

    def __init__(self, velocity = 5):
        """Constructs a new KeyboardService.

        Args:
        """
        self._dx = 0
        self._dy = 0
        self._velocity = velocity

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        self._dx = 0
        self._dy = 0

        # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:  # We can check if a key is pressed like this
            self._dx = self._velocity * -1

        if keys[pygame.K_RIGHT]:
            self._dx = self._velocity

        if keys[pygame.K_UP]:
            self._dy = self._velocity * -1

        if keys[pygame.K_DOWN]:
            self._dy = self._velocity

        direction = Point(self._dx, self._dy)

        return direction

    def set_velocity(self, vel):
        print(vel)
        self._velocity = vel

    def is_shooting(self):
        """
        """
        keys = pygame.key.get_pressed()
        return keys[pygame.K_SPACE]

from game.shared.point import Point
from game.shared.gamecontants import *
import pygame


class Actor:
    """A visible, moveable thing that participates in the game. 

    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._image = pygame.image.load(ACTOR_IMAGE)

    def getImage(self):
        return self._image

    def get_position(self):
        """Gets the actor's position in 2d space.

        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position

    def get_velocity(self):
        """Gets the actor's speed and direction.

        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def move_next(self, max_x, max_y):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.

        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

    def setImage(self, image):
        self._image = image

    def set_position(self, position):
        """Updates the position to the given one.

        Args:
            position (Point): The given position.
        """
        self._position = position

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.

        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity

from game.shared.point import Point
from game.shared.gameconstants import *
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

    def get_image(self):
        return self._image
    
    def get_image_height(self):
        return self._image.get_height()
    
    def get_image_width(self):
        return self._image.get_width()

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

    def get_center(self):
        """Gets the actor's center point.

        Returns:
            Point: The actor's center point.
        """
        pos_x = self._position.get_x() + (self.get_image_width() / 2)
        pos_y = self._position.get_y() + (self.get_image_height() / 2)
        return Point(pos_x, pos_y)

    def move_next(self, max_x, max_y):
        """Moves the actor to its next position according to its velocity.

        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x())
        y = (self._position.get_y() + self._velocity.get_y())

        self._position = Point(x, y)

    def set_image(self, image):
        self._image = pygame.image.load(image)

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
    
    def set_center(self, pos):
        """Sets the actor's center point ate the given position.

        Args:
            Point: The desired position for the actor's center.
        """
        pos_x = pos.get_x() - (self.get_image_width() / 2)
        pos_y = pos.get_y() - (self.get_image_height() / 2)
        self._position = Point(pos_x, pos_y)


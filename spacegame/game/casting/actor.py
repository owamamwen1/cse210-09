from game.shared.point import Point
from game.shared.gameconstants import *



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
        self._image = ACTOR_IMAGE
        self._enemy_image = ENEMY_IMAGE

    def get_image(self):
        return self._image
    
    def get_enemy_image(self):
        return self._enemy_image

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

    def move_next(self, max_x, max_y):
        """Moves the actor to its next position according to its velocity.

        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        pos_x = self._position.get_x()
        pos_y = self._position.get_y()
        vel_x = self._velocity.get_x()
        vel_y = self._velocity.get_y()
        image_width = self.get_image_width()
        image_height = self.get_image_height()

        if (pos_x + vel_x + image_width > max_x):
            x = max_x - image_width
        elif (pos_x + vel_x < 0):
            x = 0
        else:
            x = (pos_x + vel_x)

        if (pos_y + vel_y + image_height > max_y):
            y = max_y - image_height
        elif (pos_y + vel_y < 0):
            y = 0
        else:
            y = (pos_y + vel_y)

        self._position = Point(x, y)

    def set_image(self, image):
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

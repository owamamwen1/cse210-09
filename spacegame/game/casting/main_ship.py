from game.casting.ship import Ship
from game.services.keyboard_service import KeyboardService
from game.shared.gameconstants import *
from game.shared.point import Point


class Main_ship(Ship):
    """
    """

    def __init__(self, pos = Point(0, 0), image = ACTOR_IMAGE, health = 500, vector_vel = 6, shoot_rate = .2):
        """
        """
        super().__init__(pos, image, health, vector_vel, shoot_rate)
        self.set_center(pos)
        self._keyboard_service = KeyboardService(self._vector_vel)

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

    def set_vector_vel(self, vel):
        """
        """
        super().set_vector_vel(vel)
        self._keyboard_service.set_velocity(vel)

    def get_direction(self):
        """
        """
        velocity = self._keyboard_service.get_direction()
        return velocity

    def is_shooting(self):
        """
        """
        return self._keyboard_service.is_shooting()

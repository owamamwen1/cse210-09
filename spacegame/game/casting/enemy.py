from game.casting.ship import Ship
from game.shared.gamecontants import *
from game.shared.point import Point
import random

class Enemy(Ship):
    """
    """

    def __init__(self, pos = Point(0, 0), image = ENEMY_IMAGE, health = 30, vector_vel = 3, shoot_rate = .5):
        """"""
        super().__init__(pos, image, health, vector_vel, shoot_rate)
        self._go_to = self.get_random_point(MAX_X, MAX_Y)

    def move_next(self, max_x, max_y):
        """Moves the actor to its next position according to its velocity.

        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        go_x = self._go_to.get_x()
        go_y = self._go_to.get_y()
        pos_x = self._position.get_x()
        pos_y = self._position.get_y()
        vel_x = 0
        vel_y = 0

        if (go_x - 2 > pos_x):
            vel_x = self._vector_vel
        elif (go_x + 2 < pos_x):
            vel_x = self._vector_vel * -1
        else:
            vel_x = 0

        if (go_y - 2 > pos_y):
            vel_y = self._vector_vel
        elif (go_y + 2 < pos_y):
            vel_y = self._vector_vel * -1
        else:
            vel_y = 0

        self._position = Point(pos_x + vel_x, pos_y + vel_y)

        if self.is_close_enough(self._vector_vel * 2):
            self._go_to = self.get_random_point(max_x, max_y)

    def get_random_point(self, max_x, max_y):
        """
        """
        start_x = int(max_x / 2)
        end_x = (max_x - self.get_image_width())
        start_y = 0
        end_y = (max_y - self.get_image_height())

        pos_x = random.randrange(start_x, end_x)
        pos_y = random.randrange(start_y, end_y)

        return Point(pos_x, pos_y)

    def is_close_enough(self, tolerance):
        """
        """
        go_x = self._go_to.get_x()
        go_y = self._go_to.get_y()
        pos_x = self._position.get_x()
        pos_y = self._position.get_y()

        return tolerance ** 2 > (go_x - pos_x) ** 2 + (go_y - pos_y) ** 2

from game.casting.actor import Actor
from game.shared.gamecontants import *
from game.shared.point import Point
import pygame
import time
import random

class Enemy(Actor):
    """
    """

    def __init__(self, pos = Point(0,0)):
        """
        """
        super().__init__()
        self.set_image(pygame.image.load(ENEMY_IMAGE))
        self._position = pos
        self._dead = False
        self._t = time.perf_counter()
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
            vel_x = +3
        elif (go_x + 2 < pos_x):
            vel_x = -3
        else:
            vel_x = 0

        if (go_y - 2 > pos_y):
            vel_y = +3
        elif (go_y + 2 < pos_y):
            vel_y = -3
        else:
            vel_y = 0

        self._position = Point(pos_x + vel_x, pos_y + vel_y)

        if self.is_close_enough(5):
            self._go_to = self.get_random_point(max_x, max_y)

    def get_random_point(self, max_x, max_y):
        """"""
        start_x = int(max_x / 2)
        end_x = (max_x - self.get_image_width())
        start_y = 0
        end_y = (max_y - self.get_image_height())

        pos_x = random.randrange(start_x, end_x)
        pos_y = random.randrange(start_y, end_y)

        return Point(pos_x, pos_y)

    def is_close_enough(self, tolerance):
        """"""
        go_x = self._go_to.get_x()
        go_y = self._go_to.get_y()
        pos_x = self._position.get_x()
        pos_y = self._position.get_y()

        return tolerance ** 2 > (go_x - pos_x) ** 2 + (go_y - pos_y) ** 2

    def die(self):
        """
        """
        self._dead = True

    def is_recharged(self):
        t_now = time.perf_counter()
        diff = t_now - self._t
        return diff > .5

    def uncharge(self):
        self._t = time.perf_counter()

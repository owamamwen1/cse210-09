import pygame

from game.services.keyboard_service import KeyboardService
from game.shared.point import Point


class KeyboardServiceFlex(KeyboardService):
    """
    """

    def __init__(self, key_set_num = 0):
        """
        """
        super().__init__()

        self._key_sets = {
            0 : {'l':pygame.K_LEFT, 'r':pygame.K_RIGHT, 'u':pygame.K_UP, 'd':pygame.K_DOWN},
            1 : {'l':pygame.K_a, 'r':pygame.K_d, 'u':pygame.K_w, 'd':pygame.K_s},
            2 : {'l':pygame.K_f, 'r':pygame.K_h, 'u':pygame.K_t, 'd':pygame.K_g},
            3 : {'l':pygame.K_j, 'r':pygame.K_l, 'u':pygame.K_i, 'd':pygame.K_k},
            4 : {'l':pygame.K_KP4, 'r':pygame.K_KP6, 'u':pygame.K_KP8, 'd':pygame.K_KP5}
        }

        self.set_keys(key_set_num)


    def set_keys(self, key_set_num):
        """
        """
        self._left  = self._key_sets[key_set_num]['l']
        self._right = self._key_sets[key_set_num]['r']
        self._up    = self._key_sets[key_set_num]['u']
        self._down  = self._key_sets[key_set_num]['d']


    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """

        keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

        self._dx = 0
        self._dy = 0

        if keys[self._left] and self._dx != 1:
            self._dx = -3
            self._dy = 0

        if keys[self._right] and self._dx != -1:
            self._dx = 3
            self._dy = 0

        if keys[self._up] and self._dy != 1:
            self._dx = 0
            self._dy = -3

        if keys[self._down] and self._dy != -1:
            self._dx = 0
            self._dy = 3

        direction = Point(self._dx, self._dy)

        return direction

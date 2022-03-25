from game.shared.gamecontants import *

from game.casting.cast import Cast
from game.casting.cycle import Cycle

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.display_service import DisplayService

from game.shared.color import Color
from game.shared.point import Point


def main():

    # create the cast
    cast = Cast()

    # The next line is just a facy way of positioning proportionally to the screen size.
    position = Point(int(MAX_X / 3),
                     int(MAX_Y / 2))
    cycle1 = Cycle(position, 1)
    cycle1.set_velocity(Point(0, 0))
    cast.add_actor("cycle1", cycle1)

    position = Point(int(MAX_X / 3 * 2),
                     int(MAX_Y / 2))
    cycle2 = Cycle(position, 3)
    cycle2.set_velocity(Point(0, 0))
    cast.add_actor("cycle2", cycle2)

    # start the game
    keyboard_service = KeyboardService()
    display_service = DisplayService(
        CAPTION.format(CENTER), MAX_X, MAX_Y, FRAME_RATE)
    director = Director(keyboard_service, display_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()

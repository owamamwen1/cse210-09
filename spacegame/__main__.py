from game.shared.gamecontants import *
from game.casting.cast import Cast
from game.casting.main_ship import Main_ship
from game.casting.banner import Banner
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.display_service import DisplayService
from game.shared.point import Point


def main():

    # create the cast
    cast = Cast()

    # The next line is just a facy way of positioning proportionally to the screen size.
    position = Point(int(MAX_X / 20), int(MAX_Y / 2))
    player_ship = Main_ship(position)
    cast.add_actor("player_ship", player_ship)

    # The health banner
    health_banner = Banner(Point(0,0),'Health:')
    cast.add_actor("health_banner", health_banner)

    # The score banner
    score_banner = Banner(Point(0,0),'Score: 0')
    score_banner.set_position(Point(MAX_X - score_banner.get_image_width(), 0))
    cast.add_actor("score_banner", score_banner)

    # start the game
    keyboard_service = KeyboardService()
    display_service = DisplayService(
        CAPTION.format(CENTER), MAX_X, MAX_Y, FRAME_RATE)
    director = Director(keyboard_service, display_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()

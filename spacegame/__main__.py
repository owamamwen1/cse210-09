from game.shared.gameconstants import *
from game.casting.cast import Cast
from game.casting.main_ship import Main_ship
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.display_service import DisplayService
from game.shared.point import Point
from game.casting.enemies import Enemies

def main():

    # create the cast
    cast = Cast()

    # The next line is just a fancy way of positioning proportionally to the screen size.
    position = Point(int(MAX_X / 20), int(MAX_Y / 2))
    player_ship = Main_ship(position, 0)
    player_ship.set_velocity(Point(0, 0))
    cast.add_actor("player_ship", player_ship)
    
    position = Point(int(MAX_X - 100), int(MAX_Y // 2))
    enemy_ship = Enemies(position, 0)
    enemy_ship.set_velocity(Point(0, 0))
    cast.add_actor("enemy_ships", enemy_ship)

    # start the game
    keyboard_service = KeyboardService()
    display_service = DisplayService(
        CAPTION.format(CENTER), MAX_X, MAX_Y, FRAME_RATE)
    director = Director(keyboard_service, display_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()

from hashlib import new
from game.casting.bullet import Bullet
from game.casting.enemy import Enemy
from game.shared.point import Point

import pygame
import time
import random



class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _display_service (DisplayService): For providing display output.
    """

    def __init__(self, keyboard_service, display_service):
        self._SCORE = 600
        self.__game_over = False
        """Constructs a new Director using the specified keyboard and display services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            display_service (DisplayService): An instance of DisplayService.
        """
        self._keyboard_service = keyboard_service
        self._display_service = display_service

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._display_service.open_window()
        self._init_t = time.perf_counter()
        self._enemy_t = time.perf_counter()

        run = True
        frame_duration = self._display_service.get_frame_duration() # Here we get the duration of each frame (in milliseconds).

        while run:
            pygame.time.delay(frame_duration) # This line determines the time of each frame (actually it says to the program to wait a certain amout of time before executing the next steps).
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
            if self._is_over():
                run = False
                self.__game_over = False # Not sure if this line here is necessary

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the players.

        Args:
            cast (Cast): The cast of actors.
        """

        player_ship = cast.get_first_actor("player_ship")
        vel = player_ship.get_direction()
        player_ship.set_velocity(vel)


    def _do_updates(self, cast):
        """Updates the players' positions and resolves any collisions with trails.

        Args:
            cast (Cast): The cast of actors.
        """
        player_ship = cast.get_first_actor("player_ship")

        max_x = self._display_service.get_width()
        max_y = self._display_service.get_height()
        player_ship.move_next(max_x, max_y)

        if (time.perf_counter() - self._enemy_t > 3):
            new_enemy = Enemy()
            pos_x = max_x
            pos_y = random.randrange(0,max_y - new_enemy.get_image_height())
            new_enemy.set_position(Point(pos_x, pos_y))
            cast.add_actor("enemies", new_enemy)
            self._enemy_t = time.perf_counter()

        if (player_ship.is_shooting() and player_ship.is_recharged()):
            new_bullet = Bullet(player_ship.get_center(), 0)
            cast.add_actor("player_bullets", new_bullet)
            player_ship.uncharge()

        player_bullets = cast.get_actors("player_bullets")
        for bullet in player_bullets:
            bullet.move_next(max_x, max_y)
            if (bullet.get_position().get_x() > max_x):
                cast.remove_actor("player_bullets", bullet)
        #    if (COLIDING WITH ENEMY):
        #        REMOVE LIFE FROM ENEMY
        #        DELETE BULLET

        enemies = cast.get_actors("enemies")
        for enemy in enemies:
            enemy.move_next(max_x, max_y)
            for bullet in player_bullets:
                if (self.check_collision(bullet, enemy)):
                    try:
                        cast.remove_actor("enemies", enemy)
                    except:
                        print('Could not delete ' + str(enemy))

                    try:
                        cast.remove_actor("player_bullets", bullet)
                    except:
                        print('Could not delete ' + str(bullet))
    # The game over

    def _is_over(self):
        return self.__game_over

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        actors = cast.get_all_actors()
        self._display_service.draw_actors(actors)

    def check_collision(self, actor1, actor2):
        """"""
        # Top actor 1
        top_1 = actor1.get_position().get_y()
        # Bottom actor 1
        bottom_1 = top_1 + actor1.get_image_height()
        # Left actor 1
        left_1 = actor1.get_position().get_x()
        # Right actor 1
        right_1 = left_1 + actor1.get_image_width()


        # Top actor 2
        top_2 = actor2.get_position().get_y()
        # Bottom actor 2
        bottom_2 = top_2 + actor2.get_image_height()
        # Left actor 2
        left_2 = actor2.get_position().get_x()
        # Right actor 2
        right_2 = left_2 + actor2.get_image_width()

        #print("top_1 " + str(top_1) + "   bottom_1 " + str(bottom_1) + "   left_1 " + str(left_1) + "   right_1 " + str(right_1) + "   top_2 " + str(top_2) + "   bottom_2 " + str(bottom_2) + "   left_2 " + str(left_2) + "   right_2 " + str(right_2))

        if (actor1.get_image_height() > actor2.get_image_height()):
            temp = top_1
            top_1 = top_2
            top_2 = temp
            temp = bottom_1
            bottom_1 = bottom_2
            bottom_2 = temp

        if (actor1.get_image_width() > actor2.get_image_width()):
            temp = left_1
            left_1 = left_2
            left_2 = temp
            temp = right_1
            right_1 = right_2
            right_2 = temp

        check1 = top_1 >= top_2 and top_1 <= bottom_2
        check2 = right_1 <= right_2 and right_1 >= left_2
        check3 = bottom_1 >= top_2 and bottom_1 <= bottom_2
        check4 = left_1 <= right_2 and left_1 >= left_2

        #print(str(check1) + " " + str(check2) + " " + str(check3) + " " + str(check4))

        return ((check1 and check2) or (check2 and check3) or (check3 and check4) or (check4 and check1))

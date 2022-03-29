from game.casting.bullet import Bullet
from game.shared.gameconstants import *
import pygame


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

        if (player_ship.is_shooting() and player_ship.is_recharged()):
            new_bullet = Bullet(player_ship.get_position(), 0)
            
            cast.add_actor("player_bullets", new_bullet)
            Bullet.ACTOR_SOUND.play()
            #player_ship.uncharge() # Set slow fire rate
            

        player_bullets = cast.get_actors("player_bullets")
        for bullet in player_bullets:
            bullet.move_next(max_x, max_y)
        #    if (COLIDING WITH ENEMY):

        #        REMOVE LIFE FROM ENEMY
        #        DELETE BULLET
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
        
        
        
        



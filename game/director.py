
class Director:
    """A person who directs the game."""

    def __init__(self, video_service, keyboard_control):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service 
        self._keyboard_control = keyboard_control

        pass
        
        
    def start_game(self, cast):
        """Starts the game. Runs the main game loop."""
        self._video_service.is_window_open()
        while self._video_service.is_window_open():
            self._do_inputs(cast)
            print ("open")
        self._video_service.close_window()    
        

    def _do_inputs(self, cast):
        
        ship = cast.get_first_actor("ship")
        velocity = self._keyboard_control.get_direction()
        ship.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                message = artifact.get_message()
                banner.set_text(message)    
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()    
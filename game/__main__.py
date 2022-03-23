from director import Director
from services.video_service import VideoService
from services.keyboard_control import KeyboardService
from body.cast import Cast
from score import Score
# The main function call other functions to run
# This mean one entry point


def main():

    cast = Cast()
    video_service = VideoService()
    keyboard_control = KeyboardService() 
    # cast.add_actor(cast)
    cast.add_actor("scores", Score())

    director = Director(video_service, keyboard_control)
    director.start_game(cast)

if __name__ == "__main__":
    main()
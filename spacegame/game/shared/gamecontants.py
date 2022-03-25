from pathlib import Path

from game.shared.color import Color
# import Path

FRAME_RATE = 50
MAX_X = 800
MAX_Y = 600
FONT_SIZE = 20
PLAYER_SIZE = 15
CENTER = "center"
COLS = 60
ROWS = 40
CAPTION = "Space Game"
WHITE = Color(255, 255, 255)

ACTOR_IMAGE = Path(__file__).parent.parent.parent / "assets/images/actor.png"
BACK_GROUND_IMAGE = Path(__file__).parent.parent.parent /"assets/images/background.webp"
LOGO_IMAGE = Path(__file__).parent.parent.parent / "assets/images/logo.png"


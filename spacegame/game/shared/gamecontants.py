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
BULLET_IMAGE = Path(__file__).parent.parent.parent / "assets/images/bullet.png"
BULLET_ENEMY_IMAGE = Path(__file__).parent.parent.parent / "assets/images/bullet_enemy.png"

# Sounds for the game
ACTOR_SOUND = Path(__file__).parent.parent.parent / "assets/sounds/actor_shoot_sound.mp3"
BACK_GROUND_SOUND = Path(__file__).parent.parent.parent / "assets/sounds/background_sound.mp3"

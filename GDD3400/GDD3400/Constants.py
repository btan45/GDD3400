from Vector import Vector
# Constants file
# World constants
FRAME_RATE = 60
WORLD_WIDTH = 800
WORLD_HEIGHT = 600
I_FRAMES = 120
FLASHING_FRAMES = 5
BACKGROUND_COLOR = (100, 149, 237)
LINE_COLOR = (0, 0, 255)
SEEKING_LINE_COLOR = (255, 0, 0)

# Player constants
PLAYER_COLOR = (255, 255, 0)
PLAYER_POSITION = Vector(400, 300)
PLAYER_SIZE = 10
PLAYER_SPEED = 5.5

# Enemy constants
ENEMY_COLOR = (0, 255, 0)
ENEMY_I_FRAME_COLOR = (255, 255, 255)
ENEMY_POSITION = Vector(100, 100)
ENEMY_SIZE = 10
ENEMY_SPEED = 5
ATTACK_RANGE = 200

# Math Constants
ZERO_VECTOR = Vector(0, 0)
UP_VECTOR = Vector(0, -1)
DOWN_VECTOR = Vector(0, 1)
LEFT_VECTOR = Vector(-1, 0)
RIGHT_VECTOR = Vector(1, 0)
UPPER_LEFT_VECTOR = Vector(-1, -1).normalize()
LOWER_LEFT_VECTOR = Vector(-1, 1).normalize()
LOWER_RIGHT_VECTOR = Vector(1, 1).normalize()
UPPER_RIGHT_VECTOR = Vector(1, -1).normalize()
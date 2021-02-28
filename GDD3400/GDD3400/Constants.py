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
PLAYER_SIZE = Vector(10, 10)
PLAYER_SPEED = 5

# Enemy constants
NUM_ENEMIES = 30
ENEMY_COLOR = (0, 255, 0)
ENEMY_HUNTER_COLOR = (255, 0, 255)
ENEMY_I_FRAME_COLOR = (255, 255, 255)
ENEMY_POSITION = Vector(100, 100)
ENEMY_SIZE = Vector(10, 10)
ENEMY_SPEED = 5
ATTACK_RANGE = 200

# Dog constants
DOG_INITIAL_SPEED = 5
DOG_MAX_SPEED = 10

# Sheep constants
SHEEP_SIZE = Vector(16, 32)
SHEEP_INITIAL_SPEED = 5
SHEEP_MAX_SPEED = 5
SHEEP_NEIGHBOR_RADIUS = 100
SHEEP_BOUNDARY_RADIUS = 50
SHEEP_ALIGNMENT_WEIGHT = 0.3
SHEEP_SEPARATION_WEIGHT = 0.325
SHEEP_COHESION_WEIGHT = 0.3
SHEEP_DOG_INFLUENCE_WEIGHT = 0.2
SHEEP_BOUNDARY_INFLUENCE_WEIGHT = 0.2
MIN_ATTACK_DIST = 200
BOUNDING_COLOR = (0, 0, 0)

# Debugging Behavior
DEBUGGING = False
DEBUG_LINE_WIDTH = 3
DEBUG_BOUNDING_RECTS = DEBUGGING
DEBUG_VELOCITY = DEBUGGING
DEBUG_NEIGHBORS = DEBUGGING
DEBUG_BOUNDARIES = DEBUGGING
DEBUG_DOG_INFLUENCE = DEBUGGING

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
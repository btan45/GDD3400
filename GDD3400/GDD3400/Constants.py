from Vector import Vector

# Constants file
# World constants
FRAME_RATE = 60
WORLD_WIDTH = 1024
WORLD_HEIGHT = 768
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
NUM_ENEMIES = 10
ENEMY_COLOR = (0, 255, 0)
ENEMY_HUNTER_COLOR = (255, 0, 255)
ENEMY_I_FRAME_COLOR = (255, 255, 255)
ENEMY_POSITION = Vector(100, 100)
ENEMY_SIZE = Vector(10, 10)
ENEMY_SPEED = 5
ATTACK_RANGE = 200

# Dog constants
DOG_INITIAL_SPEED = 5
DOG_MAX_SPEED = 5
DOG_POSITION = Vector(400, 300)
DOG_SIZE = Vector(10, 10)

# Sheep constants
NUM_SHEEP = 1
SHEEP_VELOCITY_COLOR = (0, 255, 0)
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
SHEEP_VELOCITY_VISIBILITY = 10
BOUNDING_COLOR = (0, 0, 0)
BOUNDARY_LINE_COLOR = (255, 0, 255)

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

# Gate Constants
GATE_COUNT = 4
GATE_WIDTH = 100
GATES = [ [ [104, 552], [104, 664] ], \
	      [ [104, 216], [104, 104] ], \
		  [ [808, 616], [696, 616] ], \
		  [ [936, 152], [824, 152] ], \
		  #[ [456, 440], [456, 328] ]  ]		# vertical, green is on bottom (backwards c)
		  #[ [568, 328], [568, 440] ]  ]		# vertical, green is on top (c)
		  [ [456, 328], [568, 328] ]  ]	# horizontal, green on left (u)
		  #[ [568, 440], [456, 440] ]  ]	# horizontal, green on right (n)
		  
NBR_RANDOM_OBSTACLES = 20

# Graph Constants
GRID_SIZE = 16

DEBUGGING = True
DEBUG_LINE_WIDTH = 1
DEBUG_BOUNDING_RECTS = DEBUGGING
DEBUG_VELOCITY = DEBUGGING
DEBUG_NEIGHBORS = DEBUGGING
DEBUG_BOUNDARIES = DEBUGGING
DEBUG_DOG_INFLUENCE = DEBUGGING
DEBUG_OBSTACLES = DEBUGGING
DEBUG_GRID_LINES = True
DEBUG_NEIGHBOR_LINES = False
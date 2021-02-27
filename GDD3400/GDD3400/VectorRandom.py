import random
import Constants
from Vector import Vector

# random position generator
def randomPosition():
    randomx = random.randint(0, Constants.WORLD_WIDTH)
    randomy = random.randint(0, Constants.WORLD_HEIGHT)
    return Vector(randomx, randomy)

# random velocity
def randomVelocity():
    randomx = random.random() - 0.5
    randomy = random.random() - 0.5
    return Vector(randomx, randomy)

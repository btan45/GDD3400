import pygame
import Constants
import VectorRandom

from Vector import Vector
from UserInterface import UserInterface
from Sheep import Sheep
from Dog import Dog
from Graph import *
from Node import *
from random import *

#################################################################################
# Helper Functions
#################################################################################

def buildGates(graph):
    X = 0
    Y = 1
    # Add the gates to the game
    # pick one end, then pick the second end about 50 spaces away (pick a direction, generate the far end
    for gate in Constants.GATES:
        graph.placeObstacle(Vector(gate[0][X], gate[0][Y]), (0, 255, 0))
        graph.placeObstacle(Vector(gate[1][X], gate[1][Y]), (255, 0, 0))
        print("Placing Obstacles: " + str(gate[0]) + " " + str(gate[1]))

    # Add the final pen based on the final gate
    finalGate = gate[-2:]
    # If the gate is horizontally arranged
    if finalGate[0][Y] == finalGate[1][Y]:
        # If the green gate (the first gate) is on the right, paddock goes "up"
        if finalGate[0][X] > finalGate[1][X]:
            direction = -1
        else:
            direction = 1
        for y in range(finalGate[0][Y] + direction * 16, finalGate[0][Y] + direction * 112, direction * 16):
            graph.placeObstacle(Vector(finalGate[0][X], y), (0, 0, 0))
            graph.placeObstacle(Vector(finalGate[1][X], y), (0, 0, 0))
        for x in range(finalGate[0][X] + direction * 16, finalGate[1][X], direction * 16):
            graph.placeObstacle(Vector(x, finalGate[0][Y] + direction * 96), (0, 0, 0))
    # If the gate is vertically arranged
    else:
        # If the green gate (the first gate) is on the bottom, paddock goes "right"
        if finalGate[0][Y] < finalGate[1][Y]:
            direction = -1
        else:
            direction = 1
        for x in range(finalGate[0][X] + direction * 16, finalGate[1][X] + direction * 112, direction * 16):
            graph.placeObstacle(Vector(x, finalGate[0][Y]), (0, 0, 0))
            graph.placeObstacle(Vector(x, finalGate[1][Y]), (0, 0, 0))
        for y in range(finalGate[0][Y] - direction *  16, finalGate[1][Y], - direction * 16):
            graph.placeObstacle(Vector(finalGate[0][X] + direction * 96, y), (0, 0, 0))

def buildObstacles(graph):
    # Random Obstacles
    for i in range(Constants.NBR_RANDOM_OBSTACLES):
        start = Vector(randrange(0, Constants.WORLD_WIDTH), randrange(0, Constants.WORLD_HEIGHT))
        graph.placeObstacle(start, (0, 0, 0))
        for j in range(randrange(Constants.NBR_RANDOM_OBSTACLES)):
            start += Vector((randrange(3) - 1) * Constants.GRID_SIZE, (randrange(3) - 1) * Constants.GRID_SIZE)
            while(start.x >= Constants.WORLD_WIDTH - Constants.GRID_SIZE or start.y >= Constants.WORLD_HEIGHT - Constants.GRID_SIZE):
                start += Vector((randrange(3) - 1) * Constants.GRID_SIZE, (randrange(3) - 1) * Constants.GRID_SIZE)
            graph.placeObstacle(start, (0, 0, 0))


#################################################################################
# Main Functionality
#################################################################################

pygame.init()
clock = pygame.time.Clock()

# display size
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))

# images
dogImage = pygame.image.load("collie.png")
sheepImage = pygame.image.load("sheep.png")

# Setup the graph
graph = Graph()

# controls game loop
isRunning = False

# create dog
dog = Dog(Constants.DOG_POSITION, Constants.DOG_INITIAL_SPEED, Constants.DOG_MAX_SPEED, Constants.DOG_SIZE, dogImage)

# agents list
sheeps = []
# fill in list with sheeps
for i in range(Constants.NUM_SHEEP):
    sheep = Sheep(VectorRandom.randomPosition(), Constants.SHEEP_INITIAL_SPEED, Constants.SHEEP_MAX_SPEED, Constants.SHEEP_SIZE, sheepImage)
    sheeps.append(sheep)

# Setup the gates and obstacles
buildGates(graph)
buildObstacles(graph)

dog.path = graph.findPath_Breadth(graph.getNodeFromPoint(dog.center), graph.getNodeFromPoint(sheeps[0].center))

# game loop
while not isRunning:
    screen.fill(Constants.BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = True
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            UserInterface.handleNumKeys(event)

    graph.draw(screen)

    # dog
    if len(dog.path) == 0:
        dog.path = graph.findPath_Breadth(graph.getNodeFromPoint(dog.center), graph.getNodeFromPoint(sheeps[0].center))
    dog.update(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT)
    dog.draw(screen)

    # sheep
    for sheep in sheeps:
        sheep.update(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT, sheeps, dog)
        sheep.draw(screen, Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT, sheeps, dog)

    pygame.display.flip()
    clock.tick(Constants.FRAME_RATE)
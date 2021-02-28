import pygame
import Constants
import random
import VectorRandom
from Vector import Vector
from UserInterface import UserInterface
from Sheep import Sheep
from Dog import Dog

pygame.init()
clock = pygame.time.Clock()

# display size
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))

# images
dogImage = pygame.image.load("collie.png")
sheepImage = pygame.image.load("sheep.png")

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

# game loop
while not isRunning:
    screen.fill(Constants.BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = True
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            UserInterface.handleNumKeys(event)

    # dog
    dog.update(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT)
    dog.draw(screen)

    # sheep
    for sheep in sheeps:
        sheep.update(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT, sheeps, dog)
        sheep.draw(screen, Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT, sheeps, dog)

    pygame.display.flip()
    clock.tick(Constants.FRAME_RATE)
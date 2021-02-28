import pygame
import Constants
import random
import VectorRandom
from Vector import Vector
from Player import Player
from Enemy import Enemy
from EnemyHunter import EnemyHunter
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

# create player
# dog = Dog(Constants.PLAYER_POSITION, Constants.DOG_INITIAL_SPEED, Constants.DOG_MAX_SPEED, Constants.PLAYER_SIZE, Constants.PLAYER_COLOR, dogImage)

# agents list
agents = []
# fill in list with enemies
for i in range(Constants.NUM_ENEMIES):
    sheep = Sheep(VectorRandom.randomPosition(), Constants.SHEEP_INITIAL_SPEED, Constants.SHEEP_MAX_SPEED, Constants.SHEEP_SIZE, Constants.ENEMY_COLOR, sheepImage)
    agents.append(sheep)

# game loop
while not isRunning:
    screen.fill(Constants.BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = True
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            UserInterface.handleNumKeys(event)

    # player
    # dog.update(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT)
    # dog.draw(screen)

    # enemy
    for agent in agents:
        agent.update(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT, agents)
        agent.draw(screen, agents)

    pygame.display.flip()
    clock.tick(Constants.FRAME_RATE)
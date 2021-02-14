import pygame
import Constants
from Vector import Vector
from Player import Player
from Enemy import Enemy

pygame.init()
clock = pygame.time.Clock()

# display size
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))

# controls game loop
isRunning = False

# create player
player = Player(Constants.PLAYER_POSITION, Constants.PLAYER_SPEED, Constants.PLAYER_SIZE, Constants.PLAYER_COLOR)
enemy = Enemy(Constants.ENEMY_POSITION, Constants.ENEMY_SPEED, Constants.ENEMY_SIZE, Constants.ENEMY_COLOR)

while not isRunning:
    screen.fill(Constants.BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = True

    # player
    player.update()
    player.draw(screen)

    # enemy
    enemy.update(player)
    enemy.draw(screen)

    pygame.display.flip()
    clock.tick(Constants.FRAME_RATE)
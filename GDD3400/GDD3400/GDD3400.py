import pygame
import Constants
import random
from Vector import Vector
from Player import Player
from Enemy import Enemy
from EnemyHunter import EnemyHunter

# random vector generator
def randomVector():
    randomx = random.randint(0, Constants.WORLD_WIDTH)
    randomy = random.randint(0, Constants.WORLD_HEIGHT)
    return Vector(randomx, randomy)

pygame.init()
clock = pygame.time.Clock()

# display size
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))

# controls game loop
isRunning = False

# create player
player = Player(Constants.PLAYER_POSITION, Constants.PLAYER_SPEED, Constants.PLAYER_SIZE, Constants.PLAYER_COLOR)

# enemy list
enemies = []
# fill in list with enemies
for i in range(Constants.NUM_ENEMIES):
    enemy = Enemy(randomVector(), Constants.ENEMY_SPEED, Constants.ENEMY_SIZE, Constants.ENEMY_COLOR)
    enemyHunter = EnemyHunter(randomVector(), Constants.ENEMY_SPEED, Constants.ENEMY_SIZE, Constants.ENEMY_HUNTER_COLOR)

    enemies.append(enemy)
    enemies.append(enemyHunter)

# game loop
while not isRunning:
    screen.fill(Constants.BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = True
            pygame.quit()

    # player
    player.update(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT)
    player.draw(screen)

    # enemy
    for enemy in enemies:
        enemy.update(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT, player)
        enemy.draw(screen, player)

    pygame.display.flip()
    clock.tick(Constants.FRAME_RATE)
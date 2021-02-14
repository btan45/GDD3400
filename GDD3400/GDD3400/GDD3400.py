import pygame
import Constants

pygame.init()
clock = pygame.time.Clock()

# display size
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))

# controls game loop
isRunning = False

while not isRunning:
    screen.fill(Constants.BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = True

    pygame.display.flip()
    clock.tick(Constants.FRAME_RATE)
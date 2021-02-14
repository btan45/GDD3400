import pygame
from Vector import Vector
import Constants

class Player:
    def __init__(self, initialPosition, initialSpeed, size, color):
        self.position = initialPosition
        self.speed = initialSpeed
        self.velocity = Constants.ZERO_VECTOR
        self.size = size
        self.center = self.position + Vector(self.size/2, self.size/2)
        self.color = color

    def draw(self, screen):
        # draws the rectangle
        rectangle = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, rectangle)

        # line positions
        playerPos = (self.position.x, self.position.y)
        playerNextPos = (self.position.x + (self.velocity.x * 10), self.position.y + (self.velocity.y * 10))
        # drawing line
        pygame.draw.line(screen, Constants.PLAYER_LINE_COLOR, playerPos, playerNextPos)

    def update(self):
        # key pressed
        pressed = pygame.key.get_pressed()
        # moves upper left
        if pressed[pygame.K_a] and pressed[pygame.K_w]:
            self.velocity = Constants.UPPER_LEFT_VECTOR
        # moves upper right
        elif pressed[pygame.K_w] and pressed[pygame.K_d]:
            self.velocity = Constants.UPPER_RIGHT_VECTOR
        # moves lower right
        elif pressed[pygame.K_d] and pressed[pygame.K_s]:
            self.velocity = Constants.LOWER_RIGHT_VECTOR
        # moves lower left
        elif pressed[pygame.K_s] and pressed[pygame.K_a]:
            self.velocity = Constants.LOWER_LEFT_VECTOR
        # moves up
        elif pressed[pygame.K_w]:
            self.velocity = Constants.UP_VECTOR
        # moves down
        elif pressed[pygame.K_s]:
            self.velocity = Constants.DOWN_VECTOR
        # moves left
        elif pressed[pygame.K_a]:
            self.velocity = Constants.LEFT_VECTOR
        # moves right
        elif pressed[pygame.K_d]:
            self.velocity = Constants.RIGHT_VECTOR
        else:
            self.velocity = Constants.ZERO_VECTOR
        
        self.velocity = self.velocity.scale(self.speed)
        self.position += self.velocity
  
    


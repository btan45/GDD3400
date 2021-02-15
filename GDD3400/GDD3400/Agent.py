import pygame
import Constants
from Vector import Vector

class Agent:
    def __init__(self, initialPosition, initialSpeed, size, color):
        self.position = initialPosition
        self.speed = initialSpeed
        self.velocity = Constants.ZERO_VECTOR
        self.size = size
        self.center = self.position + Vector(self.size/2, self.size/2)
        self.color = color
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)

    def __str__(self):
        return "Size: {}, Position: {}, Velocity: {}, Center: {}".format(self.size, self.position, self.velocity, self.center)

    def draw(self, screen):
        # draws the rectangle
        pygame.draw.rect(screen, self.color, self.rect)

        # line positions
        startingPos = (self.position.x, self.position.y)
        nextPos = (self.position.x + (self.velocity.x * self.speed), self.position.y + (self.velocity.y * self.speed))
        # drawing line
        pygame.draw.line(screen, Constants.LINE_COLOR, startingPos, nextPos)

    def collision(self, object):
        return pygame.Rect.colliderect(self.rect, object.rect)

    def update(self):
        self.velocity = self.velocity.scale(self.speed)
        self.position += self.velocity
        self.center = self.position + Vector(self.size/2, self.size/2)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)

   

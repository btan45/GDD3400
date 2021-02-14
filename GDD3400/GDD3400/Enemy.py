import pygame
from Vector import Vector
import Constants

class Enemy:
    def __init__(self, initialPosition, initialSpeed, initialSize, color):
        self.position = initialPosition
        self.speed = initialSpeed
        self.size = initialSize
        self.velocity = Constants.ZERO_VECTOR
        self.center = self.position + Vector(self.size/2, self.size/2)
        self.color = color
    
    def __str__(self):
        return "Size: {}, Position: {}, Velocity: {}, Center: {}".format(self.size, self.position, self.velocity, self.center)

    def draw(self, screen):
        # draws the rectangle
        rectangle = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, rectangle)

        # line positions
        enemyPos = (self.position.x, self.position.y)
        enemyNextPos = (self.position.x + (self.velocity.x * 10), self.position.y + (self.velocity.y * 10))
        # drawing line
        pygame.draw.line(screen, Constants.ENEMY_LINE_COLOR, enemyPos, enemyNextPos)

    def seek(self, player):
        range = player.position - self.position
        length = range.length()

        if length < Constants.ATTACK_RANGE:
            self.velocity = range.normalize().scale(self.speed)
            self.position += self.velocity

    def update(self, player):
        self.seek(player)
        


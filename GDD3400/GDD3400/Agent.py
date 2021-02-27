import pygame
import Constants
from Vector import Vector

class Agent:
    def __init__(self, initialPosition, initialSpeed, size, color, surface):
        self.position = initialPosition
        self.speed = initialSpeed
        self.velocity = Constants.ZERO_VECTOR
        self.size = size
        self.color = color
        self.target = Constants.ZERO_VECTOR
        self.updateRect()
        self.updateCenter()
        self.surface = surface

    def __str__(self):
        return "Size: {}, Position: {}, Velocity: {}, Center: {}".format(self.size, self.position, self.velocity, self.center)

    def updateVelocity(self, velocity):
        self.velocity =  velocity.normalize()

    def updateRect(self):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

    def updateCenter(self):
        self.center = self.position + (self.size.scale(0.5))

    def isInCollision(self, object):
        # returns bool of wether or not a collision happened
        return pygame.Rect.colliderect(self.rect, object.rect)

    def update(self, boundx, boundy):
        # velocity
        self.velocity = self.velocity.scale(self.speed)
        # position
        self.position += self.velocity

        # creates bounds for the agent
        if self.position.x < 0:
            self.position.x = 0
        elif self.position.x + self.size.x > boundx:
            self.position.x = boundx - self.size.x
        if self.position.y < 0:
            self.position.y = 0
        elif self.position.y + self.size.y > boundy:
            self.position.y = boundy - self.size.y

        # rectangle
        self.updateRect();
        # center
        self.updateCenter();

    def draw(self, screen):
        screen.blit(self.surface, [self.position.x, self.position.y])

        # line positions
        startingPos = (self.position.x, self.position.y)
        nextPos = (self.position.x + (self.velocity.x * self.speed), self.position.y + (self.velocity.y * self.speed))
        # drawing line
        pygame.draw.line(screen, Constants.LINE_COLOR, startingPos, nextPos)

   

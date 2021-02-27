import pygame
import Constants
from Vector import Vector

class Agent:
    def __init__(self, initialPosition, initialSpeed, maxSpeed, size, color, surface):
        self.position = initialPosition
        self.speed = initialSpeed
        self.maxSpeed = maxSpeed
        self.velocity = Constants.ZERO_VECTOR
        self.size = size
        self.color = color
        self.surface = surface
        self.target = Constants.ZERO_VECTOR
        self.updateRotatedSurface()
        self.updateRect()
        self.updateBoundingRect()
        self.updateCenter()

    def __str__(self):
        return "Size: {}, Position: {}, Velocity: {}, Center: {}".format(self.size, self.position, self.velocity, self.center)

    def updateVelocity(self, velocity):
        self.velocity =  velocity.normalize()

    def updateRect(self):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

    def updateRotatedSurface(self):
        self.rotatedSurface = pygame.transform.rotate(self.surface, self.velocity.angle())

    def updateCenter(self):
        self.center = self.position + Vector(self.rotatedSurface.get_width(), self.rotatedSurface.get_height()).scale(0.5)

    def updateBoundingRect(self):
        self.boundingRect = self.rotatedSurface.get_bounding_rect().move(self.position.x, self.position.y)

    def isInCollision(self, object):
        # returns bool of wether or not a collision happened
        return pygame.Rect.colliderect(self.boundingRect, object.boundingRect)

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
        
        self.updateRotatedSurface()
        self.updateRect()
        self.updateBoundingRect()
        self.updateCenter()

    def draw(self, screen):
        screen.blit(self.rotatedSurface, [self.position.x, self.position.y])

        pygame.draw.rect(screen, Constants.BOUNDING_COLOR, self.boundingRect, 1)
        # line positions
        startingPos = (self.center.x, self.center.y)
        nextPos = (self.center.x + (self.velocity.x * self.speed), self.center.y + (self.velocity.y * self.speed))
        # drawing line
        pygame.draw.line(screen, self.color, startingPos, nextPos)

   

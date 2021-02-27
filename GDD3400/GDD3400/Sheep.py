import pygame
import Constants
import VectorRandom
from Vector import Vector
from Agent import Agent

class Sheep(Agent):
    def __init__(self, initialPosition, initialSpeed, maxSpeed, size, color, surface):
        super().__init__(initialPosition, initialSpeed, maxSpeed, size, color, surface)
        self.velocity = VectorRandom.randomVelocity().normalize()

    def isOtherClose(self, other):
        # finds the other's current position from enemy position
        range = other.position - self.position
        length = range.length()
        isInRange = length < Constants.ATTACK_RANGE
        
        return isInRange

    def calcTrackingVelocity(self, other):
        self.target = other.center

    def draw(self, screen, other):
        # calls parent, Agent
        super().draw(screen)
        if self.isOtherClose(other):
            pygame.draw.line(screen, Constants.SEEKING_LINE_COLOR, self.center.toTuple(), other.center.toTuple())

    # fleeing behavior
    def flee(self, other):
        # finds the other's current position from enemy position
        movementDirection = self.position - self.target

        # if other is within range, flees
        if self.isOtherClose(other):
            self.velocity = movementDirection.normalize()
            self.speed = self.maxSpeed
        # stops movement
        else:
            self.speed = 0

    def update(self, boundx, boundy, other):
        self.calcTrackingVelocity(other)
        self.flee(other)

        # calls parent, Agent
        super().update(boundx, boundy)

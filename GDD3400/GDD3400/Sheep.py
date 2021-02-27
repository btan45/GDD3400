import pygame
import Constants
from Vector import Vector
from Agent import Agent

class Sheep(Agent):
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

    # fleeing behavior
    def flee(self, other):
        # finds the other's current position from enemy position
        movementDirection = self.position - self.target

        # if other is within range, flees
        if self.isOtherClose(other):
            self.velocity = movementDirection.normalize()
        # stops movement
        else:
            self.velocity = Constants.ZERO_VECTOR

    def update(self, boundx, boundy, other):
        self.calcTrackingVelocity(other)
        self.flee(other)

        # calls parent, Agent
        super().update(boundx, boundy)

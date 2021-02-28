import pygame
import Constants
import VectorRandom
from Vector import Vector
from Agent import Agent
from UserInterface import UserInterface

class Sheep(Agent):
    def __init__(self, initialPosition, initialSpeed, maxSpeed, size, color, surface):
        super().__init__(initialPosition, initialSpeed, maxSpeed, size, color, surface)
        self.velocity = VectorRandom.randomVelocity().normalize()

    def isOtherClose(self, other):
        # finds the other's current position from enemy position
        range = other.position - self.position
        length = range.length()
        isInRange = length < Constants.SHEEP_NEIGHBOR_RADIUS
        
        return isInRange

    def calcTrackingVelocity(self, other):
        self.target = other.center

    def draw(self, screen, others):
        super().draw(screen)
        if UserInterface.NeighborLines:
            for other in others:
                if self is not other and self.isOtherClose(other):
                    pygame.draw.line(screen, Constants.LINE_COLOR, self.center.toTuple(), other.center.toTuple())

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

    # alignment behavior
    def alignment(self, others):
        if not UserInterface.AlignmentForces:
            return Constants.ZERO_VECTOR

        numNeighbors = 0
        alignmentForce = Constants.ZERO_VECTOR

        for other in others:
            if self is not other and self.isOtherClose(other):
                alignmentForce += other.velocity
                numNeighbors += 1
        if numNeighbors == 0:
            return alignmentForce
        else:
            return alignmentForce.scale(1 / numNeighbors).normalize()

    # cohesion behavior
    def cohesion(self, others):
        if not UserInterface.CohesionForces:
            return Constants.ZERO_VECTOR

        numNeighbors = 0
        cohesionForce = Constants.ZERO_VECTOR

        for other in others:
            if self is not other and self.isOtherClose(other):
                cohesionForce += other.center
                numNeighbors += 1
        if numNeighbors == 0:
            return cohesionForce
        else:
            cohesionForce.scale(1 / numNeighbors)
            return (cohesionForce - self.center).normalize()

    # separation behavior
    def separation(self, others):
        if not UserInterface.SeparationForces:
            return Constants.ZERO_VECTOR

        numNeighbors = 0
        separationForce = Constants.ZERO_VECTOR

        for other in others:
            if self is not other and self.isOtherClose(other):
                separationForce += self.center - other.center
                numNeighbors += 1
        if numNeighbors == 0:
            return separationForce
        else:
            separationForce.scale(-1 / numNeighbors)
            return (separationForce - self.center).normalize()

    def update(self, boundx, boundy, others):
        # self.calcTrackingVelocity(other)
        # self.flee(other)

        netForce = self.alignment(others).scale(Constants.SHEEP_ALIGNMENT_WEIGHT)
        netForce += self.cohesion(others).scale(Constants.SHEEP_COHESION_WEIGHT)
        netForce += self.separation(others).scale(Constants.SHEEP_SEPARATION_WEIGHT)
        self.velocity = netForce

        

        # calls parent, Agent
        super().update(boundx, boundy)

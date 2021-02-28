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

    def draw(self, screen, others):
        super().draw(screen)
        if UserInterface.NeighborLines:
            for other in others:
                if self is not other and self.isOtherClose(other):
                    pygame.draw.line(screen, Constants.LINE_COLOR, self.center.toTuple(), other.center.toTuple())
        if UserInterface.SheepVelocityLine:
            # line positions
            nextPos = self.center + self.velocity.scale(self.speed * Constants.SHEEP_VELOCITY_VISIBILITY)
            # drawing line
            pygame.draw.line(screen, self.color, self.center.toTuple(), nextPos.toTuple())

    # fleeing behavior
    def dogInfluence(self, other):
        if not UserInterface.DogForces:
            return Constants.ZERO_VECTOR
        
        # finds the other's current position from enemy position
        dogForce = self.center - other.center

        # if other is within range, flees
        if self.isOtherClose(other):
            return dogForce.normalize()
        else:
            return Constants.ZERO_VECTOR

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

    def boundaries(self, boundx, boundy):
        if not UserInterface.BoundaryForces:
            return Constants.ZERO_VECTOR

        boundaryForce = Constants.ZERO_VECTOR
        if self.center.x < Constants.SHEEP_BOUNDARY_RADIUS:
            boundaryForce += Constants.RIGHT_VECTOR
        if self.center.y < Constants.SHEEP_BOUNDARY_RADIUS:
            boundaryForce += Constants.DOWN_VECTOR
        if boundx - self.center.x < Constants.SHEEP_BOUNDARY_RADIUS:
            boundaryForce += Constants.LEFT_VECTOR
        if boundy - self.center.y < Constants.SHEEP_BOUNDARY_RADIUS:
            boundaryForce += Constants.UP_VECTOR
        return boundaryForce.normalize()

    def update(self, boundx, boundy, otherSheep, dog):

        netForce = self.alignment(otherSheep).scale(Constants.SHEEP_ALIGNMENT_WEIGHT)
        netForce += self.cohesion(otherSheep).scale(Constants.SHEEP_COHESION_WEIGHT)
        netForce += self.separation(otherSheep).scale(Constants.SHEEP_SEPARATION_WEIGHT)
        netForce += self.dogInfluence(dog).scale(Constants.SHEEP_DOG_INFLUENCE_WEIGHT)
        netForce += self.boundaries(boundx, boundy).scale(Constants.SHEEP_BOUNDARY_INFLUENCE_WEIGHT)
        self.velocity = netForce.normalize()

        

        # calls parent, Agent
        super().update(boundx, boundy)

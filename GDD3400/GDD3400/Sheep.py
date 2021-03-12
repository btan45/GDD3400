import pygame
import Constants
import VectorRandom
from Vector import Vector
from Agent import Agent
from UserInterface import UserInterface

class Sheep(Agent):
    def __init__(self, initialPosition, initialSpeed, maxSpeed, size, surface):
        super().__init__(initialPosition, initialSpeed, maxSpeed, size, surface)
        self.velocity = VectorRandom.randomVelocity().normalize()
        self.neighbors = []

    # calculates range of objects
    def isOtherClose(self, other):
        # finds the other's current position from enemy position
        range = other.position - self.position
        length = range.length()
        isInRange = length < Constants.SHEEP_NEIGHBOR_RADIUS
        return isInRange

    # calculate neighbors
    def calculateNeighbors(self, herd):
        neighbors = []
        for sheep in herd:
            if self is not sheep and self.isOtherClose(sheep):
                neighbors.append(sheep)
        return neighbors

    def draw(self, screen, boundx, boundy, otherSheep, dog):
        super().draw(screen)

        # toggle draws neighbors lines
        if UserInterface.NeighborLines:
            for neighbor in self.neighbors:
                pygame.draw.line(screen, Constants.LINE_COLOR, self.center.toTuple(), neighbor.center.toTuple())
        
        # toggle draws sheep velocity line
        if UserInterface.SheepVelocityLine:
            # line positions
            nextPos = self.center + self.velocity.scale(self.speed * Constants.SHEEP_VELOCITY_VISIBILITY)
            # drawing line
            pygame.draw.line(screen, Constants.SHEEP_VELOCITY_COLOR, self.center.toTuple(), nextPos.toTuple())

        # toggle draws dog force line
        if UserInterface.DogForceLine and self.isOtherClose(dog):
            pygame.draw.line(screen, Constants.SEEKING_LINE_COLOR, self.center.toTuple(), dog.center.toTuple())

        # toggle draws boundary force lines
        if UserInterface.BoundaryForceLines:
            if self.center.x < Constants.SHEEP_BOUNDARY_RADIUS:
                pygame.draw.line(screen, Constants.BOUNDARY_LINE_COLOR, self.center.toTuple(), (0, self.center.y))
                
            if self.center.y < Constants.SHEEP_BOUNDARY_RADIUS:
                pygame.draw.line(screen, Constants.BOUNDARY_LINE_COLOR, self.center.toTuple(), (self.center.x, 0))

            if boundx - self.center.x < Constants.SHEEP_BOUNDARY_RADIUS:
                pygame.draw.line(screen, Constants.BOUNDARY_LINE_COLOR, self.center.toTuple(), (boundx, self.center.y))

            if boundy - self.center.y < Constants.SHEEP_BOUNDARY_RADIUS:
                pygame.draw.line(screen, Constants.BOUNDARY_LINE_COLOR, self.center.toTuple(), (self.center.x, boundy))

    # fleeing behavior
    def dogInfluence(self, other):
        # toggle
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
        # toggle
        if not UserInterface.AlignmentForces:
            return Constants.ZERO_VECTOR

        numNeighbors = 0
        alignmentForce = Constants.ZERO_VECTOR

        # calculate alignment behavior
        for neighbor in self.neighbors:
            alignmentForce += neighbor.velocity
            numNeighbors += 1
        if numNeighbors == 0:
            return alignmentForce
        else:
            return alignmentForce.scale(1 / numNeighbors).normalize()

    # cohesion behavior
    def cohesion(self, others):
        # toggle
        if not UserInterface.CohesionForces:
            return Constants.ZERO_VECTOR

        numNeighbors = 0
        cohesionForce = Constants.ZERO_VECTOR

        # calculates cohesion force
        for neighbor in self.neighbors:
            cohesionForce += neighbor.center
            numNeighbors += 1
        if numNeighbors == 0:
            return cohesionForce
        else:
            cohesionForce.scale(1 / numNeighbors)
            return (cohesionForce - self.center).normalize()

    # separation behavior
    def separation(self, others):
        # toggle
        if not UserInterface.SeparationForces:
            return Constants.ZERO_VECTOR

        numNeighbors = 0
        separationForce = Constants.ZERO_VECTOR

        # calculates separation force
        for neighbor in self.neighbors:
            separationForce += self.center - neighbor.center
            numNeighbors += 1
        if numNeighbors == 0:
            return separationForce
        else:
            separationForce.scale(-1 / numNeighbors)
            return (separationForce - self.center).normalize()
    
    # calculates the boundary force
    def boundaries(self, boundx, boundy):
        # toggle
        if not UserInterface.BoundaryForces:
            return Constants.ZERO_VECTOR

        # finds the boundary force
        boundaryForce = Constants.ZERO_VECTOR
        # left boundary
        if self.center.x < Constants.SHEEP_BOUNDARY_RADIUS:
            boundaryForce += Constants.RIGHT_VECTOR
        # top boundary
        if self.center.y < Constants.SHEEP_BOUNDARY_RADIUS:
            boundaryForce += Constants.DOWN_VECTOR
        # right boundary
        if boundx - self.center.x < Constants.SHEEP_BOUNDARY_RADIUS:
            boundaryForce += Constants.LEFT_VECTOR
        # bottom boundary
        if boundy - self.center.y < Constants.SHEEP_BOUNDARY_RADIUS:
            boundaryForce += Constants.UP_VECTOR
        return boundaryForce.normalize()

    # checks for obstacles
    def obstacles(self, obstacleList):
        obstacleForce = Constants.ZERO_VECTOR

        for obstacle in obstacleList:
            # finds the opposite vector
            distanceToObstacle = self.center - obstacle.center 
            if distanceToObstacle.length() < Constants.SHEEP_BOUNDARY_RADIUS:
                obstacleForce += distanceToObstacle
        return obstacleForce.normalize()

    def update(self, boundx, boundy, otherSheep, dog, obstacleList):
        # calculates list of neighbors
        self.neighbors = self.calculateNeighbors(otherSheep)

        # forces
        alignmentForce = self.alignment(otherSheep).scale(Constants.SHEEP_ALIGNMENT_WEIGHT)
        cohesionForce = self.cohesion(otherSheep).scale(Constants.SHEEP_COHESION_WEIGHT)
        separationForce = self.separation(otherSheep).scale(Constants.SHEEP_SEPARATION_WEIGHT)
        dogForce = self.dogInfluence(dog).scale(Constants.SHEEP_DOG_INFLUENCE_WEIGHT)
        boundaryForce = self.boundaries(boundx, boundy).scale(Constants.SHEEP_BOUNDARY_INFLUENCE_WEIGHT)
        obstacleForce = self.obstacles(obstacleList).scale(Constants.SHEEP_OBSTACLE_INFLUENCE_WEIGHT)

        # adds forces
        netForce = alignmentForce + cohesionForce + separationForce + dogForce + boundaryForce + obstacleForce
        # angular movment
        # slowly moving the sheep angle so it is not as abrupt
        angluarVelocity = (netForce - self.velocity).scale(Constants.SHEEP_ANGULAR_SPEED)
        self.velocity += angluarVelocity
        self.velocity = self.velocity.normalize()

        # calls parent, Agent
        super().update(boundx, boundy)

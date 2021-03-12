import pygame
import Constants
from Vector import Vector
from Agent import Agent

class Dog(Agent):
    def __init__(self, initialPosition, initialSpeed, maxSpeed, size, surface):
         super().__init__(initialPosition, initialSpeed, maxSpeed, size, surface)
         self.path = []

    # dog follows the path
    def followPath(self):
        if self.path:
            nextNode = self.path[0]
            nextVelocity = (nextNode.center - self.center).normalize()

            if nextNode.isInCollision(self):
                self.path.remove(nextNode)

            return nextVelocity
        else:
            return Constants.ZERO_VECTOR

    def update(self, boundx, boundy):
        nextVelocity = self.followPath()
        # angular movment
        # slowly moving the dog angle so it is not as abrupt
        angluarVelocity = (nextVelocity - self.velocity).scale(Constants.DOG_ANGULAR_SPEED)
        self.velocity += angluarVelocity
        self.velocity.normalize()
        # calls parent, Agent
        super().update(boundx, boundy)
  
    



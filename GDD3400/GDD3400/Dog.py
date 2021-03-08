import pygame
import Constants
from Vector import Vector
from Agent import Agent

class Dog(Agent):
    def __init__(self, initialPosition, initialSpeed, maxSpeed, size, surface):
         super().__init__(initialPosition, initialSpeed, maxSpeed, size, surface)
         self.path = []

    def followPath(self):
        if self.path:
            nextNode = self.path[0]
            self.velocity = (nextNode.center - self.center).normalize()

            if nextNode.isInCollision(self):
                self.path.remove(nextNode)

    def update(self, boundx, boundy):
        self.followPath()
        # calls parent, Agent
        super().update(boundx, boundy)
  
    



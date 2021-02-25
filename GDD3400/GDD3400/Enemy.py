import pygame
import Constants
from Vector import Vector
from Agent import Agent
from enum import Enum

# enum for enemy behavior
class EnemyBehavior(Enum):
    SEEKING = 0
    FOLLOWING = 1
    FLEEING = 2

class Enemy(Agent):
    def __init__(self, initialPosition, initialSpeed, size, color):
        super().__init__(initialPosition, initialSpeed, size, color)
        # behavior for enemy
        self.behavior = EnemyBehavior.SEEKING
        # starting color
        self.normalColor = color
        # invulnerabilty frames
        self.iFrames = 0

    def switchMode(self):
        # changes behavior based on what it is currently
        if self.behavior == EnemyBehavior.SEEKING or self.behavior == EnemyBehavior.FOLLOWING:
            self.behavior = EnemyBehavior.FLEEING
        elif self.behavior == EnemyBehavior.FLEEING:
            self.behavior = EnemyBehavior.SEEKING

    def isPlayerClose(self, player):
        # finds the player's current position from enemy position
        range = player.position - self.position
        length = range.length()
        isInRange = length < Constants.ATTACK_RANGE
        
        if isInRange and self.behavior == EnemyBehavior.SEEKING:
            self.behavior = EnemyBehavior.FOLLOWING
        elif not isInRange and self.behavior == EnemyBehavior.FOLLOWING:
            self.behavior = EnemeyBehavior.SEEKING
        return isInRange

    def calcTrackingVelocity(self, player):
        self.target = player.center

    def draw(self, screen, player):
        # calls parent, Agent
        super().draw(screen)
        if self.behavior == EnemyBehavior.FOLLOWING:
            # line position
            centerPos = (self.center.x, self.center.y)
            targetPos = (self.target.x, self.target.y)
            pygame.draw.line(screen, Constants.SEEKING_LINE_COLOR, centerPos, targetPos)

    # seeking behavior
    def seek(self, player):
        # finds the player's current position from enemy position
        movementDirection = self.target - self.position

        # if player is within range, seeks
        if self.isPlayerClose(player):
            self.velocity = movementDirection.normalize()
        # stops movement
        else:
            self.velocity = Constants.ZERO_VECTOR

    # fleeing behavior
    def flee(self, player):
        # finds the player's current position from enemy position
        movementDirection = self.position - self.target

        # if player is within range, flees
        if self.isPlayerClose(player):
            self.velocity = movementDirection.normalize()
        # stops movement
        else:
            self.velocity = Constants.ZERO_VECTOR

    def update(self, boundx, boundy, player):
        self.calcTrackingVelocity(player)

        # checks to see if there is a collision and if there are no invulnerabilty frames
        if self.isInCollision(player) and self.iFrames == 0:
            # sets frames to constant I-Frames
            self.iFrames = Constants.I_FRAMES
            self.switchMode()
        
        # depending on which behavior, calls seek or flee methods
        if self.behavior == EnemyBehavior.SEEKING or self.behavior == EnemyBehavior.FOLLOWING:
            self.seek(player)
        elif self.behavior == EnemyBehavior.FLEEING:
            self.flee(player)
        
        # changes enemy color to indicate I-Frames
        if self.iFrames > 0:
            if self.iFrames % Constants.FLASHING_FRAMES == 1:
                if self.color == self.normalColor:
                    self.color = Constants.ENEMY_I_FRAME_COLOR
                else:
                    self.color = self.normalColor
            self.iFrames -= 1

        # calls parent, Agent
        super().update(boundx, boundy)
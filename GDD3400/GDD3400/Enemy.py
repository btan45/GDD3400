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

    def draw(self, screen, player):
        # calls parent, Agent
        super().draw(screen)
        if self.behavior == EnemyBehavior.FOLLOWING:
            # line position
            startingPos = (self.center.x, self.center.y)
            nextPos = (player.center.x, player.center.y)
            pygame.draw.line(screen, Constants.SEEKING_LINE_COLOR, startingPos, nextPos)

    # seeking behavior
    def seek(self, player):
        # finds the player's current position from enemy position
        range = player.position - self.position
        length = range.length()

        # if player is within range, seeks
        if length < Constants.ATTACK_RANGE:
            self.velocity = range.normalize()
            self.behavior = EnemyBehavior.FOLLOWING
        # stops movement
        else:
            self.velocity = Constants.ZERO_VECTOR
            self.behavior = EnemyBehavior.SEEKING

    # fleeing behavior
    def flee(self, player):
        # finds the player's current position from enemy position
        range = player.position - self.position
        length = range.length()

        # if player is within range, flees
        if length < Constants.ATTACK_RANGE:
            self.velocity = range.normalize().scale(-1)
        # stops movement
        else:
            self.velocity = Constants.ZERO_VECTOR

    def update(self, boundx, boundy, player):
        # checks to see if there is a collision and if there are no invulnerabilty frames
        if self.collision(player) and self.iFrames == 0:
            # sets frames to constant I-Frames
            self.iFrames = Constants.I_FRAMES
            # changes behavior based on what it is currently
            if self.behavior == EnemyBehavior.SEEKING or self.behavior == EnemyBehavior.FOLLOWING:
                self.behavior = EnemyBehavior.FLEEING
            elif self.behavior == EnemyBehavior.FLEEING:
                self.behavior = EnemyBehavior.SEEKING
        
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
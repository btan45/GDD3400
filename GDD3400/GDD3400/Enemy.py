import pygame
import Constants
from Vector import Vector
from Agent import Agent
from enum import Enum

class EnemyBehavior(Enum):
    SEEKING = 0
    FOLLOWING = 1
    FLEEING = 2

class Enemy(Agent):
    def __init__(self, initialPosition, initialSpeed, size, color):
        super().__init__(initialPosition, initialSpeed, size, color)
        self.behavior = EnemyBehavior.SEEKING
        self.normalColor = color
        self.iFrames = 0

    def draw(self, screen, player):
        super().draw(screen)
        if self.behavior == EnemyBehavior.FOLLOWING:
            # line position
            startingPos = (self.center.x, self.center.y)
            nextPos = (player.center.x, player.center.y)
            pygame.draw.line(screen, Constants.SEEKING_LINE_COLOR, startingPos, nextPos)

    def seek(self, player):
        range = player.position - self.position
        length = range.length()

        if length < Constants.ATTACK_RANGE:
            self.velocity = range.normalize()
            self.behavior = EnemyBehavior.FOLLOWING
        else:
            self.velocity = Constants.ZERO_VECTOR
            self.behavior = EnemyBehavior.SEEKING

    def flee(self, player):
        range = player.position - self.position
        length = range.length()

        if length < Constants.ATTACK_RANGE:
            self.velocity = range.normalize().scale(-1)
        else:
            self.velocity = Constants.ZERO_VECTOR

    def update(self, boundx, boundy, player):
        if self.collision(player) and self.iFrames == 0:
            self.iFrames = Constants.I_FRAMES
            if self.behavior == EnemyBehavior.SEEKING or self.behavior == EnemyBehavior.FOLLOWING:
                self.behavior = EnemyBehavior.FLEEING
            elif self.behavior == EnemyBehavior.FLEEING:
                self.behavior = EnemyBehavior.SEEKING

        if self.behavior == EnemyBehavior.SEEKING or self.behavior == EnemyBehavior.FOLLOWING:
            self.seek(player)
        elif self.behavior == EnemyBehavior.FLEEING:
            self.flee(player)
        
        if self.iFrames > 0:
            if self.iFrames % Constants.FLASHING_FRAMES == 1:
                if self.color == self.normalColor:
                    self.color = Constants.ENEMY_I_FRAME_COLOR
                else:
                    self.color = self.normalColor
            self.iFrames -= 1

        super().update(boundx, boundy)
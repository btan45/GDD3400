import pygame
import Constants
from Vector import Vector
from Agent import Agent
from Enemy import Enemy
from Enemy import EnemyBehavior


class EnemyHunter(Enemy):
    def draw(self, screen, player):
        Agent.draw(self, screen)
        if self.behavior == EnemyBehavior.FOLLOWING:
            # line position
            startingPos = (self.center.x, self.center.y)
            nextPos = (player.center.x + player.velocity.x, player.center.y + player.velocity.y)
            pygame.draw.line(screen, Constants.SEEKING_LINE_COLOR, startingPos, nextPos)

    def seek(self, player):
        futurePlayerPos = player.position + player.velocity
        range =  futurePlayerPos - self.position
        length = range.length()

        if length < Constants.ATTACK_RANGE:
            self.velocity = range.normalize()
            self.behavior = EnemyBehavior.FOLLOWING
        else:
            self.velocity = Constants.ZERO_VECTOR
            self.behavior = EnemyBehavior.SEEKING

    def flee(self, player):
        futurePlayerPos = player.position + player.velocity
        range =  futurePlayerPos - self.position
        length = range.length()

        if length < Constants.ATTACK_RANGE:
            self.velocity = range.normalize().scale(-1)
        else:
            self.velocity = Constants.ZERO_VECTOR

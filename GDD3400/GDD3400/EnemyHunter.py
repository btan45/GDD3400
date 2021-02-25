import pygame
import Constants
from Vector import Vector
from Agent import Agent
from Enemy import Enemy
from Enemy import EnemyBehavior


class EnemyHunter(Enemy):
    def calcTrackingVelocity(self, player):
        self.target = player.center + player.velocity.scale(player.speed)


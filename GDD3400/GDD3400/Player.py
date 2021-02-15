import pygame
import Constants
from Vector import Vector
from Agent import Agent

class Player(Agent):
    def handleKeyPressed(self):
        # key pressed
        pressed = pygame.key.get_pressed()
        # moves upper left
        if pressed[pygame.K_a] and pressed[pygame.K_w]:
            self.velocity = Constants.UPPER_LEFT_VECTOR
        # moves upper right
        elif pressed[pygame.K_w] and pressed[pygame.K_d]:
            self.velocity = Constants.UPPER_RIGHT_VECTOR
        # moves lower right
        elif pressed[pygame.K_d] and pressed[pygame.K_s]:
            self.velocity = Constants.LOWER_RIGHT_VECTOR
        # moves lower left
        elif pressed[pygame.K_s] and pressed[pygame.K_a]:
            self.velocity = Constants.LOWER_LEFT_VECTOR
        # moves up
        elif pressed[pygame.K_w]:
            self.velocity = Constants.UP_VECTOR
        # moves down
        elif pressed[pygame.K_s]:
            self.velocity = Constants.DOWN_VECTOR
        # moves left
        elif pressed[pygame.K_a]:
            self.velocity = Constants.LEFT_VECTOR
        # moves right
        elif pressed[pygame.K_d]:
            self.velocity = Constants.RIGHT_VECTOR
        else:
            self.velocity = Constants.ZERO_VECTOR
    def update(self, boundx, boundy):
        self.handleKeyPressed()
        super().update(boundx, boundy)
  
    


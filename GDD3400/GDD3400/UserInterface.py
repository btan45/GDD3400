import pygame

class UserInterface():
    SheepVelocityLine = False
    DogForceLine = False
    BoundaryForceLines = False
    NeighborLines = False
    BoundingBoxes = False
    DogForces = False
    AlignmentForces = True
    SeparationForces = True
    CohesionForces = True
    BoundaryForces = False

    @staticmethod
    def handleNumKeys(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print('Toggle Sheep Velocity line.')
                UserInterface.SheepVelocityLine = not UserInterface.SheepVelocityLine

            elif event.key == pygame.K_2:
                print('Toggle Dog Force line')
                UserInterface.DogForceLine = not UserInterface.DogForceLine

            elif event.key == pygame.K_3:
                print('Toggle Boundary Force lines')
                UserInterface.BoundaryForceLines = not UserInterface.BoundaryForceLines

            elif event.key == pygame.K_4:
                print('Toggle Neighbor lines')
                UserInterface.NeighborLines = not UserInterface.NeighborLines

            elif event.key == pygame.K_5:
                print('Toggle Bounding Boxes')
                UserInterface.BoundingBoxes = not UserInterface.BoundingBoxes

            elif event.key == pygame.K_6:
                print('Toggle Dog Forces')
                UserInterface.DogForces = not UserInterface.DogForces

            elif event.key == pygame.K_7:
                print('Toggle Alignment Forces')
                UserInterface.AlignmentForces = not UserInterface.AlignmentForces

            elif event.key == pygame.K_8:
                print('Toggle Separation Forces')
                UserInterface.SeparationForces = not UserInterface.SeparationForces

            elif event.key == pygame.K_9:
                print('Toggle Cohesion Forces')
                UserInterface.CohesionForces = not UserInterface.CohesionForces

            elif event.key == pygame.K_0:
                print('Toggle Boundary Forces')
                UserInterface.BoundaryForces = not UserInterface.BoundaryForces

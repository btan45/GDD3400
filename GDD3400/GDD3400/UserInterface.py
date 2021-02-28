import pygame

class UserInterface():
    # User Interface Toggles
    SheepVelocityLine = False
    DogForceLine = False
    BoundaryForceLines = False
    NeighborLines = False
    BoundingBoxes = False
    DogForces = True
    AlignmentForces = True
    SeparationForces = True
    CohesionForces = True
    BoundaryForces = True

    @staticmethod
    def handleNumKeys(event):
        if event.type == pygame.KEYDOWN:
            # 1 key
            if event.key == pygame.K_1:
                print('Toggle Sheep Velocity line.')
                UserInterface.SheepVelocityLine = not UserInterface.SheepVelocityLine
            # 2 key
            elif event.key == pygame.K_2:
                print('Toggle Dog Force line')
                UserInterface.DogForceLine = not UserInterface.DogForceLine
            # 3 key
            elif event.key == pygame.K_3:
                print('Toggle Boundary Force lines')
                UserInterface.BoundaryForceLines = not UserInterface.BoundaryForceLines
            # 4 key
            elif event.key == pygame.K_4:
                print('Toggle Neighbor lines')
                UserInterface.NeighborLines = not UserInterface.NeighborLines
            # 5 key
            elif event.key == pygame.K_5:
                print('Toggle Bounding Boxes')
                UserInterface.BoundingBoxes = not UserInterface.BoundingBoxes
            # 6 key
            elif event.key == pygame.K_6:
                print('Toggle Dog Forces')
                UserInterface.DogForces = not UserInterface.DogForces
            # 7 key
            elif event.key == pygame.K_7:
                print('Toggle Alignment Forces')
                UserInterface.AlignmentForces = not UserInterface.AlignmentForces
            # 8 key
            elif event.key == pygame.K_8:
                print('Toggle Separation Forces')
                UserInterface.SeparationForces = not UserInterface.SeparationForces
            # 9 key
            elif event.key == pygame.K_9:
                print('Toggle Cohesion Forces')
                UserInterface.CohesionForces = not UserInterface.CohesionForces
            # 0 key
            elif event.key == pygame.K_0:
                print('Toggle Boundary Forces')
                UserInterface.BoundaryForces = not UserInterface.BoundaryForces

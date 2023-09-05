import pygame

def moveAliens(aliens, direction):
    if direction == "right":
        moveDistance = 20
    else:
        moveDistance = -20
    for column in aliens[:]:
        for alien in column[:]: 
            alien.x += moveDistance

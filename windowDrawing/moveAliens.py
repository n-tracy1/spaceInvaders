import pygame

def moveAliens(aliens, direction):
    if direction == "right":
        moveHorizontal(aliens, 20)
    elif direction == "left":
        moveHorizontal(aliens, -20)
    else:
        moveVertical(aliens, 40)
    
    
def moveHorizontal(aliens, distance):
    for column in aliens[:]:
        for alien in column[:]: 
            alien.x += distance

def moveVertical(aliens, distance):
    for column in aliens[:]:
        for alien in column[:]: 
            alien.y += distance
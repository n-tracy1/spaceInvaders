import pygame
from windowDrawing import bulletHeight

def moveBullets(bullets, aliens, playerInfo):
    for bullet in bullets[:]:
        # loop through aliens and see if the bullet collides with the aliens
        alienCollision = False
        if bullet.y > 0 - bulletHeight:
            bullet.y -= 5
        for column in aliens[:]:
            for alien in column[:]:
                if alien.colliderect(bullet):
                    column.remove(alien)
                    alienCollision = True
                    playerInfo["score"] += 100
                    playerInfo["alienCount"] -= 1
        if bullet.y < 0 - bulletHeight or alienCollision:
            bullets.remove(bullet)
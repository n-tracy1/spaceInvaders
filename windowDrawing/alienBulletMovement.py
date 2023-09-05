import pygame
import random
from windowDrawing import bulletWidth, bulletHeight, alienWidth

def alienFireBullets(bullets, aliens, player):
    
    for column in aliens[:]:
        for alien in column[:]:
            if random.randint(1, 2500) == 1:
                bullet = pygame.Rect((alien.x + alien.x + alienWidth)/2, alien.y, bulletWidth, bulletHeight)
                bullets.append(bullet)

    for bullet in bullets[:]:
        if bullet.colliderect(player):
            return True
        elif bullet.y < 800:
            bullet.y += 5
        else:
            bullets.remove(bullet)
    
    return False

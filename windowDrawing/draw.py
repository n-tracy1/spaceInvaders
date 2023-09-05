import pygame
from utils.font import font

background = pygame.image.load("space.jpg")

def draw(win, player, playerInfo, aliens, bullets, alienBullets):
    win.blit(background, (0, 0))

    time_text = font.render(f"Score: {playerInfo['score']}", 1, "white")
    win.blit(time_text, (10, 10))

    pygame.draw.rect(win, "red", player)
    
    # for star in stars:
    #     pygame.draw.rect(win, "white", star)

    # loop through and draw aliens
    for column in aliens:
        for alien in column:
            pygame.draw.rect(win, "white", alien)

    # loop through and draw bullets
    for bullet in bullets:
        pygame.draw.rect(win, "yellow", bullet)

    for bullet in alienBullets:
        pygame.draw.rect(win, "red", bullet)

    pygame.display.update()
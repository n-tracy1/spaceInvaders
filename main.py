import pygame
import time

from windowDrawing.draw import draw
from windowDrawing.gameOver import gameOver
from windowDrawing.bulletMovement import moveBullets
from windowDrawing.alienBulletMovement import alienFireBullets
from windowDrawing.moveAliens import moveAliens
from utils import width, height
from windowDrawing import bulletWidth, bulletHeight, alienWidth, alienHeight

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")

background = pygame.image.load("space.jpg")

playerWidth = 40
playerHeight = 60

playerVelocity = 5

# Button colors
color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)

def main():
    run = True 

    player = pygame.Rect(480, height - playerHeight - 20, playerWidth, playerHeight)

    clock = pygame.time.Clock()
    startTime = time.time()
    bulletCounter = 0
    bulletLimit = 750
    alienMoveCounterSideways = 0
    alienMoveCounterVertical = 0
    elapsedTime = 0

    playerInfo = {
        "score": 0,
        "alienCount": 0
    }

    aliens = []  
    bullets = []
    alienBullets = []
  
    hit = False

    alienRowStartY = 40
    alienRowStartX = 120
    increment = 80

    rowIndex = alienRowStartY
    columnIndex = alienRowStartX
    
    alienMovement = 2
    alienDirection = "right"

    while rowIndex < 360:
        newColumn = []
        while columnIndex < 880:
            alien = pygame.Rect(columnIndex, rowIndex, alienWidth, alienHeight)
            newColumn.append(alien)
            playerInfo["alienCount"] += 1
            columnIndex += increment
        columnIndex = alienRowStartX
        aliens.append(newColumn)
        rowIndex += increment

    while run:
        bulletCounter += clock.tick(30)
        alienMoveCounterSideways += 30
        alienMoveCounterVertical += 30
        elapsedTime = time.time() - startTime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Move player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= playerVelocity
        elif keys[pygame.K_RIGHT] and player.x < width - playerWidth:
            player.x += playerVelocity  
        # Make bullets
        if keys[pygame.K_SPACE] and bulletCounter >= bulletLimit:
            bullet = pygame.Rect((player.x + player.x + playerWidth)/2, player.y, bulletWidth, bulletHeight)
            bullets.append(bullet)
            bulletCounter = 0

        moveBullets(bullets, aliens, playerInfo)
        hit = alienFireBullets(alienBullets, aliens, player)

        if alienMoveCounterSideways > 1000:
            alienMoveCounterSideways = 0
            if alienMovement < 4:
                alienMovement += 1
                moveAliens(aliens, alienDirection)
            elif alienDirection == "right":
                alienMovement = 1
                alienDirection = "left"
                moveAliens(aliens, alienDirection)
            else:
                alienMovement = 1
                alienDirection = "right"
                moveAliens(aliens, alienDirection)
        if alienMoveCounterVertical > 5000:
            alienMoveCounterVertical = 0
            moveAliens(aliens, "down")

        if hit == True:
            break

        draw(win, player, playerInfo, aliens, bullets, alienBullets)

        if playerInfo["alienCount"] == 0:
            break
      
    gameOver(win, clock, main)
    pygame.quit()


if __name__ == "__main__":
    main()
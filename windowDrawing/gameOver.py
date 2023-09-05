import pygame

from utils import height, width
from utils.font import font

restartWidth = 150
restartHeight = 75
quitWidth = 150
quitHeight = 75

restartXLeftCoord = width/2 - restartWidth/2
restartXRightCoord = width/2 + restartWidth/2
restartYTopCoord = height/2 - 3/2*restartHeight
restartYBottomCoord = height/2 - restartHeight/2
restartText = font.render('restart', 1, "white")

quitXLeftCoord = width/2 - quitWidth/2
quitXRightCoord = width/2 + quitWidth/2
quitYTopCoord = height/2 + quitHeight/2
quitYBottomCoord = height/2 + 3/2*quitHeight
quitText=  font.render('quit', 1, "blue")


def gameOver(win, clock, main_func):
    restartButton = pygame.Rect(restartXLeftCoord, restartYTopCoord, restartWidth, restartHeight)
    quitButton = pygame.Rect(quitXLeftCoord, quitYTopCoord, quitWidth, quitHeight)
    pygame.draw.rect(win, "blue", restartButton)
    pygame.draw.rect(win, "white", quitButton)
    win.blit(restartText, (width/2 - restartText.get_width()/2, (restartYBottomCoord + restartYTopCoord)/2 - restartText.get_height()/2))
    win.blit(quitText, (width/2 - quitText.get_width()/2, (quitYBottomCoord + quitYTopCoord)/2 - quitText.get_height()/2))
    pygame.display.update()

    while True:
        clock.tick(60)
        event = pygame.event.wait()
        print("Checking python event: ", event)
        if event.type == pygame.QUIT:
            print("event is pygame.QUIT")
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if quitXLeftCoord <= mouse[0] <= quitXRightCoord and quitYTopCoord <= mouse[1] <= quitYBottomCoord:
                break
            elif restartXLeftCoord <= mouse[0] <= restartXRightCoord and restartYTopCoord <= mouse[1] <= restartYBottomCoord:
                main_func()
                break
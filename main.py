import pygame
import time
import random
pygame.font.init()

width, height = 1000, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")

background = pygame.image.load("space.jpg")

playerWidth = 40
playerHeight = 60

playerVelocity = 5
starWidth = 10
starHeight = 20

font = pygame.font.SysFont("comicsans", 30)

# Button colors
color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)

def draw(player, elapsedTime, stars):
    win.blit(background, (0, 0))

    time_text = font.render(f"Time: {round(elapsedTime)}s", 1, "white")
    win.blit(time_text, (10, 10))

    pygame.draw.rect(win, "red", player)
    
    for star in stars:
        pygame.draw.rect(win, "white", star)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, height - playerHeight, playerWidth, playerHeight)

    clock = pygame.time.Clock()
    startTime = time.time()
    elapsedTime = 0

    starAddIncrement = 2000
    starCount = 0

    stars = []  
  
    hit = False

    while run:
        starCount += clock.tick(60)
        elapsedTime = time.time() - startTime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if starCount > starAddIncrement:
            for _ in range(3):
                starX = random.randint(0, width - starWidth)
                star = pygame.Rect(starX, -starHeight, starWidth, starHeight) # star starts off the top of the screen
                stars.append(star)
        
            starAddIncrement = max(200, starAddIncrement - 50)
            starCount = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
                player.x -=  playerVelocity
        elif keys[pygame.K_RIGHT] and player.x < width - playerWidth:
                player.x += playerVelocity  
        
        for star in stars[:]:
            if star.y < height:
                star.y += 2
            else:
                stars.remove(star)
            if star.y + height >= player.y and star.colliderect(player):
                 stars.remove(star)
                 hit = True
                 break
            

        if hit == True:
            lostText = font.render('you lost!', 1, "white")
            win.blit(lostText, (width/2 - lostText.get_width()/2, height/2 - lostText.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
            #  run = False

        draw(player, elapsedTime, stars)
      
    # Add restart button/exit button here
    # pygame.event.wait()

    pygame.quit()

if __name__ == "__main__":
    main()
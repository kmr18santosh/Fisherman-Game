import pygame
#new comment added
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('FisherMan')
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#adding player

playerImg=pygame.image.load('sailing-boat.png')
playerX=400
playerY=480
playerX_change=0
playerY_change=0
pressed=0
def player(X,Y):
    screen.blit(playerImg,(X,Y))



running = True
while running:
    screen.fill((27,27,199))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            pressed+=1
            if event.key==pygame.K_LEFT:
                playerX_change=-0.1                
            if event.key==pygame.K_RIGHT:
                playerX_change=0.1 
            if event.key==pygame.K_UP:
                playerY_change=-0.1
            if event.key==pygame.K_DOWN:
                playerY_change=0.1    
        
        if event.type==pygame.KEYUP:
            pressed-=1
            if pressed==0 and (event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN):
                playerX_change=0
                playerY_change=0
            

    playerX+=playerX_change
    playerY+=playerY_change

    if playerX<0:
        playerX=0
    if playerY<0:
        playerY=0    
    if playerX>736:
        playerX=736
    if playerY>536:
        playerY=536
    player(playerX,playerY)
    pygame.display.update()

    
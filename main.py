import pygame
import random
import math

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('FisherMan')
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#adding player boat
playerImg=pygame.image.load('sailing-boat.png')
playerX=400
playerY=500
playerX_change=0
playerY_change=0
pressed=0
def player(X,Y):
    screen.blit(playerImg,(X,Y))
           
#adding sharks

sharkImg=[]
sharkX=[]
sharkY=[]
sharkX_change=[]
sharkY_change=[]
shark_frame_check=[]
num_of_sharks=6

for i in range(num_of_sharks-1):
    sharkImg.append(pygame.image.load('shark.png'))
    sharkX.append(random.randint(0,736))
    sharkY.append(random.randint(0,400))
    sharkX_change.append(0.3)
    sharkY_change.append(40)
    shark_frame_check.append(0)

#adding one Kraken
sharkImg.append(pygame.image.load('kraken.png'))
sharkX.append(random.randint(0,736))
sharkY.append(random.randint(0,400))
sharkX_change.append(0.3)
sharkY_change.append(40)
shark_frame_check.append(0)


def shark(X,Y,i):
    screen.blit(sharkImg[i],(X,Y))


def isCollision(sharkX, sharkY, boatX, boatY):
    distance = math.sqrt(math.pow(sharkX - boatX, 2) + (math.pow(sharkY - boatY, 2)))
    if distance < 27:
        return True
    else:
        return False



running = True
while running:
    screen.fill((0,0,128))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            pressed+=1
            if event.key==pygame.K_LEFT:
                playerX_change=-0.3                
            if event.key==pygame.K_RIGHT:
                playerX_change=0.3 
            if event.key==pygame.K_UP:
                playerY_change=-0.3
            if event.key==pygame.K_DOWN:
                playerY_change=0.3  
            

        
        if event.type==pygame.KEYUP:
            pressed-=1
            if pressed==0 and (event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT 
            or event.key==pygame.K_UP or event.key==pygame.K_DOWN):
                playerX_change=0
                playerY_change=0
            
    #Bounding the Boat within frame
    if playerX<0:
        playerX=0
    if playerY<0:
        playerY=0    
    if playerX>736:
        playerX=736
    if playerY>536:
        playerY=536 
    
    
    for i in range(num_of_sharks):
        
        #Moving the shark
        sharkX[i]+=sharkX_change[i]
        
        #Bounding the shraks within Frame
        if shark_frame_check[i]==0:
            if sharkX[i]<0:
                sharkX_change[i]=0.3
                sharkY[i]+=sharkY_change[i]
            if sharkX[i]>770:
                sharkX_change[i]=-0.3
                sharkY[i]+=sharkY_change[i]
        elif shark_frame_check[i]==1: 
            if sharkX[i]<0:
                sharkX_change[i]=0.3
                sharkY[i]-=sharkY_change[i]
            if sharkX[i]>770:
                sharkX_change[i]=-0.3
                sharkY[i]-=sharkY_change[i]          

        #blitting the sharks
        shark(sharkX[i],sharkY[i],i)
        if sharkY[i]>500:
            shark_frame_check[i]=1
        elif sharkY[i]<0:
            shark_frame_check[i]=0

    

    playerX+=playerX_change
    playerY+=playerY_change
    
    player(playerX,playerY)


    pygame.display.update()

    
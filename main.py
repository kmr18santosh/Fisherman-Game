from gc import DEBUG_SAVEALL
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
sharkX_change.append(0.6)
sharkY_change.append(40)
shark_frame_check.append(0)

#adding fish
fishImg=[]
fishX=[]
fishY=[]
fishX_change=[]
fishY_change=[]
fish_frame_check=[]
num_of_fishes=5

for i in range(num_of_fishes):
    fishImg.append(pygame.image.load('fishR.png'))
    fishX.append(random.randint(0,736))
    fishY.append(random.randint(0,400))
    fishX_change.append(0.1)
    fishY_change.append(20)
    fish_frame_check.append(0)


def player(X,Y):
    screen.blit(playerImg,(X,Y))

def shark(X,Y,i):
    screen.blit(sharkImg[i],(X,Y))

direction=0
def fish(X,Y,i):
    if direction%2==0:
        fishImg[i]=(pygame.image.load('fishR.png'))
    else:
        fishImg[i]=(pygame.image.load('fishL.png'))
    screen.blit(fishImg[i],(X,Y))


def shark_Collision(sharkX, sharkY, boatX, boatY):
    gap = math.sqrt(math.pow(sharkX - boatX, 2) + (math.pow(sharkY - boatY, 2)))
    if gap < 27:
        return True
    else:
        return False

def fish_Collision(sharkX, sharkY, boatX, boatY):
    gap = math.sqrt(math.pow(sharkX - boatX, 2) + (math.pow(sharkY - boatY, 2)))
    if gap < 35:
        return True
    else:
        return False

def disatnce(oldX, oldY, newX, newY):
    distance = math.sqrt(math.pow(oldX - newX, 2) + (math.pow(oldY - newY, 2)))
    return distance

#PLAYER PARAMETERS
boat_health = 20
boat_fuel=30
fish_count=0
font = pygame.font.Font('freesansbold.ttf', 18)


def show_boat_health():
    score = font.render("Boat Health : " + str(boat_health), True, (255, 255, 255))
    screen.blit(score, (10,10))


def game_over_text():
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    over_text = over_font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def show_catch_fish():
    catch_text = font.render("Fish Caught: " + str(fish_count),True,(255,255,255))
    screen.blit(catch_text,(10,38))

def show_fuel():
    if boat_fuel<0:
        fuel_text=font.render("Boat Fuel:EMPTY",True,(255,255,255))
    else:
        fuel_text=font.render("Boat Fuel:" + str(boat_fuel),True,(255,255,255))
    screen.blit(fuel_text,(600,10))

#Boat Running Parameteres
startX=playerX
startY=playerY
endX=0
endY=0


running = True
while running:
    screen.fill((6,11,84))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            pressed+=1
            startX=playerX
            startY=playerY
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
            endX=playerX
            endY=playerY

            travel=disatnce(startX, startY, endX, endY)
            boat_fuel -= travel/50



    #Bounding the Boat within frame
    if playerX<0:
        playerX=0
    if playerY<0:
        playerY=0    
    if playerX>736:
        playerX=736
    if playerY>536:
        playerY=536 
    
    #MANAGING SHARKS
    for i in range(num_of_sharks):

         # Game Over
        if boat_health < 0 or boat_fuel<0:
            for j in range(num_of_sharks):
                sharkY[j] = 2000
            game_over_text()
            break
        
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

        #checking collision
        collision = shark_Collision(sharkX[i], sharkY[i], playerX, playerY)
        if collision:
            #explosionSound = mixer.Sound("explosion.wav")
            #explosionSound.play()
            if i==num_of_sharks-1:
                boat_health -= 5
            else:
                boat_health -= 1
            sharkX[i] = random.randint(0, 736)
            sharkY[i] = random.randint(0, 736)
            
    #MANAGING FISHES
    for i in range(num_of_fishes):

        #Moving the fishes
        fishX[i]+=fishX_change[i]
        
        #Bounding the fishes within Frame
        if fish_frame_check[i]==0:
            if fishX[i]<0:
                fishX_change[i]=0.1
                fishY[i]+=fishY_change[i]
                direction+=1
            if fishX[i]>770:
                fishX_change[i]=-0.1
                fishY[i]+=fishY_change[i]
                direction+=1
        elif fish_frame_check[i]==1: 
            if fishX[i]<0:
                fishX_change[i]=0.1
                fishY[i]-=fishY_change[i]
                direction+=1
            if fishX[i]>770:
                fishX_change[i]=-0.1
                fishY[i]-=fishY_change[i] 
                direction+=1

        #blitting the fishes
        fish(fishX[i],fishY[i],i)
        if fishY[i]>500:
            shark_frame_check[i]=1
        elif fishY[i]<0:
            shark_frame_check[i]=0


        #checking collision
        collision = fish_Collision(fishX[i], fishY[i], playerX, playerY)
        if collision:
            #explosionSound = mixer.Sound("explosion.wav")
            #explosionSound.play()
            fish_count += 1
            fishX[i] = random.randint(0, 736)
            fishY[i] = random.randint(0, 736)

    

    playerX+=playerX_change
    playerY+=playerY_change
    
    player(playerX,playerY)
    show_boat_health()
    show_catch_fish()
    show_fuel()

    pygame.display.update()

    
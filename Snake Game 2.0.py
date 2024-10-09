#Initiating
import random

import pygame
pygame.init()

info = pygame.display.Info()
x = info.current_w
y = info.current_h

window = pygame.display.set_mode((x,y),pygame.RESIZABLE)
pygame.display.set_caption("Snake Game")

#Colours

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue=(0,0,255)
font_style = pygame.font.SysFont(None,40)
def scoree(score):
    msg = font_style.render("Score :"+str(score), True, Black)
    window.blit(msg, (50,50))
def message(content,posx,posy):
    msg = font_style.render(content,True,Red)
    window.blit(msg,(posx,posy))

def snk(snk_list):
    for s in snk_list:
        window.blit(snak,(s[0],s[1]))


obs=[(100,200,100,20),(400,100,20,100),(100,400,100,20),(300,500,200,20),(900,200,20,100),(800,600,300,20),(500,300,20,100)]
#clock
clock = pygame.time.Clock()

#snk = snake
snk_block = 20
snk_speed = 10
bg2 = pygame.image.load('bg2.jpg')
bg2 = pygame.transform.scale(bg2,(info.current_w,info.current_h))
straw = pygame.image.load('strawberry.png')
straw = pygame.transform.scale(straw,(snk_block,snk_block))
snak = pygame.image.load('snk.png')
snak = pygame.transform.scale(snak,(snk_block,snk_block))
apple_sound = pygame.mixer.Sound('crunchy-bite-001-86703.mp3')
def gameloop():
    run = True
    close = False
    scores = 0
    foodx = round(random.randrange(20,info.current_w,20))
    foody = round(random.randrange(20,info.current_h,20))

    snk_list = []
    snk_len = 1
    x1 =info.current_w/2
    y1 = info.current_h/2
    x2 = 0
    y2 = 0
    while run:

        while close:
            window.fill(White)
            message("You Lost!",info.current_w/3,250)
            message("Press P to Play again",info.current_w/3,300)
            message("Press Q to Quit",info.current_w/3,350)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameloop()
                    if event.key == pygame.K_q:
                        close = False
                        run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x2 = -snk_speed
                    y2 = 0
                if event.key == pygame.K_RIGHT:
                    x2 = +snk_speed
                    y2 = 0
                if event.key == pygame.K_UP:
                    y2 = -snk_speed
                    x2 = 0
                if event.key == pygame.K_DOWN:
                    y2 = +snk_speed
                    x2 = 0
        if x1 < 0 or x1 >= info.current_w or y1 < 0 or y1 >= info.current_h:
            close = True
        x1 += x2
        y1 += y2
        window.blit(bg2,(0,0))
        clock.tick(20)
        scoree(scores)
        window.blit(straw,(foodx, foody))
        snk_head = [x1,y1]
        snk_list.append(snk_head)
        if len(snk_list)>snk_len:
            del snk_list[0]
        for x in snk_list[:-1]:
            if x == snk_head:
                close = True
        for obst in obs:
            pygame.draw.rect(window,Black,obst)
            if x1 in range(obst[0],obst[0]+obst[2]) and y1 in range(obst[1],obst[1]+obst[3]):
                close = True
            if foodx in range(obst[0],obst[0]+obst[2]) and foody in range(obst[1],obst[1]+obst[3]):
                foodx = round(random.randrange(0, info.current_w))
                foody = round(random.randrange(0, info.current_h))
        snk(snk_list)
        if( x1+snk_block > foodx and x1 < foodx+snk_block and y1+snk_block > foody and y1 < foody+snk_block):
            foodx = round(random.randrange(0, info.current_w))
            foody = round(random.randrange(0, info.current_h))
            snk_len += 1
            scores = scores + 1
            apple_sound.play()

        pygame.display.update()
gameloop()
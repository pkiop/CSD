import pygame
import csv
from decimal import *

WHITE = (255, 255, 255)
BLACK = (0,0,0)
pad_width = 1024
pad_height = 512
background_width = 1024

f = open('csvfile/disturbance.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
getcontext().prec = 1

dic = {}
for line in rdr:
    dic[line[0]] = [line[1], line[2]]

def view_degree(D):
    global gamepad
    font = pygame.font.SysFont(None, 40)
    test = font.render('Degree : ' + str(D), True, BLACK)
    gamepad.blit(test, (5 , 60))

def view_dirturbance(D):
    global gamepad
    font = pygame.font.SysFont(None, 40)
    test = font.render('Disturbance : ' + str(D), True, BLACK)
    gamepad.blit(test, (5 , 60))

def view_time(T):
    global gamepad
    font = pygame.font.SysFont(None, 40)
    test = font.render('Time : ' + str(T), True, BLACK)
    gamepad.blit(test, (5,30))

def view_velocity(V):
    global gamepad
    font = pygame.font.SysFont(None, 40)
    text = font.render('Velocity : ' + str(V), True, BLACK)
    gamepad.blit(text, (5,0))

def trainlocation(x,y):
    global gamepad, train
    gamepad.blit(train, (x,y))

def back(background, x,y):
    global gamepad
    gamepad.blit(background, (x,y))

def runGame():
    global gamepad, train, clock, background, background2, background_dis, background_dis2

    now_val = 0
    backcount = 0
    cnt = 0
    x = 0
    y = 300
    background_x = 0
    background2_x = background_width
    ended = False
    while not ended :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT PUSH")
                ended = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x = 400
                elif event.key == pygame.K_DOWN:
                    x = 400

        x_diff = 10
        background_x -= x_diff
        background2_x -= x_diff

        #clear
        gamepad.fill(WHITE)
        #draw
        if background_x <= -background_width + x_diff:
            background_x = background_width

        if background2_x <= -background_width + x_diff:
            background2_x = background_width

        if backcount <= 200:
            backcount += 1
            back(background, background_x, 0)
            back(background, background2_x, 0)
        else :
            back(background_dis, background_x, 0)
            back(background_dis2, background2_x, 0)

        # view
        mstime = pygame.time.get_ticks()
        start_time = 492
        now_val = start_time + mstime / 1000
        now_val = (int(now_val * 10))
        if now_val % 10 == 0:
            now_val = int(now_val / 10)
        else:
            now_val = now_val / 10
        now_val = str(now_val)
        view_time(now_val)
        view_velocity(dic[now_val][1])
        view_dirturbance(dic[now_val][0])
        trainlocation(x, y)

        cnt += 1

        #rotate



        pygame.display.update()
        clock.tick(60)


    pygame.quit()
    quit()

def initGame():
    global gamepad, train, clock, background, background_dis, background2, background_dis2

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('H-train disturbance simulation')
    train = pygame.image.load('image/train.png')
    train = pygame.transform.scale(train, (121*2,43*2))
    background = pygame.image.load('image/background.jpg')
    background = pygame.transform.scale(background, (1024,512))
    background_dis = pygame.image.load('image/bitrain_background.jpg')
    background_dis = pygame.transform.scale(background_dis,(1024, 512))
    background2 = background.copy()
    background_dis2 = background_dis.copy()

    clock = pygame.time.Clock()
    runGame()

initGame()



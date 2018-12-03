import pygame
import csv
from decimal import *

WHITE = (255, 255, 255)
BLACK = (0,0,0)
pad_width = 1024
pad_height = 512
background_width = 1024

f = open('csvfile/inclinedata.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
getcontext().prec = 1

dic = {}
for line in rdr:
    dic[line[0]] = line[1]

def view_degree(D):
    global gamepad
    font = pygame.font.SysFont(None, 40)
    test = font.render('Degree : ' + str(D), True, BLACK)
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
    global gamepad, train, clock, background, background2


    now_val = 0
    cnt = 0
    train_x = 0
    train_y = 330
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


        back(background, 0, 0)

        #view
        mstime=pygame.time.get_ticks()
        start_time = 490
        now_val = start_time + mstime/1000
        now_val = (int(now_val * 10))
        if now_val%10 == 0:
            now_val = int(now_val/10)
        else:
            now_val = now_val/10
        now_val = str(now_val)
        view_time(now_val)
        view_velocity(dic[now_val])
        view_degree(20)

        #rotate
        if cnt%5 == 0:
            train_x += 3
            train_y += -1
            if cnt%30 == 0:
                train_y += -1
        trainlocation(train_x, train_y)
        cnt+=1



        pygame.display.update()
        clock.tick(60)


    pygame.quit()
    quit()

def initGame():
    global gamepad, train, clock, background

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('H-Train')
    train = pygame.image.load('image/incline.png')
    train = pygame.transform.scale(train, (121*2,43*2))
    background = pygame.image.load('image/incline_back.png')
    background = pygame.transform.scale(background, (1024,512))
    background2 = background.copy()

    clock = pygame.time.Clock()
    runGame()

initGame()



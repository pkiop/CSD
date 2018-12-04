import pygame

WHITE = (255, 255, 255)
pad_width = 1024
pad_height = 512

def runGame():
    global clock

def initGame() :
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PyFlying')
    train = pygame.image.load('train.PNG')

    clock = pygame.time.Clock()
    runGame()

initGame()




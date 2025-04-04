import pygame, sys
from pygame.locals import QUIT
import random
pygame.init()
ball = pygame.image.load("ball.png")
ball_rect = ball.get_rect()
ball = pygame.transform.scale(ball, (50,50))
ball_rect = ball.get_rect()
DISPLAYSURF = pygame.display.set_mode((550, 300))
floor = pygame.image.load("floor.png")
floor = pygame.transform.scale(floor,(550, 300))
pygame.display.set_caption('doge ball')
while True:
    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
    DISPLAYSURF.blit(floor,(0,0))
    DISPLAYSURF.blit(ball, ball_rect)
    pygame.display.update()
   
    
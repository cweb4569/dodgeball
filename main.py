import pygame, sys
from pygame.locals import QUIT
import random
pygame.init()
sb = pygame.image.load("sb.png")
sb_rect = sb.get_rect()
sb = pygame.transform.scale(sb, (100,60))
ball = pygame.image.load("ball.png")
ball_rect = ball.get_rect()
ball = pygame.transform.scale(ball, (50,50))
DISPLAYSURF = pygame.display.set_mode((550, 300))
floor = pygame.image.load("floor.png")
floor = pygame.transform.scale(floor,(550, 300))
pygame.display.set_caption('doge ball')
bs = 1
while True:
    sb_rect.x += bs
    if sb_rect.x > 500:
        bs = -1
        print(bs)
    if sb_rect.x < -50:
        bs = 1
    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
    DISPLAYSURF.blit(floor,(0,0))
    DISPLAYSURF.blit(ball, ball_rect)
    DISPLAYSURF.blit(sb, sb_rect)
    pygame.display.update()
    

import pygame as pygame
import sys
from pygame import gfxdraw
from pygame.locals import *

pygame.init()

WHITE = (230, 230, 230)
GREY = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
x = 0
y = 0
posx = 50
posy = 50
sx = 320
sy = 240
coef = 5


def afficher(posx, posy):
    for x in range(sx):
        for y in range(sy):
            page.set_at((x, y), WHITE)

    carre_plein = pygame.image.load("../wolfproject/carre_plein.png").convert()
    page.blit(carre_plein, (posx, posy))
    pygame.display.flip()


while 1:
    page = pygame.display.set_mode((sx, sy))
    for x in range(sx):
        for y in range(sy):
            if 120 <= y <= 240:
                page.set_at((x, y), WHITE)
            if 0 <= y < 120:
                page.set_at((x, y), GREY)
            if sy/2 - sy/coef <= y <= sy/2 + sy/coef:
                page.set_at((x, y), RED)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            # déplacement curseur
            if event.key == pygame.K_RIGHT:
                posx += 20
            elif event.key == pygame.K_LEFT:
                posx -= 20
            elif event.key == pygame.K_UP:
                coef -= 0.2
            elif event.key == pygame.K_DOWN:
                coef += 0.2


    pygame.display.flip()

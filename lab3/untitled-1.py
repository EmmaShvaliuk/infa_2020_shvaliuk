import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (230, 200, 170), (0, 0, 400, 80))
rect(screen, (255,230,230), (0, 80, 400, 80))
rect(screen, (255, 240, 200), (0, 160, 400, 80))
rect(screen, (153, 100, 120), (0, 240, 400, 160))
circle(screen, (255, 255, 0), (200, 80), 30)
polygon(screen, (255, 140, 0), [(0,170),(5,150),(75,80),(95,85),(100,75),(150,150)])
polygon(screen, (139, 0, 0), [(0,240),(0,180),(25,190),(60,150),(80,150),(100,230),(120,200),(150,220),(170,190),(200,195),(230,220),(260,215),(295,170),(350,165),(360,185),(375,175),(385,185),(395,182),(400,150),(400,240)])

    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
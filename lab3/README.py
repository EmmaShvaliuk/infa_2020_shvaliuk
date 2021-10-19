import pygame

from pygame.draw import *

pygame.init()
t=2
FPS = 30
screen = pygame.display.set_mode((400, 400))
pi = 3.14
rect(screen, (240, 200, 170), (0, 0, 400, 80))
rect(screen, (255,230,230), (0, 80, 400, 80))
rect(screen, (240, 200, 170), (0, 160, 400, 80))
rect(screen, (153, 100, 120), (0, 240, 400, 160))
circle(screen, (255, 255, 0), (200, 80), 30)
polygon(screen, (255, 140, 0), [(0,170),(5,150),(75,80),(95,85),(100,75),(150,140),(180,135),(190,148),(210,130),(220,132),(225,117),(300,75),(310,75),(340,110),(355,107),(380,115),(385,110),(400,140)])
polygon(screen, (139, 0, 0), [(0,240),(0,180),(25,190),(60,150),(80,150),(100,230),(120,200),(150,220),(170,190),(200,195),(230,220),(260,215),(295,170),(350,165),(360,185),(375,175),(385,185),(395,182),(400,150),(400,240)])
polygon(screen,(0,0,0),[(0,400),(0,200),(70,210),(170,390),(200,390),(250,350),(300,370),(400,200),(400,400)])
aalines(screen, (139, 0, 0), False,[(0,240),(0,180),(25,190),(60,150),(80,150),(100,230),(120,200),(150,220),(170,190),(200,195),(230,220),(260,215),(295,170),(350,165),(360,185),(375,175),(385,185),(395,182),(400,150),(400,240)])
aalines(screen, (255, 140, 0), True,[(0,170),(5,150),(75,80),(95,85),(100,75),(150,140),(180,135),(190,148),(210,130),(220,132),(225,117),(300,75),(310,75),(340,110),(355,107),(380,115),(385,110),(400,140)])    
aalines(screen,(0,0,0),True,[(0,400),(0,200),(70,210),(170,390),(200,390),(250,350),(300,370),(400,200),(400,400)])
def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

def BIRDS(x, y, alpha=1): 
    draw_ellipse_angle(screen, (0,0,0), [x - 12.5*alpha, y, 40*alpha, 10*alpha], -35)
    draw_ellipse_angle(screen, (0,0,0), [x + 12.5*alpha, y - 2*alpha, 43*alpha, 10*alpha], 50)

BIRDS(130, 140, 0.4)
BIRDS(150, 150, 0.4)
BIRDS(125, 160, 0.4)
BIRDS(150, 162, 0.4)
BIRDS(250, 240, 0.4)
BIRDS(300, 260, 0.4)
BIRDS(305, 250, 0.3)
BIRDS(275, 252, 0.3)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
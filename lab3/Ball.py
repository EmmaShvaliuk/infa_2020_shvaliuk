import pygame
import random
from pygame.draw import *
from math import hypot

pygame.init()
pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 40)

N = 10
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

FPS = 120
screen = pygame.display.set_mode((1000, 700))


class Ball:
    def __init__(self, coord, velocity, color, r):
        self.coord = coord
        self.velocity = velocity
        self.r = r
        self.color = color

    def move(self, dt):
        circle(screen, self.color, self.coord, self.r)
        self.coord[0] += self.velocity[0] * dt
        self.coord[1] += self.velocity[1] * dt

    def collision(self):
        if self.coord[0] - self.r < 50:
            self.velocity[0] = abs(self.velocity[0])
        elif self.coord[0] + self.r > 950:
            self.velocity[0] = -abs(self.velocity[0])

        if self.coord[1] - self.r < 50:
            self.velocity[1] = abs(self.velocity[1])
        elif self.coord[1] + self.r > 650:
            self.velocity[1] = -abs(self.velocity[1])

    def is_hit(self, cors):
        if hypot(cors[0] - self.coord[0], cors[1] - self.coord[1]) <= self.r:
            return True
        return False


class Square:
    def __init__(self, coord, velocity, color, a):
        self.coord = coord
        self.velocity = velocity
        self.a = a
        self.color = color

    def move(self, dt):
        rect(screen, self.color, (self.coord[0] - self.a / 2, self.coord[1] - self.a / 2, self.a, self.a))
        self.coord[0] += self.velocity[0] * dt
        self.coord[1] += self.velocity[1] * dt

    def collision(self):
        if self.coord[0] - self.a / 2 < 50:
            self.velocity[0] = abs(self.velocity[0])
        elif self.coord[0] + self.a / 2 > 950:
            self.velocity[0] = -abs(self.velocity[0])

        if self.coord[1] - self.a / 2 < 50:
            self.velocity[1] = abs(self.velocity[1])
        elif self.coord[1] + self.a / 2 > 650:
            self.velocity[1] = -abs(self.velocity[1])

    def is_hit(self, cors):
        if abs(cors[0] - self.coord[0]) <= self.a/2 and abs(cors[1] - self.coord[1]) <= self.a/2:
            return True
        return False


def gen_color():
    return random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)


def gen_fig():
    fig = random.randint(0, 1)
    x = random.randint(100, 900)
    y = random.randint(100, 700)
    vx = random.randint(-200, 200)
    vy = random.randint(-200, 200)
    r = random.randint(20, 50)
    color = gen_color()  # random.choice(COLORS)

    if fig == 0:
        obj = Ball([x, y], [vx, vy], color, r)
        obj.points_for_hit = 10
    else:
        obj = Square([x, y], [vx, vy], color, 2 * r)
        obj.points_for_hit = 20
    return obj


objects = []
for i in range(2 * N):
    objects.append(gen_fig())

pygame.display.update()
clock = pygame.time.Clock()
finished = False

points = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for obj in objects:
                if obj.is_hit(event.pos):
                    objects.remove(obj)
                    objects.append(gen_fig())
                    points += obj.points_for_hit
                    print(points)

    font_image = font.render("Score: " + str(points), True, WHITE, BLACK)
    screen.blit(font_image, (0, 0))

    for obj in objects:
        obj.move(1 / FPS)
        obj.collision()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

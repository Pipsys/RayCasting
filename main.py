from numpy import half
import pygame
from Settings import *
from player import Player
import math 
from map import world_map
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT)) 
clock = pygame.time.Clock() 
player = Player()
drawing = Drawing(sc)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    pygame.draw.rect(sc, SKYBLUE, (0,0, WIDTH, HALF_HEIGHT)) # не трогать нахуй
    pygame.draw.rect(sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)

    # # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    # # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    # # player.y + WIDTH * math. sin(player.angle)))

    # for x,y in world_map:
    #     pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick()
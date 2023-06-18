from ipaddress import collapse_addresses
import pygame
from Settings import *
from map import world_map

def ray_casting(sc, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            # pygame.draw.line(sc, DARKGRAY, player_pos, (x, y), 2)
            if (x // TILE * TILE, y // TILE * TILE ) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                proj_height = PROJ_COEFF / depth
                c = 255 / (1 + depth * depth* 0.00002)
                color = (c, c // 2, c // 3)
                pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE

# def mapping (a, b):
#     return (a // TILE) * TILE, (b //TILE) * TILE

# def ray_casting(sc, player_pos, player_angle):
#     ox, oy = player_pos
#     xm, ym = mapping(ox, oy)
#     cur_angle = player_angle - HALF_FOV
#     for ray in range(NUM_RAYS):
#         sin_a = math.sin(cur_angle)
#         cos_a = math.cos(cur_angle)

#     # x, dx = (xm + TILE, 1) if cos_a >= 0 else(xm, -1) 
#         if cos_a >= 0:
#             x = xm + TILE
#             dx = 1
#         else:
#             x = xm
#             x = -1 
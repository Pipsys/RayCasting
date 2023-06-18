import math

# game settings
WIDTH = 1200 # Ширина 
HEIGHT = 800 # Высота 
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
FPS_POS = (WIDTH - 65, 5)
TILE = 100

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# player settings 
player_pos = (HALF_WIDTH, HALF_HEIGHT)
palyer_angle = 0
player_speed = 1

# colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
YELLOW = (255, 186, 0)
SKYBLUE = (0, 186, 255)

from handle_grid import *
from handle_pygame import *
import random


screen = init_screen()

size, step, nb_steps = 70, 10, 1000
seed = random.randint(0, 1000)

grid = generate_perlin_grid(size, 1.6, seed)

draw_grid(screen, grid, size)

draw_flow_both_directions_grid_points(screen, grid, size, nb_steps, step)
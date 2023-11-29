from handle_grid import *
from handle_pygame import *
import random


size = 70
step = 10
nb_steps = 1000
seed = random.randint(0, 1000)
grid = generate_perlin_grid(size, 2, seed)

screen = init_screen()

draw_grid(screen, grid, size)

while handle_events():
    draw_flow_thread(screen, grid, size, nb_steps, step, 10)
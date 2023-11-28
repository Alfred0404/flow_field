from handle_grid import *
from handle_pygame import *


size = 50
step = 4
nb_steps = 100
grid = fill_grid_perlin_noise(size, 'assets/perlin_noise.png')

screen = init_screen()

draw_grid(screen, grid, size)

while handle_events():
    draw_flow(screen, grid, size, nb_steps * step, step)
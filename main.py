from handle_grid import *
from handle_pygame import *


size = 50

grid = fill_grid_perlin_noise(size, 'assets/perlin_noise.png')


screen = init_screen()

while True:
    handle_events()

    # point = (346, 178)
    # closest_point = get_closest_point_dir(screen, grid, size, point[0], point[1])
    # calculate_angle(screen, grid, size, point[0], point[1])
    # draw_grid(screen, grid, size)
    # # print(closest_point)
    # draw_curve(screen, grid, size, point[0], point[1], 50, 10)
    draw_flow(screen, grid, size, 100, 2)
    # pygame.display.update()
import pygame
import math
import time
import random

HEIGHT = 800
WIDTH  = 800

def init_screen(width = WIDTH, height = HEIGHT) :
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    screen.fill((26, 27, 38))

    pygame.display.set_caption('Flow field')

    return screen


def handle_events():
    run = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == 27):
            run = False
    return run


def draw_grid(screen, grid, grid_size):
    offset = WIDTH / grid_size
    vector_lenght = offset / 2 + 5

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            x = i * offset + offset/2
            y = j * offset + offset/2
            angle = math.radians(grid[i][j])
            x2 = x + math.cos(angle) * vector_lenght
            y2 = y + math.sin(angle) * vector_lenght

            pygame.draw.line(screen, (100, 100, 100), (x, y), (x2, y2), 2)


def get_closest_point_dir(screen, grid, grid_size, x, y) :

    min_dist = math.inf
    offset = WIDTH / grid_size

    for i in range(len(grid)) :
        for j in range(len(grid[i])) :

            dist = math.sqrt((x - i * offset - offset/2) ** 2 + (y - j * offset - offset/2) ** 2)

            if dist < min_dist :
                min_dist = dist
                closest_point = (i, j)

    # pygame.draw.circle(screen, (0, 255, 255), (x, y), 5)
    # pygame.draw.circle(screen, (255, 0, 0), (closest_point[0] * offset + offset/2, closest_point[1] * offset + offset/2), 5)
    # pygame.display.update()

    return closest_point


def calculate_angle(screen, grid, grid_size, x, y) :
    offset = WIDTH / grid_size
    closest_point = get_closest_point_dir(screen, grid, grid_size, x, y)

    angle = math.radians(grid[closest_point[0]][closest_point[1]])


    return angle


def draw_curve(screen, grid, grid_size, x, y, nb_steps, distance) :
    offset = WIDTH / grid_size
    closest_point = get_closest_point_dir(screen, grid, grid_size, x, y)
    r, g, b = [255 * random.random(), 255 * random.random(), 255 * random.random()]

    for i in range(nb_steps) :
        angle = math.radians(grid[closest_point[0]][closest_point[1]])

        new_x = math.cos(angle) * distance
        new_y = math.sin(angle) * distance

        pygame.draw.line(screen, (255 * angle/5, 100, 100), (x, y), (x + new_x, y + new_y), 2)

        x += new_x
        y += new_y

        closest_point = get_closest_point_dir(screen, grid, grid_size, x, y)
    pygame.display.update()


def draw_flow(screen, grid, grid_size, nb_steps, distance) :
    point = (int(WIDTH * random.random()), int(HEIGHT * random.random()))
    draw_curve(screen, grid, grid_size, point[0], point[1], nb_steps, distance)

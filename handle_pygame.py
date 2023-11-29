import pygame
import math
import random
import threading


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

            pygame.draw.circle(screen, (46, 47, 58), (int(x), int(y)), 2)
            pygame.draw.line(screen, (46, 47, 58), (x, y), (x2, y2), 1)


def get_closest_point_dir(screen, grid, grid_size, x, y) :

    min_dist = math.inf
    offset = WIDTH / grid_size

    for i in range(len(grid)) :
        for j in range(len(grid[i])) :

            dist = math.sqrt((x - i * offset - offset/2) ** 2 + (y - j * offset - offset/2) ** 2)

            if dist < min_dist :
                min_dist = dist
                closest_point = (i, j)

    return closest_point


def calculate_angle(screen, grid, grid_size, x, y) :
    closest_point = get_closest_point_dir(screen, grid, grid_size, x, y)

    angle = math.radians(grid[closest_point[0]][closest_point[1]])

    return angle


def draw_curve(screen, grid, grid_size, x, y, nb_steps, distance) :
    closest_point = get_closest_point_dir(screen, grid, grid_size, x, y)

    random_value = 70 * random.uniform(-1, 1)

    r, g, b = min(175 + random_value, 255), 0, 0

    for i in range(nb_steps) :
        angle = math.radians(grid[closest_point[0]][closest_point[1]])

        new_x = math.cos(angle) * distance
        new_y = math.sin(angle) * distance

        if x + new_x < 0 or x + new_x > WIDTH or y + new_y < 0 or y + new_y > HEIGHT :
            break


        pygame.draw.line(screen, (r, g, b), (x, y), (x + new_x, y + new_y), 1)

        x += new_x
        y += new_y

        closest_point = get_closest_point_dir(screen, grid, grid_size, x, y)
        pygame.display.update()


def draw_flow(screen, grid, grid_size, nb_steps, distance) :
    side = random.randint(0, 3)

    if side == 0 :
        point = (int(WIDTH * random.random()), 0)

    elif side == 1 :
        point = (WIDTH, int(HEIGHT * random.random()))

    elif side == 2 :
        point = (int(WIDTH * random.random()), HEIGHT)

    elif side == 3 :
        point = (0, int(HEIGHT * random.random()))

    draw_curve(screen, grid, grid_size, point[0], point[1], nb_steps, distance)


def draw_flow_thread(screen, grid, grid_size, nb_steps, distance, nb_curves = 10) :

    threads = []
    for i in range(nb_curves) :
        t = threading.Thread(target=draw_flow, args=(screen, grid, grid_size, nb_steps, distance))
        threads.append(t)
        t.start()

    for t in threads :
        t.join()

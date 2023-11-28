import math
from random import random, randint
from PIL import Image


def fill_grid_perlin_noise(grid_size, path) :
    grid = [[360 * (i + j + 1) for i in range(grid_size)] for j in range(grid_size)]

    img = Image.open(path)
    img = img.resize((grid_size, grid_size))
    img = img.convert('L')

    pixels = img.load()

    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = pixels[i, j]

    return grid


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='\t')
        print()

import math
from random import random, randint
from PIL import Image
from perlin_noise import PerlinNoise


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


def generate_perlin_grid(grid_size, octaves, seed) :
    noise1 = PerlinNoise(octaves=octaves, seed=seed)
    noise2 = PerlinNoise(octaves=2*octaves, seed=seed)
    noise3 = PerlinNoise(octaves=3*octaves, seed=seed)
    noise4 = PerlinNoise(octaves=4*octaves, seed=seed)

    perlin_grid = []
    for i in range(grid_size) :
        row = []
        for j in range(grid_size):
            noise_val = noise1([i/grid_size, j/grid_size])
            noise_val += 0.5 * noise2([i/grid_size, j/grid_size])
            noise_val += 0.25 * noise3([i/grid_size, j/grid_size])
            noise_val += 0.125 * noise4([i/grid_size, j/grid_size])
            noise_val *= 360

            row.append(noise_val)
        perlin_grid.append(row)
    return perlin_grid


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='\t')
        print()

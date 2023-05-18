#!/usr/bin/env python
"""day 11 part 1"""

import numpy as np


def evolve_grid(grid):
    """increase all values by 1 and set 9 to 0"""
    return (grid + 1) % 10


def get_neighbour_locations(i, j):
    """get coordinates for neighbours regardless of conditions"""
    return [
        (i - 1, j),
        (i + 1, j),
        (i - 1, j - 1),
        (i - 1, j + 1),
        (i + 1, j + 1),
        (i + 1, j - 1),
        (i, j - 1),
        (i, j + 1),
    ]


def check_for_neighbours(grid, i, j):
    """return adjacent and diagonal octopi"""
    neighbours = [[False for _ in range(3)] for _ in range(3)]
    neighbours[1][1] = True
    coordinates = get_neighbour_locations(i, j)
    for coord in coordinates:
        if 0 <= coord[0] <= len(grid) - 1 and 0 <= coord[1] <= len(grid[0]) - 1:
            neighbours[abs(coord[0] - i + 1)][abs(coord[1] - j + 1)] = True
    return neighbours


def get_pre_flash(grid):
    """get the coordinates of zeros"""
    return list(
        zip(
            np.where(
                grid == 0,
            )[0].tolist(),
            np.where(
                grid == 0,
            )[1].tolist(),
        )
    )


def affect_neighbours(grid, i, j):
    """for octopi that flashes, affect its neighbours"""
    coord = check_for_neighbours(grid, i, j)
    for i_a, t_v_line in enumerate(coord):
        for i_b, t_v in enumerate(t_v_line):
            if t_v and 0 < grid[i + i_a - 1][j + i_b - 1]:
                grid[i + i_a - 1][j + i_b - 1] = (
                    grid[i + i_a - 1][j + i_b - 1] + 1
                ) % 10
    return grid


with open("day11-input", "r") as data:
    octo_grid = np.array(
        [list(map(int, line.strip("\n"))) for line in data.readlines()]
    )
    COUNTER = 0
    STEPS = 100
    while True:
        if STEPS == 0:
            break
        STEPS -= 1
        octo_grid = evolve_grid(octo_grid)
        seen = []
        to_flash = set(get_pre_flash(octo_grid))
        while len(to_flash) > 0:
            coord = to_flash.pop()
            if coord not in seen:
                octo_grid = affect_neighbours(octo_grid, coord[0], coord[1])
                COUNTER += 1
                to_flash = set(get_pre_flash(octo_grid))
                seen.append(coord)
    print(COUNTER)

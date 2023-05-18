#!/usr/bin/env python
""" day 9 part 2 """

from collections import Counter
import numpy as np


def remove_not_deepest(line_map, replace):
    """Remove areas of non troughs"""
    map_horizontal = list(line_map)
    for i in range(len(line_map) - 1):
        if line_map[i] >= line_map[i + 1]:
            map_horizontal[i] = replace
    map_horizontal, line_map = map_horizontal[::-1], line_map[::-1]
    for i in range(len(line_map) - 1):
        if line_map[i] >= line_map[i + 1]:
            map_horizontal[i] = replace
    return map_horizontal[::-1]


def deepest_coordinates(horiz, vert):
    """Find the coordinates for the troughs"""
    return list(
        zip(
            np.concatenate(
                (np.where(np.array(vert).T == np.array(horiz))[0],)
            ).tolist(),
            np.concatenate(
                (np.where(np.array(vert).T == np.array(horiz))[1],)
            ).tolist(),
        )
    )


def flood_recursive(heightmap_f, x, y, key):
    """run recursive floodfill until it's done"""

    def floodfill(x, y, key):
        """floodfill algorithm to fill each basin with a unique number"""
        if heightmap_f[x][y] != 0:
            return
        if heightmap_f[x][y] == key:
            return
        heightmap_f[x][y] = key
        neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for coord_f in neighbours:
            if (
                0 <= coord_f[0] <= len(heightmap_f) - 1
                and 0 <= coord_f[1] <= len(heightmap_f[0]) - 1
            ):
                floodfill(coord_f[0], coord_f[1], key)

    floodfill(x, y, key)
    return heightmap_f


def get_result(heightmap_r):
    """get the product of the 3 biggest basins"""
    heightmap_r = Counter(heightmap_r)
    heightmap_r[-1] = 0
    return np.prod([size[1] for size in heightmap_r.most_common(3)])


with open("day9-input", "r") as data:
    heightmap = [list(map(int, list(line.strip("\n")))) for line in data.readlines()]
    result_h, result_v = [], []
    for line in heightmap:
        result_h.append(remove_not_deepest(line, -1))
    for line in np.array(heightmap).T.tolist():
        result_v.append(remove_not_deepest(line, -2))
    coordinates = deepest_coordinates(result_h, result_v)
    fill_key = {coordinates[i]: i + 1 for i in range(len(coordinates))}
    heightmap = np.where(np.array(heightmap) != 9, 0, -1).tolist()
    for coord in fill_key:
        heightmap = flood_recursive(heightmap, coord[0], coord[1], fill_key[coord])
    print(get_result(np.array(heightmap).flatten().tolist()))

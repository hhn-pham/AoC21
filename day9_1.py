#!/usr/bin/env python
""" day 9 part 1 """

import numpy as np


def compare(line_map):
    """Find deep areas"""
    map_horizontal = list(line_map)
    for i in range(len(line_map) - 1):
        if line_map[i] >= line_map[i + 1]:
            map_horizontal[i] = -1
    map_horizontal, line_map = map_horizontal[::-1], line_map[::-1]
    for i in range(len(line_map) - 1):
        if line_map[i] >= line_map[i + 1]:
            map_horizontal[i] = -1
    return map_horizontal[::-1]


with open("test-input-day9", "r") as data:
    heightmap = [list(map(int, list(line.strip("\n")))) for line in data.readlines()]
    result_h, result_v = [], []
    for line in heightmap:
        result_h.append(compare(line))
    heightmap = np.array(heightmap).T.tolist()
    for line in heightmap:
        result_v.append(compare(line))
    result_v = np.array(result_v).T.tolist()
    risk_locations = np.array(
        [
            result_v[i][j]
            for i in range(len(result_v))
            for j in range(len(result_v[0]))
            if result_v[i][j] == result_h[i][j]
        ]
    )
    print(sum(risk_locations + 1))

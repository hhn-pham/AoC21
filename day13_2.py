#!/usr/bin/env python
"""day 13 part 2"""
from collections import Counter
import numpy as np


def fold(coordinates, fold_line, is_left):
    """reflect along axis"""
    if is_left:
        folded_half = [
            (2 * fold_line - line[0], line[1])
            for line in coordinates
            if line[0] > fold_line
        ]
        original_half = [
            tuple(line)
            for line in coordinates
            if line[0] < fold_line
        ]
    else:
        folded_half = [
            (line[0], 2 * fold_line - line[1])
            for line in coordinates
            if line[1] > fold_line
        ]
        original_half = [
            tuple(line)
            for line in coordinates
            if line[1] < fold_line
        ]
    return list(set(original_half + folded_half))


with open("day13-input", "r") as data:
    coordinates_global = [line.strip("\n") for line in data.readlines()]
instructions = [line.split(" ")[-1] for line in coordinates_global if "f" in line]
coordinates_global = [
    tuple(map(int, coord))
    for coord in [line.split(",") for line in coordinates_global if "f" not in line][
        :-1
    ]
]
for instruction in instructions:
    left = instruction[0] == "x"
    coordinates_global = fold(coordinates_global, int(instruction[2:]), left)
max_a = max([line[0] for line in coordinates_global])
max_b = max([line[1] for line in coordinates_global])
secret = np.zeros((max_b+1,max_a+1),dtype="int64")
for coord in coordinates_global:
    if coord[1] >= 0 and coord[0] >= 0:
        secret[coord[1]][coord[0]] = 1
secret = np.where(secret == 1, "█", " ").tolist()
for line in secret:
    print(''.join(map(str, line)))

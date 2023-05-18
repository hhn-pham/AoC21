#!/usr/bin/env python
"""day 13 part 1"""
from collections import Counter


def fold(coordinates, fold_line, is_left):
    """reflect along axis"""
    if is_left:
        folded_half = [
            (2 * fold_line - line[0], line[1])
            for line in coordinates
            if line[0] > fold_line
        ]
        original_half = [tuple(line) for line in coordinates if line[0] < fold_line]
    else:
        folded_half = [
            (line[0], 2 * fold_line - line[1])
            for line in coordinates
            if line[1] > fold_line
        ]
        original_half = [tuple(line) for line in coordinates if line[1] < fold_line]
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
left = instructions[0][0] == "x"
print(len(Counter(fold(coordinates_global, int(instructions[0][2:]), left))))

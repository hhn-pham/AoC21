#!/usr/bin/env python
""" env """
with open("day1-input", "r") as puzzle_input:
    depths = [int(depth) for depth in puzzle_input.readlines()]
    previous, COUNTER = int(sum(depths[0:3])), 0
    for value in range(len(depths)):
        if int(sum(depths[value : value + 3])) > previous:
            COUNTER += 1
        previous = int(sum(depths[value : value + 3]))
    print(COUNTER)

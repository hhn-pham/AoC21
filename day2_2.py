#!/usr/bin/env python
"""day 2 part 2"""
coordinate = [0, 0, 0]
with open("day2-input", "r") as commands:
    for line in commands.readlines():
        if line.split()[0] == "forward":
            coordinate[0] += int(line.split()[1])
            coordinate[1] += coordinate[2] * int(line.split()[1])
        elif line.split()[0] == "down":
            coordinate[2] += int(line.split()[1])
        else:
            coordinate[2] -= int(line.split()[1])
print(coordinate[0] * coordinate[1])

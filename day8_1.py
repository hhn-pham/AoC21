#!/usr/bin/env python
""" env """

with open("day8-input", "r") as data:
    segments = [n.strip("\n").split(" | ")[1].split(" ") for n in data.readlines()]
    COUNT = 0
    for i,digit in enumerate(segments):
        for j in range(4):
            if len(digit[j]) in [2,3,4,7]:
                COUNT += 1
    print(segments)
    print(COUNT)

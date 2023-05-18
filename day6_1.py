#!/usr/bin/env python
""" env """

def grow_fish(fish, days):
    """ woot """
    for _ in range(days):
        for i, target in enumerate(fish):
            if target != 0:
                fish[i] -= 1
            elif target ==0:
                fish[i] = 6
                fish.append(9)
    return len(fish)

with open("day6-input", "r") as initial_fish_data:
    fish_data = [
        list(map(int, line.strip("\n").split(",")))
        for line in initial_fish_data.readlines()
    ][0]
    print(grow_fish(fish_data, 80))

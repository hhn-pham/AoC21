#!/usr/bin/env python
""" env """


def draw_vents(x_1, x_2, y_1, y_2, vent_map):
    """add to dictionary of vents"""
    for vent_x in range(min(x_1, x_2), max(x_1, x_2) + 1):
        for vent_y in range(min(y_1, y_2), max(y_1, y_2) + 1):
            vent_map[(vent_x, vent_y)] = vent_map.get((vent_x, vent_y), 0) + 1
    return vent_map


with open("day5-input", "r") as vent_list:
    vent_map_global, POINTS = {}, 0
    for line in vent_list.readlines():
        start, end = line.split(" -> ")
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        if x1 == x2 or y1 == y2:
            vent_map_global = draw_vents(x1, x2, y1, y2, vent_map_global)
    for overlap in vent_map_global.values():
        if overlap > 1:
            POINTS += 1
    print(POINTS)

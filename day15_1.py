#!/usr/bin/env python
"""day 15 part 1"""

import heapq
from collections import defaultdict
from math import inf as INFINITY


def get_neighbours(x, y, x_size, y_size):
    "get the neighbours given location, no diagonal neighbours"
    neighbours = []
    for neighbour in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= neighbour[0] <= x_size and 0 <= neighbour[1] <= y_size:
            neighbours.append((neighbour[0], neighbour[1]))
    return neighbours


def run_dijsktra(grid):
    """Dijsktra's algorithm which contains
    two main operations that repeats until we reach the end goal
    1. Update the neighbour's risk levels (current's node risk + neighbour's risk).
    2. Explore the neighbour with the lowest risk.
    All the while maintaining a min heap that is updated every time
    a neighbour is updated.
    """
    queue, visited = [(0, (0, 0))], set()
    minimum_risk = defaultdict(lambda: INFINITY, {(0, 0): 0})

    while len(queue) != 0:
        risk, node = heapq.heappop(queue)
        if node == (len(grid) - 1, len(grid[0]) - 1):
            return risk
        if node not in visited:
            visited.add(node)
            for neighbour in get_neighbours(
                node[0], node[1], len(grid) - 1, len(grid[0]) - 1
            ):
                if neighbour not in visited:
                    minimum_risk[neighbour] = min(
                        risk + grid[neighbour[0]][neighbour[1]], minimum_risk[neighbour]
                    )
                    heapq.heappush(queue, (minimum_risk[neighbour], neighbour))
    return INFINITY


with open("day15-input", "r") as data:
    risk_levels = [list(map(int, list(line.strip("\n")))) for line in data.readlines()]
print(run_dijsktra(risk_levels))

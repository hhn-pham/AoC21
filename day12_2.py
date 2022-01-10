#!/usr/bin/env python
"""day 12 part 2"""

from collections import defaultdict
from functools import lru_cache


@lru_cache(maxsize=None)
def dfs(start_name, seen, second_cave):
    """dfs"""
    if start_name == "end":
        return 1
    if start_name == "start" and len(seen) != 0:
        return 0
    if start_name.islower() and start_name in seen:
        if second_cave == "":
            second_cave = start_name
        else:
            return 0
    seen = seen | {start_name}
    count = 0
    for route in links[start_name]:
        count += dfs(route, seen, second_cave)
    return count


with open("day12-input") as data:
    data = [line.strip("\n") for line in data.readlines()]
links = defaultdict(list)
for line in data:
    name1, name2 = line.split("-")
    links[name1].append(name2)
    links[name2].append(name1)
number_of_paths = dfs("start", frozenset(), "")
print(number_of_paths)

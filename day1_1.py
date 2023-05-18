#!/usr/bin/env python
"""day 1 part 1"""

with open("day1-input", "r") as puzzle_input:
    previous, COUNTER = int(next(puzzle_input).strip("\n")), 0
    for line in puzzle_input:
        if int(line.strip("\n")) > previous:
            COUNTER += 1
        previous = int(line.strip("\n"))
print(COUNTER)

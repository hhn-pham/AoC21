#!/usr/bin/env python
""" env """
import numpy as np

with open("day7-input", "r") as data:
    positions = list(map(int, data.readlines()[0].strip("\n").split(",")))
    positions, fuel, steps = (
        np.array(positions),
        np.zeros(len(positions), dtype="int64"),
        np.zeros(len(positions), dtype="int64"),
    )
    MINIMUM = 9999999999
    for mean in range(min(positions), max(positions)):
        MINIMUM = min(
            MINIMUM, int(sum(abs(positions - mean) * (abs(positions - mean) + 1) / 2))
        )
    print(MINIMUM)

#!/usr/bin/env python
""" env """
import numpy as np

with open("day7-input", "r") as data:
    positions = list(map(int, data.readlines()[0].strip("\n").split(",")))
    positions = np.array(positions)
    MINIMUM_STEPS = 9999999
    for mean in range(min(positions), max(positions)):
        MINIMUM_STEPS = min(sum(abs(positions - mean)), MINIMUM_STEPS)
    print(MINIMUM_STEPS)

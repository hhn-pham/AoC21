#!/usr/bin/env python
"""day 3 part 1"""
from collections import Counter
import numpy as np

with open("day3-input", "r") as diagnostics:
    table = np.array(
        [list(line.strip("\n")) for line in diagnostics.readlines()]
    ).T.tolist()
gamma = [Counter(bit).most_common()[0][0] for bit in table]
epsilon = [Counter(bit).most_common()[-1][0] for bit in table]
print(int("".join(gamma), 2) * int("".join(epsilon), 2))

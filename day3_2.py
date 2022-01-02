#!/usr/bin/env python
""" env """

from collections import Counter
import numpy as np


def get_rating(rating_table, criteria, bit_max_position):
    """solution method"""
    target_bit = np.array(rating_table).T.tolist()[-bit_max_position]
    if "".join(target_bit).count("1") != "".join(target_bit).count("0"):
        target = Counter(target_bit).most_common()[criteria][0]
    else:
        target = str(1 - criteria)
    rating_table = [
        sub_bit for sub_bit in rating_table if sub_bit[-bit_max_position] == target
    ]
    return (
        rating_table
        if len(rating_table) == 1
        else get_rating(rating_table, criteria, bit_max_position - 1)
    )


with open("day3-input", "r") as diagnostics:
    table = [list(line.strip("\n")) for line in diagnostics.readlines()]
    OXYGEN_RATING = get_rating(table, 0, len(table[0]))
    CO2_RATING = get_rating(table, 1, len(table[0]))
    print(int("".join(OXYGEN_RATING[0]), 2) * int("".join(CO2_RATING[0]), 2))

#!/usr/bin/env python
"""day 14 part 1"""
from collections import Counter


def append_alternate(final, insertion, first_element):
    """append each element of one list to another list every other index"""
    for i in range(first_element, len(final), 2):
        final[i] = insertion[int(i / 2)]
    return final


with open("day14-input", "r") as data:
    sequence = [line.strip("\n") for line in data.readlines()]

template = list(sequence[0])
rules = {item.split(" -> ")[0]: item.split(" -> ")[1] for item in sequence[2:]}

for step in range(10):
    new_insertions = [
        rules[template[i] + template[i + 1]] for i in range(len(template) - 1)
    ]
    new_template = [""] * (len(template) + len(new_insertions))
    new_template = append_alternate(new_template, template, 0)
    new_template = append_alternate(new_template, new_insertions, 1)
    template = new_template

print(Counter(template).most_common()[0][1] - Counter(template).most_common()[-1][1])

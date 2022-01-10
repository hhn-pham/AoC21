#!/usr/bin/env python
"""day 14 part 2"""
from collections import Counter

with open("day14-input", "r") as data:
    sequence = [line.strip("\n") for line in data.readlines()]

pairs = Counter(
    [sequence[0][i] + sequence[0][i + 1] for i in range(len(sequence[0]) - 1)]
)
rules = {
    item.split(" -> ")[0]: [
        item.split(" -> ")[0][0] + item.split(" -> ")[1],
        item.split(" -> ")[1] + item.split(" -> ")[0][1],
    ]
    for item in sequence[2:]
}

for step in range(40):
    temp_pairs = dict(pairs)
    for pair in pairs:
        if pairs[pair] > 0:
            for new_pair in rules[pair]:
                temp_pairs[new_pair] = temp_pairs.get(new_pair, 0) + pairs[pair]
            temp_pairs[pair] = temp_pairs[pair] - pairs[pair]
    pairs = dict(temp_pairs)
count_char = {}
for pair in pairs:
    if pairs[pair] > 0:
        count_char[pair[0]] = count_char.get(pair[0], 0) + pairs[pair]
count_char[sequence[0][-1]] = count_char.get(sequence[0][-1], 0) + 1
print(Counter(count_char).most_common()[0][1] - Counter(count_char).most_common()[-1][1])

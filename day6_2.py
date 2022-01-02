#!/usr/bin/env python
""" env """


with open("day6-input", 'r') as fish_data:
    data = fish_data.readlines()
    data = list(map(int, data[0].strip().split(",")))
fish = [data.count(i) for i in range(9)]
for i in range(256):
    num_breed_reset = fish.pop(0)
    fish[6] += num_breed_reset
    fish.append(num_breed_reset)
print(sum(fish))

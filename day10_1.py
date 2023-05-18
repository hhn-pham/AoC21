#!/usr/bin/env python
""" day 10 part 1 """


def get_line_score(line_g):
    """find point of first closing bracket that causes corruption"""
    bracket_pairs = {"}": ["{",1197], "]": ["[",57], ")": ["(",3], ">": ["<",25137]}
    stack = []
    for bracket in line_g:
        if bracket in bracket_pairs:
            if not stack or stack.pop() != bracket_pairs[bracket][0]:
                return bracket_pairs[bracket][1]
        else:
            stack.append(bracket)
    return 0

with open("day10-input", "r") as data:
    bracket_lines = [line.strip("\n") for line in data.readlines()]
    SCORE = 0
    for line in bracket_lines:
        SCORE += get_line_score(line)
    print(SCORE)

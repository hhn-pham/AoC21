#!/usr/bin/env python
""" day 10 part 2 """


def get_extra_brackets(line_g):
    """find point of first closing bracket that causes corruption"""
    bracket_pairs = {"}": "{", "]": "[", ")": "(", ">": "<"}
    stack = []
    for bracket_g in line_g:
        if bracket_g in bracket_pairs:
            if not stack or stack.pop() != bracket_pairs[bracket_g]:
                return []
        else:
            stack.append(bracket_g)
    return stack


with open("day10-input", "r") as data:
    bracket_lines = [line.strip("\n") for line in data.readlines()]
    bracket_scores = {"(": 1, "[": 2, "{": 3, "<": 4}
    all_scores = []
    for line in bracket_lines:
        if len(get_extra_brackets(line)) != 0:
            SCORE = 0
            remaining_brackets = get_extra_brackets(line)[::-1]
            for bracket in remaining_brackets:
                SCORE = SCORE * 5
                SCORE += bracket_scores.get(bracket)
            all_scores.append(SCORE)
    print(sorted(all_scores)[int(len(all_scores) / 2)])

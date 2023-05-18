#!/usr/bin/env python
"""day 4 part 1"""
import numpy as np

def is_bingo(board_bingo):
    """check bingo"""
    for row in board_bingo:
        if sum(row) == -5:
            return True
    for row in np.array(board_bingo).T.tolist():
        if sum(row) == -5:
            return True
    return False


def play_bingo(board_play, draws_play):
    """play bingo"""
    steps = 0
    for number in draws_play:
        for row_num, row in enumerate(board_play):
            if number in row:
                board_play[row_num][row.index(number)] = -1
        steps += 1
        if is_bingo(board_play):
            return [
                number
                * sum(
                    element for line in board_play for element in line if element != -1
                ),
                steps,
            ]
    return [-1, steps]


with open("day4-input", "r") as puzzle_input:
    draws = list(map(int, list(next(puzzle_input).split(","))))
    board_parser = [
        line.strip("\n").split()
        for line in list(puzzle_input.readlines()[1:])
        if len(line.strip("\n").split()) != 0
    ]

board, top_score = [], [0, 1000000]
for i in range(0, len(board_parser), 5):
    board = [list(map(int, line)) for line in board_parser[i : i + 5]]
    result = play_bingo(board, draws)
    if result is not None and result[1] < top_score[1]:
        top_score = result

print(top_score[0])

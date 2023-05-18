#!/usr/bin/env python
""" env """


def solver_parts(helper):
    """find the keys needed to determine other numbers"""
    parts = {}
    for digit in helper:
        if len(digit) in [2, 3, 4, 7]:
            parts[len(digit)] = list(digit)
    parts[3] = [digit for digit in parts[3] if digit not in parts[2]]
    parts[4] = [digit for digit in parts[4] if digit not in parts[2]]
    parts[7] = [
        digit
        for digit in parts[7]
        if digit not in parts[2] and digit not in parts[3] and digit not in parts[4]
    ]
    return parts


def solver_puzzle(parts, puzzle):
    """return the sum of all digits, takes in 4 strings and the key"""
    result = [0] * 4
    for i, digit in enumerate(puzzle):
        result[i] = get_num(parts, digit)
    return int("".join(list(map(str, result))))


def get_num(parts, digit):
    """get the number of the digit"""
    unique_case = {2: 1, 3: 7, 4: 4, 7: 8}
    if len(digit) in unique_case:
        return unique_case.get(len(digit))
    return get_num_more(parts, digit)


def get_num_more(parts, digit):
    """for non-unique numbers"""
    if is_zero(parts, digit):
        return 0
    if is_two(parts, digit):
        return 2
    if is_three(parts, digit):
        return 3
    if is_five(parts, digit):
        return 5
    if is_six(parts, digit):
        return 6
    return 9


def pass_segment(parts, digit, target):
    """func to return whether condition to match a certain number was met"""
    match_condition = {2: 2, 3: 1, 4: 2, 7: 2}
    if (
        sum(match in parts.get(target) for match in list(digit))
        == match_condition[target]
    ):
        return True
    return False


def is_zero(parts, digit):
    """ZERO needs to pass 7 and 3 and 2
    and not 4"""
    return (
        pass_segment(parts, digit, 7)
        and pass_segment(parts, digit, 3)
        and pass_segment(parts, digit, 2)
        and not pass_segment(parts, digit, 4)
    )


def is_two(parts, digit):
    """TWO needs to pass 7 and 3
    and not 4 and not 2"""
    return (
        pass_segment(parts, digit, 7)
        and pass_segment(parts, digit, 3)
        and not pass_segment(parts, digit, 4)
        and not pass_segment(parts, digit, 2)
    )


def is_three(parts, digit):
    """THREE needs to pass 2 and 3
    and not 4 and not 7"""
    return (
        pass_segment(parts, digit, 2)
        and pass_segment(parts, digit, 3)
        and not pass_segment(parts, digit, 4)
        and not pass_segment(parts, digit, 7)
    )


def is_five(parts, digit):
    """FIVE needs to pass 4 and
    and not 7 and not 2"""
    return (
        pass_segment(parts, digit, 4)
        and pass_segment(parts, digit, 3)
        and not pass_segment(parts, digit, 7)
        and not pass_segment(parts, digit, 2)
    )


def is_six(parts, digit):
    """SIX needs to pass 7 and 3 and 4
    and not 2"""
    return (
        pass_segment(parts, digit, 7)
        and pass_segment(parts, digit, 3)
        and pass_segment(parts, digit, 4)
        and not pass_segment(parts, digit, 2)
    )


def is_nine(parts, digit):
    """NINE needs to pass 7 and 2 and 4
    and not 3"""
    return (
        pass_segment(parts, digit, 7)
        and pass_segment(parts, digit, 2)
        and pass_segment(parts, digit, 4)
        and not pass_segment(parts, digit, 3)
    )


with open("day8-input", "r") as data:
    data_split = [
        [
            n.strip("\n").split(" | ")[0].split(" "),
            n.strip("\n").split(" | ")[1].split(" "),
        ]
        for n in data.readlines()
    ]
    RUNNING_TOTAL = 0
    for line in data_split:
        key = solver_parts(line[0])
        RUNNING_TOTAL += solver_puzzle(key, line[1])
    print(RUNNING_TOTAL)

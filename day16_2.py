#!/usr/bin/env python
""" day 16 part 2 """

with open("day16-input", "r") as op_stack:
    binary = bin(int("1" + op_stack.readlines()[0], 16))[3:]


def parse_packet(packet: str):
    """Recursively runs until the outermost packet is done"""
    global op_stack
    tid = int(packet[3:6], 2)
    if tid == 4:
        literal = packet[6:]
        for i, prefix in enumerate(literal[::5]):
            if int(prefix, 2) == 0:
                value = [
                    num for j, num in enumerate(literal[: (i + 1) * 5]) if j % 5 != 0
                ]
                op_stack.append(" ")
                print(f"{''.join(op_stack)}{int(''.join(value),2)}")
                eol = i * 5 + 10
                op_stack.pop()
                return eol
    else:
        print(f"{''.join(op_stack)}{op_table[tid]}")
        op_stack.append("│")
        ltid = int(packet[6], 2)
        if ltid == 0:
            length = int(packet[7:22], 2)
            cur_length_0 = 0
            while cur_length_0 < length:
                subpacket = packet[cur_length_0 + 22 :]
                cur_length_0 += parse_packet(subpacket) + 1
            op_stack.pop()
            return length + 22 - 1
        if ltid == 1:
            packet_num = int(packet[7:18], 2)
            cur_length_1 = 0
            while packet_num > 0:
                subpacket = packet[cur_length_1 + 18 :]
                cur_length_1 += parse_packet(subpacket) + 1
                packet_num -= 1
            op_stack.pop()
            return cur_length_1 + 18 - 1
    op_stack.pop()
    return 0,0


op_table = {
    0: "SUM",
    1: "PRODUCT",
    2: "MINIMUM",
    3: "MAXIMUM",
    5: "GREATER THAN",
    6: "LESS THAN",
    7: "EQUAL",
}
op_stack = []
_ = parse_packet(binary)
# from functools import reduce
# from operator import *

# with open('day16-input', 'r') as f:
#     data = f.read().strip()

# bits = [(int(c, 16) >> (3 - i)) & 1 for c in data for i in range(4)][::-1]

# def as_num(bits):
#     return reduce(lambda x, y: (x << 1) | y, bits)

# def read_bits(data, n):
#     for _ in range(n):
#         yield data.pop()

# def read_num(data, n):
#     return as_num(read_bits(data, n))

# vnum_total = 0

# def decode(data):
#     global vnum_total
#     version = read_num(data, 3)
#     vnum_total += version
#     type_id = read_num(data, 3)
#     def get_subpackets():
#         if type_id == 4:
#             while True:
#                 done = not data.pop()
#                 yield read_num(data, 4)
#                 if done:
#                     return
#         lid = data.pop()
#         if lid:
#             for _ in range(read_num(data, 11)):
#                 yield decode(data)
#         else:
#             blen = read_num(data, 15)
#             l1 = len(data) - blen
#             while len(data) != l1:
#                 yield decode(data)
#     f = [add, mul, min, max, lambda x, y: (x << 4) | y, gt, lt, eq][type_id]
#     return reduce(f, get_subpackets())

# print(decode(bits))
# print(vnum_total)

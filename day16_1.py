#!/usr/bin/env python
""" day 16 part 1 """

with open("day16-input", "r") as data:
    binary = bin(int("1" + data.readlines()[0], 16))[3:]


def parse_packet(packet: str):
    """Recursively runs until the outermost packet is done"""
    global SUM_VER
    ver = int(packet[0:3], 2)
    SUM_VER += ver
    tid = int(packet[3:6], 2)
    if tid == 4:
        literal = packet[6:]
        for i, prefix in enumerate(literal[::5]):
            if int(prefix, 2) == 0:
                eol = i * 5 + 10
                return eol
    else:
        ltid = int(packet[6], 2)
        if ltid == 0:
            length = int(packet[7:22], 2)
            cur_length_0 = 0
            while cur_length_0 < length:
                subpacket = packet[cur_length_0 + 22 :]
                cur_length_0 += parse_packet(subpacket) + 1
            return length + 22 - 1
        if ltid == 1:
            packet_num = int(packet[7:18], 2)
            cur_length_1 = 0
            while packet_num > 0:
                subpacket = packet[cur_length_1 + 18 :]
                cur_length_1 += parse_packet(subpacket) + 1
                packet_num -= 1
            return cur_length_1 + 18 - 1
    return 0


SUM_VER = 0
_ = parse_packet(binary)
print(SUM_VER)

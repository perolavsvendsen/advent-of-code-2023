"""Advent of Code - Day 8"""

import re
import itertools
import math


def test_part1():
    instructions, nodes = parse_data("data\day8_testdata1.txt")
    assert walk(instructions, nodes) == 2

    instructions, nodes = parse_data("data\day8_testdata2.txt")
    assert walk(instructions, nodes) == 6


def solution_part1():
    instructions, nodes = parse_data("data\day8_data.txt")
    stepcount = walk(instructions, nodes)
    print(f"Part 1: {stepcount}")


def test_part2():
    instructions, nodes = parse_data("data\day8_testdata3.txt")
    stepcount = walk_like_a_ghost(instructions, nodes)
    assert stepcount == 6, stepcount


def solution_part2():
    instructions, nodes = parse_data("data\day8_data.txt")
    stepcount = walk_like_a_ghost(instructions, nodes)
    print(f"Part 2: {stepcount}")


def walk(instructions, nodes, current="AAA"):
    stepcount = 0
    while current != "ZZZ":
        for instruction in instructions:
            stepcount += 1
            current = step(instruction, nodes, current)

    return stepcount


def step(instruction, nodes, current):
    if instruction == "L":
        return nodes[current][0]
    elif instruction == "R":
        return nodes[current][1]
    else:
        raise ValueError(f"Unknown instruction {instruction}")


def walk_like_a_ghost(instructions, nodes):
    currents = [node for node in nodes if node.endswith("A")]
    steps = [False for _ in currents]

    for stepcount, instruction in enumerate(itertools.cycle(instructions)):
        # Follow the instructions and walk from each starting node
        # until we have seen exactly one node that ends in Z for
        # each of the starting nodes. Then find the Lowest Common
        # Multiplier (lcm) for these, which is the answer.

        # The math.lcm() usage was picked up from other contestants, I did not
        # come up with that myself. And I don't fully understand it.

        for n, node in enumerate(currents):
            if node.endswith("Z") and not steps[n]:
                steps[n] = stepcount
                if all(steps):
                    return math.lcm(*steps)

        # take one step for each node, update currents
        currents = [step(instruction, nodes, current) for current in currents]

        # In my original attempt, I was iterating endlessly waiting for all
        # nodes to end with "Z" at the same time.
        # if all([node.endswith("Z") for node in currents]):
        #    return stepcount


def parse_data(fin):
    with open(fin, "r", encoding="utf-8") as file:
        raw = file.readlines()
    instructions = raw[0].strip()

    nodes = {}
    for line in raw[2:]:
        node, in_l, in_r = re.findall(r"\w{3}", line)
        nodes[node] = (in_l, in_r)

    return instructions, nodes


if __name__ == "__main__":
    test_part1()
    solution_part1()
    test_part2()
    solution_part2()

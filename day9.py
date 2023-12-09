"""Advent of Code - Day 9"""


def test_part1():
    histories = parse_data("data\day9_testdata.txt")
    assert solve(histories) == 114


def solution_part1():
    histories = parse_data("data\day9_data.txt")
    result = solve(histories)
    print(f"Part 1: {result}")


def test_part2():
    histories = parse_data("data\day9_testdata.txt")
    assert solve(histories, backwards=True) == 2


def solution_part2():
    histories = parse_data("data\day9_data.txt")
    result = solve(histories, backwards=True)
    print(f"Part 2: {result}")


def solve(histories, backwards=False):
    return sum([extrapolate(history, backwards) for history in histories])


def extrapolate(history, backwards=False):
    iteration = history
    iterations = [iteration]
    while any(iteration):
        iteration = [y - x for x, y in zip(iteration, iteration[1:])]
        iterations.append(iteration)

    # Each iteration is a list of diffs from line above. Now go backwards
    # through the iterations, fill in the first or last value starting with 0
    # in the last list of 0's.

    for i, iteration in enumerate(iterations[::-1]):
        if backwards:
            extrapolation = 0 if i == 0 else iteration[0] - extrapolation
            iteration.insert(0, extrapolation)
        else:
            extrapolation = 0 if i == 0 else iteration[-1] + extrapolation
            iteration.append(extrapolation)

    return extrapolation


def parse_data(fin):
    with open(fin, "r", encoding="utf-8") as file:
        data = [[int(x) for x in line.split()] for line in file.readlines()]
    return data


if __name__ == "__main__":
    test_part1()
    solution_part1()
    test_part2()
    solution_part2()

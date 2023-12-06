"""Advent of Code 2023 - day 6"""


def test_part1():
    times, distances = parse_data("data\day6_testdata.txt")

    mult = 1
    for time, record in zip(times, distances):
        # distance is current record
        ways_to_win = calc_ways_to_win(time, record)
        mult = mult * len(ways_to_win)

    assert mult == 288


def solution_part1():
    times, distances = parse_data("data\day6_data.txt")

    mult = 1
    for time, record in zip(times, distances):
        # distance is current record
        ways_to_win = calc_ways_to_win(time, record)
        mult = mult * len(ways_to_win)

    print(f"Part 1: {mult}")


def test_part2():
    time, distance = parse_data("data\day6_testdata.txt", remove_spaces=True)
    ways_to_win = calc_ways_to_win(time, distance)
    assert len(ways_to_win) == 71503, len(ways_to_win)


def solution_part2():
    time, distance = parse_data("data\day6_data.txt", remove_spaces=True)
    ways_to_win = calc_ways_to_win(time, distance)
    print(f"Part 2: {len(ways_to_win)}")


def calc_ways_to_win(time, record, v0=0):
    v0 = 0
    ways_to_win = []
    for H in range(0, time + 1):
        V = v0 + H
        D = V * (time - H)
        if D > record:
            ways_to_win.append(H)
    return ways_to_win


def parse_data(fin, remove_spaces=False):
    with open(fin, "r", encoding="utf-8") as file:
        data = file.readlines()

    times = [int(t) for t in data[0].split(":")[-1].split()]
    distances = [int(d) for d in data[1].split(":")[-1].split()]

    if remove_spaces:
        times = int("".join([str(t) for t in times]))
        distances = int("".join([str(d) for d in distances]))

    return times, distances


if __name__ == "__main__":
    test_part1()
    solution_part1()
    test_part2()
    solution_part2()

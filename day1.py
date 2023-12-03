"""Advent of Code 2023 - day 1"""


def test_part1():
    data = read("data/day1-1_testdata.txt")
    result = sum([first_last_digit_or_word(line) for line in data])
    assert result == 142, result

    # confirmed result part 1-1
    data = read("data/day1_data.txt")
    result = sum([first_last_digit(line) for line in data])
    assert result == 55172, result


def solution_part1():
    data = read("data/day1_data.txt")
    result = sum([first_last_digit(line) for line in data])
    print(f"Part 1: {result}")


def test_part2():
    data = read("data/day1-2_testdata.txt")
    result = sum([first_last_digit_or_word(line) for line in data])
    assert result == 281, result


def solution_part2():
    data = read("data/day1_data.txt")
    result = sum([first_last_digit_or_word(line) for line in data])
    print(f"Part 2: {result}")


def first_last_digit(line):
    """From line of txt combine first and last valid digit."""

    first = None
    for value in line:
        if value.isnumeric():
            first = value
            break

    last = None
    for value in line[::-1]:
        if value.isnumeric():
            last = value
            break

    result = int("".join([first, last]))
    return result


def first_last_digit_or_word(line):
    """From line of txt combine first and last valid digit including words."""

    numberwords = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    first = None
    myline = line
    while first is None:
        if myline[0].isnumeric():
            first = myline[0]
        for numberword, numbervalue in numberwords.items():
            if myline.startswith(numberword):
                first = numbervalue
                break
        myline = myline[1:]

    last = None
    myline = line
    while last is None:
        if myline[-1].isnumeric():
            last = myline[-1]
        for numberword, numbervalue in numberwords.items():
            if myline.endswith(numberword):
                last = numbervalue
                break
        myline = myline[:-1]

    result = int(f"{first}{last}")
    return result


def read(fin):
    """Read from file."""
    with open(fin, "r", encoding="utf-8") as file:
        data = file.readlines()

    data = [d.strip() for d in data]
    return data


if __name__ == "__main__":
    test_part1()
    test_part2()
    solution_part1()
    solution_part2()

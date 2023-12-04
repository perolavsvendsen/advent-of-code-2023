"""Advent of Code - day 3"""


def test_part1():
    data = parse_data("data/day3_testdata.txt")

    matrix = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
    ]

    result = find_adjacent_cells(matrix, (0, 0))
    assert sorted(result) == sorted([(1, 0), (0, 1), (1, 1)]), result

    sums = sum_of_partnr(data)
    assert sums == 4361, sums


def solution_part1():
    data = parse_data("data/day3_data.txt")
    sums = sum_of_partnr(data)
    print(f"Part 1: {sums}")


def test_part2():
    data = parse_data("data/day3_testdata.txt")
    gear_ratios = find_gear_ratios(data)
    assert sum(gear_ratios) == 467835, sum(gear_ratios)


def solution_part2():
    data = parse_data("data/day3_data.txt")
    gear_ratios = find_gear_ratios(data)
    print(f"Part 2: {sum(gear_ratios)}")


def find_gear_ratios(data):
    numbers = find_numbers(data)
    numbers_matrix = [["" for x in data[0]] for y in data]

    number_ids = {}
    nid = 0
    for number, coords in numbers:
        number_ids[nid] = number
        for x, y in coords:
            numbers_matrix[y][x] = nid
        nid += 1

    # for line in numbers_matrix:
    #     print(line)

    gears_matrix = [["" for x in data[0]] for y in data]

    gear_ratios = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "*":
                # found a potential gear, now check if adjacent to any numbers
                adjacent_numbers = []
                for gx, gy in find_adjacent_cells(gears_matrix, (x, y)):
                    if isinstance(numbers_matrix[gy][gx], int):
                        adjacent_numbers.append(numbers_matrix[gy][gx])
                if len(set(adjacent_numbers)) == 2:
                    parts = [number_ids[n] for n in set(adjacent_numbers)]
                    gear_ratio = 1
                    for part in parts:
                        gear_ratio = gear_ratio * part
                    # print(f"Found a gear in {x, y} with part numbers {parts}")
                    # print(f"Gear ratio is {gear_ratio}")
                    gear_ratios.append(gear_ratio)

    return gear_ratios


def sum_of_partnr(data):
    """Find partnumbers, return sum."""

    # find symbols and create adjacents matrix
    visited = []
    adjacents = [["" for x in data[0]] for y in data]
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (x, y) in visited:
                continue
            visited.append((x, y))

            if not is_symbol(char):
                continue

            # found symbol, now print symbol in all adjacent cells
            adjacents[y][x] = char
            for ax, ay in find_adjacent_cells(adjacents, (x, y)):
                adjacents[ay][ax] += char

    # find numbers and check if they are adjacent to symbol

    numbers = find_numbers(data)

    # for each number, if any coordinate is adjacent to symbol, keep
    engine_parts = []
    for number, coords in numbers:
        for x, y in coords:
            if is_symbol(adjacents[y][x]):
                # this number is adjacent to a symbol
                engine_parts.append(number)
                break

    return sum(engine_parts)


def find_adjacent_cells(matrix, coord):
    """Return list of coords for adjacent cells to coord in matrix."""

    adjacents = []

    xmax = len(matrix[0])
    ymax = len(matrix)

    x, y = coord

    if x <= xmax:
        adjacents.append((x + 1, y))
    if x > 0:
        adjacents.append((x - 1, y))
    if y <= ymax:
        adjacents.append((x, y + 1))
    if y > 0:
        adjacents.append((x, y - 1))
    if y > 0 and x > 0:
        adjacents.append((x - 1, y - 1))
    if y <= ymax and x > 0:
        adjacents.append((x + 1, y - 1))
    if y > 0 and x <= xmax:
        adjacents.append((x - 1, y + 1))
    if y <= ymax and x <= xmax:
        adjacents.append((x + 1, y + 1))

    return adjacents


def find_numbers(data):
    visited = []
    numbers = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (x, y) in visited:
                continue
            else:
                visited.append((x, y))
            if char.isnumeric():
                # found number, now follow it towards right until next .
                subx = x
                digits = []
                coords = []
                while True:
                    subchar = data[y][subx]
                    if not subchar.isnumeric():
                        break
                    visited.append((subx, y))
                    digits.append(subchar)
                    coords.append((subx, y))
                    subx += 1
                    if subx >= len(line):  # reached end of line
                        break
                number = int("".join(digits))
                numbers.append((number, coords))

    return numbers


def is_symbol(char):
    if char.isnumeric():
        return False
    if char == ".":
        return False
    if char == "":
        return False
    return True


def parse_data(fin):
    with open(fin, "r", encoding="utf-8") as file:
        data = file.readlines()

    data = [line.strip() for line in data]

    return data


if __name__ == "__main__":
    test_part1()
    solution_part1()
    test_part2()
    solution_part2()

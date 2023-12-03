"""Advent of Code 2023 - day 2"""


def test_part1():
    games = parse_data("data\day2_testdata.txt")
    bag = {"red": 12, "green": 13, "blue": 14}

    assert find_possibles(games, bag) == [1, 2, 5]

    # confirmed solution part 1
    games = parse_data("data\day2_data.txt")
    bag = {"red": 12, "green": 13, "blue": 14}
    assert sum(find_possibles(games, bag)) == 2085


def solution_part1():
    games = parse_data("data\day2_data.txt")
    bag = {"red": 12, "green": 13, "blue": 14}
    print(f"Part 1: {sum(find_possibles(games, bag))}")


def test_part2():
    games = parse_data("data\day2_testdata.txt")
    assert find_game_minimums_power(games[1]) == 48
    assert find_game_minimums_power(games[2]) == 12
    assert find_game_minimums_power(games[3]) == 1560
    assert find_game_minimums_power(games[4]) == 630
    assert find_game_minimums_power(games[5]) == 36

    sums = sum(find_minimums_power(games))
    assert sums == 2286, sums


def solution_part2():
    games = parse_data("data\day2_data.txt")
    print(f"Part 2: {sum(find_minimums_power(games))}")


def find_minimums_power(games):
    """Find and multiply minimums across many games."""
    return [find_game_minimums_power(games[gameid]) for gameid in games]


def find_game_minimums_power(game):
    """Find the power of the minimum per color needed for the game."""

    mult = 1
    for color in game:
        mult = mult * max(game[color])
    return mult


def find_possibles(games, bag):
    possibles = []
    for game_id, game in games.items():
        if is_possible(game, bag):
            possibles.append(game_id)
    return possibles


def is_possible(samples, bag):
    for color, bagvalue in bag.items():
        if bagvalue < max(samples[color]):
            return False
    return True


def parse_data(fin):
    """Read data from file."""
    with open(fin, "r", encoding="utf-8") as file:
        raw = file.readlines()

    raw = [line.strip() for line in raw]

    games = {}
    for line in raw:
        game_id = get_game_id(line)
        games[game_id] = {}
        game = games[game_id]

        draws = [draw.strip() for draw in line.split(":")[-1].split(";")]
        for draw in draws:
            samples = [sample.strip() for sample in draw.split(",")]
            for sample in samples:
                count = int(sample.split(" ")[0].strip())
                color = sample.split(" ")[-1].strip()

                if color in game:
                    game[color].append(count)
                else:
                    game[color] = [count]
    return games


def get_game_id(line):
    """Get game ID from line."""
    return int(line.split(":")[0].replace("Game ", ""))


if __name__ == "__main__":
    test_part1()
    solution_part1()
    test_part2()
    solution_part2()

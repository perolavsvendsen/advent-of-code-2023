"""Advent of Code - day 4"""


def test_part1():
    data = parse_data("data\day4_testdata.txt")
    score = calculate_score(data)
    assert score == 13

    # confirmed solution
    data = parse_data("data\day4_data.txt")
    score = calculate_score(data)
    assert score == 23028, score


def solution_part1():
    data = parse_data("data\day4_data.txt")
    score = calculate_score(data)
    print(f"Part 1: {score}")


def test_part2():
    data = parse_data("data\day4_testdata.txt")
    cardcount = count_scratchcards(data)
    assert cardcount == 30, cardcount


def solution_part2():
    data = parse_data("data\day4_data.txt")
    cardcount = count_scratchcards(data)
    print(f"Part 2: {cardcount}")


def count_scratchcards(data):
    for cardid in data:
        data[cardid]["instances"] = 1

    for cardid, line in data.items():
        matches = len(set(line["mine"]) & set(line["winners"]))
        instances = line["instances"]

        if matches == 0:
            continue

        for c in range(cardid + 1, cardid + 1 + matches):
            data[c]["instances"] += instances

    return sum(line["instances"] for cardid, line in data.items())


def calculate_score(data):
    scores = []
    for cardid, line in data.items():
        inboth = set(line["mine"]) & set(line["winners"])
        if len(inboth) == 0:
            score = 0
        else:
            score = 1 * 2 ** (len(inboth) - 1)
        scores.append(score)

    return sum(scores)


def parse_data(fin):
    with open(fin, "r", encoding="utf-8") as file:
        raw = file.readlines()

    data = {}
    for line in raw:
        cardid, linedata = parse_line(line)
        data[cardid] = linedata

    return data


def parse_line(line):
    cardid = int(line.split(":")[0].split()[-1].strip())
    winners = [int(w) for w in line.split(":")[-1].split("|")[0].strip().split()]
    mine = [int(m) for m in line.split(":")[-1].split("|")[-1].strip().split()]

    return cardid, {"winners": winners, "mine": mine}


if __name__ == "__main__":
    test_part1()
    solution_part1()
    test_part2()
    solution_part2()

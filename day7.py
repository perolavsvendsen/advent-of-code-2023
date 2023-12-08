"""Advent of Code - day 7"""

from collections import Counter
import pandas as pd


def test_part1():
    hands = [
        ("AAAAA", 7000),
        ("33332", 6000),
        ("2AAAA", 6000),
        ("77888", 5000),
        ("77788", 5000),
        ("T55J5", 4000),
        ("QQQJA", 4000),
        ("KK677", 3000),
        ("KTJJT", 3000),
        ("AA123", 2000),
        ("32T3K", 2000),
        ("12345", 1000),
    ]
    for hand, value in hands:
        assert categorize_hand(hand) == value, categorize_hand(hand)

    handbids = parse_data("data/day7_testdata.txt")

    assert solve(handbids, J=11) == 6440


def solution_part1():
    handbids = parse_data("data/day7_data.txt")
    print(f"Part 1: {solve(handbids, J=11)}")


def test_part2():
    assert evaluate_hand("JJJJJ", J=1)[0] == 7000
    assert evaluate_hand("JJJJK", J=1)[0] == 7000, evaluate_hand("JJJJK", J=1)[0]
    assert evaluate_hand("JJJKK", J=1)[0] == 7000, evaluate_hand("JJJKK", J=1)[0]
    assert evaluate_hand("JJKKK", J=1)[0] == 7000, evaluate_hand("JJKKK", J=1)[0]

    handbids = parse_data("data/day7_testdata.txt")
    assert solve(handbids, J=1) == 5905

    result = make_result(handbids, J=1)
    df = make_df(result)
    assert list(df["hand"]) == ["32T3K", "KK677", "T55J5", "QQQJA", "KTJJT"]


def solution_part2():
    handbids = parse_data("data/day7_data.txt")
    result = solve(handbids, J=1)
    assert result < 250437590, result
    assert result != 250493819, result
    print(f"Part 2: {result}")


def solve(handbids, J):
    result = make_result(handbids, J)
    df = make_df(result)
    return sum(df["score"])


def make_result(handbids, J):
    result = {
        "hand": [],
        "bid": [],
        "type": [],
        "one": [],
        "two": [],
        "three": [],
        "four": [],
        "five": [],
    }

    for hand, bid in handbids:
        type_, one, two, three, four, five = evaluate_hand(hand, J)

        result["hand"].append(hand)
        result["bid"].append(bid)
        result["type"].append(type_)
        result["one"].append(one)
        result["two"].append(two)
        result["three"].append(three)
        result["four"].append(four)
        result["five"].append(five)

    return result


def make_df(result):
    df = pd.DataFrame(result)

    df = df.sort_values(
        by=["type", "one", "two", "three", "four", "five"], ascending=True
    )
    df["rank"] = range(1, len(df) + 1)
    df["score"] = df["rank"] * df["bid"]

    return df


def evaluate_hand(hand, J):
    if J == 11 or ("J" not in hand):
        result = [categorize_hand(hand)]
    elif Counter(hand)["J"] == 4:
        result = [7000]
    else:
        tmpresults = []
        tmphand = []
        for char in "23456789TQKA":
            for p, _ in enumerate(hand):
                if hand.find("J", p) == -1:
                    break
                rhand = hand.replace("J", char, p + 1)
                tmpresults.append(categorize_hand(rhand))
                tmphand.append(rhand)
        result = [max(tmpresults)]

    label_values = {"T": 10, "J": J, "Q": 12, "K": 13, "A": 14}

    for char in hand:
        if char in label_values:
            result.append(label_values[char])
        else:
            result.append(int(char))

    return tuple(result)


def categorize_hand(hand):
    if len(hand) != 5:
        raise ValueError(f"Expected 5 cards in hand. {hand=}")
    if len(set(hand)) == 1:
        return 7000  # five of kind
    elif 4 in sorted(Counter(hand).values()):
        return 6000  # four of kind
    elif sorted(Counter(hand).values()) == [2, 3]:
        return 5000  # full house
    elif 3 in sorted(Counter(hand).values()):
        return 4000  # three of kind
    elif sorted(Counter(hand).values()) == [1, 2, 2]:
        return 3000  # two pairs
    elif sorted(Counter(hand).values()) == [1, 1, 1, 2]:
        return 2000  # one pair
    else:
        return 1000  # high card


def parse_data(fin):
    with open(fin, "r", encoding="utf-8") as file:
        data = file.readlines()

    hands = []
    for line in data:
        hand, bid = line.strip().split()
        hands.append((hand, int(bid)))

    return hands


if __name__ == "__main__":
    test_part1()
    solution_part1()
    test_part2()
    solution_part2()

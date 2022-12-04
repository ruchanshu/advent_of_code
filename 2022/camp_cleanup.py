from aoc import AoCData


def get_range(data):
    start, end = data.split("-")
    return range(int(start), int(end) + 1)


def fully_contains(pairs):
    pair_1 = get_range(pairs[0])
    pair_2 = get_range(pairs[1])
    if len(pair_1) > len(pair_2):
        return pair_2.start in pair_1 and pair_2[-1] in pair_1
    else:
        return pair_1.start in pair_2 and pair_1[-1] in pair_2


def any_overlap(pairs):
    pair_1 = get_range(pairs[0])
    pair_2 = get_range(pairs[1])
    if len(pair_1) > len(pair_2):
        return pair_2.start in pair_1 or pair_2[-1] in pair_1
    else:
        return pair_1.start in pair_2 or pair_1[-1] in pair_2


if __name__ == "__main__":
    aoc = AoCData()
    full_overlap_count = 0
    any_overlap_count = 0
    for line in aoc.get_input_lines():
        pairs = line.split(",")
        if fully_contains(pairs):
            full_overlap_count += 1
        if any_overlap(pairs):
            any_overlap_count += 1

    print(f"Par One: {full_overlap_count}")
    print(f"Par Two: {any_overlap_count}")

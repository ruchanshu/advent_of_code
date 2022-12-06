import os


def rucksacks_size(items):
    return len(items)


def compartment_size(items):
    return int(len(items) / 2)


def get_common_item(items):
    size = compartment_size(items)
    first_compartment = line[:size]
    second_compartment = line[size:]
    return list(set(first_compartment).intersection(second_compartment))


def get_badge_item(group):
    return list(set.intersection(*map(set, group)))


def get_item_priority(item):
    if 65 <= ord(item) <= 90:
        return ord(item) - 38
    if 67 <= ord(item) <= 122:
        return ord(item) - 96


if __name__ == "__main__":
    item_priorities = 0
    badge_priorities = 0
    rucksacks_group = []
    count = 0
    input_data = os.path.join("data/day_3", "input_3.txt")
    with open(input_data, "r") as file:
        for raw_line in file.readlines():
            line = raw_line.strip("\n")
            rucksacks_group.append(line)
            common_item = get_common_item(line)[0]
            item_priorities += get_item_priority(common_item)
            count += 1
            if count % 3 == 0:
                badge_item = get_badge_item(rucksacks_group)[0]
                badge_priorities += get_item_priority(badge_item)
                rucksacks_group = []
        print(f"The sum of the priorities of common item types is {item_priorities}")
        print(f"The sum of the priorities of badges is {badge_priorities}")

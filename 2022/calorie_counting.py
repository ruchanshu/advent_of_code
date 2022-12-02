import os

from functools import cached_property


class Elf:
    def __repr__(self):
        return f"Elf: {self.name}"

    def __init__(self, name, foods, total_calories):
        self.name = name
        self.foods = foods
        self.total_calories = total_calories


class ElvesDetails:
    def __init__(self, all_elves):
        self.all_elves = all_elves

    @cached_property
    def sort_by_calories(self):
        return sorted(self.all_elves, key=lambda x: x.total_calories)

    def get_top_n(self, n):
        return self.sort_by_calories[n:]


if __name__ == "__main__":
    elves_details = []
    day_1_data = os.path.join("day_1", "input_1.txt")
    with open(day_1_data) as data:
        elf_count = 0
        elf_foods = []
        elf_calories = 0

        for line in data.readlines():
            if line == "\n":
                elf_count += 1
                elves_details.append(Elf(f"elf_{elf_count}", elf_foods, elf_calories))
                elf_foods = []
                elf_calories = 0
            else:
                calorie = int(line.strip("\n"))
                elf_foods.append(calorie)
                elf_calories += calorie

    elves = ElvesDetails(elves_details)
    elf_with_max_calories = elves.get_top_n(-1)[0]
    print(
        f"Part One: {elf_with_max_calories.name} is carrying the most {elf_with_max_calories.total_calories} Calories."
    )

    top_3_max_calories = 0
    for elf in elves.get_top_n(-3):
        top_3_max_calories += elf.total_calories
    print(f"Part Two: Top three Elves are carrying {top_3_max_calories} calories.")

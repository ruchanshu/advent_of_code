from aoc import AoCData
from constants import URL

# stack_1 = ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S']
# stack_2 = ['T', 'B', 'M', 'Z', 'R']
# stack_3 = ['Z', 'L', 'C', 'H', 'N', 'S']
# stack_4 = ['S', 'C', 'F', 'J']
# stack_5 = ['P', 'G', 'H', 'W', 'R', 'Z', 'B']
# stack_6 = ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T']
# stack_7 = ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q']
# stack_8 = ['M', 'Z', 'R']
# stack_9 = ['M', 'C', 'L', 'G', 'V', 'R', 'T']

stack_1 = ["H", "T", "Z", "D"]
stack_2 = ["Q", "R", "W", "T", "G", "C", "S"]
stack_3 = ["P", "B", "F", "Q", "N", "R", "C", "H"]
stack_4 = ["L", "C", "N", "F", "H", "Z"]
stack_5 = ["G", "L", "F", "Q", "S"]
stack_6 = ["V", "P", "W", "Z", "B", "R", "C", "S"]
stack_7 = ["Z", "F", "J"]
stack_8 = ["D", "L", "V", "Z", "R", "H", "Q"]
stack_9 = ["B", "H", "G", "N", "F", "Z", "L", "D"]

if __name__ == "__main__":
    aoc = AoCData()
    count = 0
    for line in aoc.get_input_lines(f"{URL}2022/day/5/input"):
        if "move" in line:
            words = line.split(" ")
            size, from_, to_ = int(words[1]), int(words[3]), int(words[5])
            from_stack = eval(f"stack_{from_}")
            to_stack = eval(f"stack_{to_}")
            to_stack.extend(from_stack[-size:])
            del from_stack[-size:]
            # for i in range(size):
            #     _ = from_stack.pop()
            #     to_stack.append(_)

    for i in range(1, 10):
        print(eval(f"stack_{i}")[-1], end="")

from aoc import AoCData

if __name__ == "__main__":
    aoc = AoCData()
    start_of_packet = 0
    start_1 = 0
    end_1 = 4

    start_of_message = 0
    start_2 = 0
    end_2 = 14
    for line in aoc.get_input_lines():
        while end_1 < len(line):
            if len(set(line[start_1:end_1])) == 4:
                start_of_packet += end_1
                break
            start_1 += 1
            end_1 += 1

        while end_2 < len(line):
            if len(set(line[start_2:end_2])) == 14:
                start_of_message += end_2
                break
            start_2 += 1
            end_2 += 1

    print(f"Par One: {start_of_packet}")
    print(f"Par Two: {start_of_message}")

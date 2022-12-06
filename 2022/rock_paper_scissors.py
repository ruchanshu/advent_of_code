import os
import csv

from constants import ROCK, PAPER, SCISSORS, WON, DRAW, LOST, SHAPE_SCORE, OUTCOME_SCORE

rock = ("A", "X")
paper = ("B", "Y")
scissors = ("C", "Z")


def get_move(move):
    if move in rock:
        return ROCK
    if move in paper:
        return PAPER
    if move in scissors:
        return SCISSORS


def get_result_without_strategy(you, opponent):
    if you == opponent:
        return DRAW
    if you == ROCK and opponent == PAPER:
        return LOST
    if you == ROCK and opponent == SCISSORS:
        return WON
    if you == PAPER and opponent == SCISSORS:
        return LOST
    if you == PAPER and opponent == ROCK:
        return WON
    if you == SCISSORS and opponent == ROCK:
        return LOST
    if you == SCISSORS and opponent == PAPER:
        return WON


def get_move_with_strategy(opponent, outcome):
    if outcome == DRAW:
        return opponent
    if outcome == WON and opponent == ROCK:
        return PAPER
    if outcome == WON and opponent == PAPER:
        return SCISSORS
    if outcome == WON and opponent == SCISSORS:
        return ROCK
    if outcome == LOST and opponent == ROCK:
        return SCISSORS
    if outcome == LOST and opponent == PAPER:
        return ROCK
    if outcome == LOST and opponent == SCISSORS:
        return PAPER


def get_result_with_strategy(outcome):
    if outcome == rock[1]:
        return LOST
    if outcome in paper[1]:
        return DRAW
    if outcome in scissors[1]:
        return WON


def get_player_score(move, outcome):
    return SHAPE_SCORE[move] + OUTCOME_SCORE[outcome]


def play_without_strategy(player, opponent):
    opponent_move = get_move(opponent)
    your_move = get_move(player)
    result = get_result_without_strategy(your_move, opponent_move)
    return get_player_score(your_move, result)


def play_with_strategy(outcome, opponent):
    result = get_result_with_strategy(outcome)
    opponent_move = get_move(opponent)
    move = get_move_with_strategy(opponent_move, result)
    return get_player_score(move, result)


if __name__ == "__main__":
    count = 0
    total_score = 0
    strategic_total_score = 0
    input_data = os.path.join("data/day_2", "input_2.csv")
    with open(input_data) as file:
        reader = csv.reader(file)
        for row in reader:
            total_score += play_without_strategy(row[0][2], row[0][0])
            strategic_total_score += play_with_strategy(row[0][2], row[0][0])

    print(f"Part One: Total score will be {total_score}.")
    print(
        f"Part Two: Total score will be {strategic_total_score} "
        f"if everything goes exactly according to your strategy guide"
    )

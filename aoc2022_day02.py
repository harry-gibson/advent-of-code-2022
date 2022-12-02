from enum import Enum

from aocd import data


# Part 1

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def map_value(char):
    if char in ('A', 'X'): return RPS.ROCK
    if char in ('B', 'Y'): return RPS.PAPER
    if char in ('C', 'Z'): return RPS.SCISSORS
    raise ValueError(char)

def get_winner_p1(a:RPS, b:RPS):
    pair = set((a, b))
    if pair == {RPS.ROCK, RPS.PAPER}: return RPS.PAPER
    if pair == {RPS.ROCK, RPS.SCISSORS}: return RPS.ROCK
    if pair == {RPS.SCISSORS, RPS.PAPER}: return RPS.SCISSORS
    return None


# Part 2

class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0

outcomes = {
    'X': Outcome.LOSE,
    'Y': Outcome.DRAW,
    'Z': Outcome.WIN 
}

_req_plays = {
        (RPS.ROCK, Outcome.WIN): RPS.PAPER,
        (RPS.ROCK, Outcome.LOSE): RPS.SCISSORS,
        (RPS.PAPER, Outcome.WIN): RPS.SCISSORS,
        (RPS.PAPER, Outcome.LOSE): RPS.ROCK,
        (RPS.SCISSORS, Outcome.WIN): RPS.ROCK,
        (RPS.SCISSORS, Outcome.LOSE): RPS.PAPER
}

def get_required_play(a:RPS, b:Outcome):
    if b == Outcome.DRAW: return a
    return _req_plays[(a, b)]
    

if __name__ == "__main__":
    score_p1 = 0
    for round in data.split('\n'):
        them, us_p1 = [map_value(v) for v in round.split()]
        winner = get_winner_p1(them, us_p1)
        score_p1 += us_p1.value
        result = Outcome.WIN if winner == us_p1 else Outcome.DRAW if winner is None else Outcome.LOSE
        score_p1 += result.value
    print(score_p1)

    score_p2 = 0
    for round in data.split('\n'):
        them_item, us_item = round.split()
        them = map_value(them_item)
        outcome = outcomes[us_item]
        score_p2 += outcome.value
        score_p2 += get_required_play(them, outcome).value
    print(score_p2)

import random

p1_games = 0
p1_sets = 0
p2_games = 0
p2_sets = 0
  


def play_game():
    p1 = 0
    p2 = 0
    global p1_games
    global p2_games

    while True:
        # player 1 wins 55% of poins
        if random.random() <= 0.55:
            p1 += 1
        else:
            p2 += 1
        
        if p1 >= 4 and p1 - p2 > 1:
            p1_games += 1
            return 1
        if p2 >= 4 and p2 - p1 > 1:
            p2_games += 1
            return 2
    
def play_set():
    p1 = 0
    p2 = 0
    global p1_sets
    global p2_sets

    while True:
        if play_game() == 1:
            p1 += 1
        else:
            p2 += 1
    
        if p1 == 6 and p2 < 5 or p1 == 7:
            p1_sets += 1
            return 1
        if p2 == 6 and p1 < 5 or p2 == 7:
            p2_sets += 1
            return 2
        
def play_match():
    p1 = 0
    p2 = 0

    while True:
        if play_set() == 1:
            p1 += 1
        else:
            p2 += 1
        
        if p1 == 2:
            return 1
        if p2 == 2:
            return 2
        
def play_games(n_matches: int):
    p1 = 0
    p2 = 0
    global p1_games
    global p1_sets
    global p2_games
    global p2_sets

    for i in range(n_matches):
        if play_match() == 1:
            p1 += 1
        else:
            p2 += 1
    print(f"p1 games:   {100 * p1_games / (p1_games + p2_games):.2f}%")
    print(f"p1 sets:    {100 * p1_sets / (p1_sets + p2_sets):.2f}%")
    print(f"p1 matches: {100 * p1 / n_matches:.2f}% ({p1}/{n_matches} matches)")

play_games(10000)
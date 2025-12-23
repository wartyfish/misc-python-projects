import re
import random
from pathlib import Path

# extract state-capital pairs from states.csv
pattern = re.compile(r"^(.+?)\s\t(.+?)\s\t")
states = {}
with open("states.csv", "r", encoding="utf-8") as f:
    for line in f:
        if match := pattern.search(line.strip()):
            states[match.group(1)] = match.group(2)

# generate questions in the form of state (key): 4x capitals (values)
questions = {}
answers = {}
s = 42
i = 0
for state in states:
    random.seed(i)                          # seed keeps pseudo-random sequences consistant 
    r = list(range(0, 50))                  # generate indices of 50 states 
    r.pop(i)                                # remove currently selected state
    answer_indices = random.sample(r, 3)    # generate then ranomise list of 4 indices
    answer_indices.append(i)                # including one that correspondes to selected state
    random.shuffle(answer_indices)          

    questions[state] = []
    answers[state] = (answer_indices.index(i), states[state])
    for j in answer_indices:
        questions[state].append(list(states.values())[j])
        
    i += 1
    s += 1

# generate 35 unique quizzes
abcd = "ABCD"

for i in range(35):
    # generate paths for Q and A sheets
    p_q = Path("questions") / f"questions_{i+1:02d}.txt"
    p_a = Path("answers") / f"answer_key_{i+1:02d}.txt"

    r_50 = random.shuffle(list(range(50)))
    
    

    with open(p_a, "w", encoding="utf-8") as f:
        
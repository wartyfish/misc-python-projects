"""
Random Quiz Generator.

Generates 35x randomised multiple-choice quizes and corresponding answer keys.
Each question is one of the US states and the choices contain the capital city and 3 other randomly-selected state capitals.
All of the quizzes contain the same 50 questions, but in a randomised order. 
Quizzes and answer keys are each saved to their own .txt files.
"""

import re
import random
from pathlib import Path
import os

os.chdir(Path(os.getcwd()) 
        / "misc-python-scripts" 
        / "2025" 
        / "Automate the Boring Stuff" 
        / "Chapter 10 Reading and Writing Files" 
        / "random quiz files")

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
    random.seed(s)                          # seed keeps pseudo-random sequences consistant 
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
abcd = "abcd"

for i in range(35):
    random.seed(s)
    # generate paths for Q and A sheets
    p_q = Path("questions") / f"questions_{i+1:02d}.txt"
    p_a = Path("answers") / f"answer_key_{i+1:02d}.txt"

    r_50 = list(range(50))
    random.shuffle(r_50)

    # writing Q files
    question_number = 1
    with open(p_q, "w", encoding="utf-8") as f:
        for n in r_50:
            state = list(questions.keys())[n] 
            
            f.write(f"{question_number}. {state}:\n")
            for m in range(4):
                f.write(f"{abcd[m]}. {questions[state][m]}\n")
            f.write("\n")
            question_number += 1
    # writing A files
    question_number = 1
    with open(p_a, "w", encoding="utf-8") as f:
        for n in r_50:
            state = list(questions.keys())[n]
            ABCD_answer, answer = answers[state]
            ABCD_answer = abcd[ABCD_answer]
            f.write(f"{question_number}. {state}: {ABCD_answer}. {answer}\n")
            question_number += 1

    s += 1

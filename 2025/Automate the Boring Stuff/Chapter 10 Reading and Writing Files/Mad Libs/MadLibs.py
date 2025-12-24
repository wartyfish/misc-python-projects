"""
Mad Libs text replacer.

Reads a text file containing placeholders (ADJECTIVE, ADVERB, NOUN, VERB),
prompts the user to replace each placeholder, and writes the completed
story to a new output file.
"""

import os
import re
from pathlib import Path

os.chdir(Path(os.getcwd()) 
        / "misc-python-scripts" 
        / "2025" 
        / "Automate the Boring Stuff" 
        / "Chapter 10 Reading and Writing Files" 
        / "Mad Libs")

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

pattern = r"\b(ADJECTIVE|ADVERB|NOUN|VERB)\b"

def replace_word(match):
    w = match.group(1)
    if w == "ADJECTIVE" or w == "ADVERB":
        n = "n"
    else:
        n = ""
    substitution = input(f"Enter a{n} {w.lower()}:\n")
    return substitution

result = re.sub(pattern, replace_word, text)

with open("output.txt", "w") as f:
    f.write(result)
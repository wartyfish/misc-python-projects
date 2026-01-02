#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    result = []
    pattern = re.compile(r"^(\d{1,3})\s*(\d{1,3})\s*(\d{1,3})\s*([\w\s]*)")
    with open(filename, "r") as f:
        for line in f:
            match = re.search(pattern, line.strip())
            if match:
                result.append(f"{int(match.group(1)):03d}\t{int(match.group(2)):03d}\t{int(match.group(3)):03d}\t{match.group(4)}")
    return result

def main():
    for colour in red_green_blue("rgb.txt"):
        print(colour)

if __name__ == "__main__":
    main()
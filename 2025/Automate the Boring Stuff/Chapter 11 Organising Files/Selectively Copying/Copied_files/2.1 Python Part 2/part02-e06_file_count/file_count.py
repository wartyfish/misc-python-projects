#!/usr/bin/env python3

import sys

def file_count(filename):
    lines = words = characters = 0
    with open(filename) as f:
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len([char for char in line])
    return lines, words, characters


def main():
    for file in sys.argv[1:]:
        lines, words, characters = file_count(file)
        print("{}\t{}\t{}\t{}".format(lines, words, characters, file))

if __name__ == "__main__":
    main()

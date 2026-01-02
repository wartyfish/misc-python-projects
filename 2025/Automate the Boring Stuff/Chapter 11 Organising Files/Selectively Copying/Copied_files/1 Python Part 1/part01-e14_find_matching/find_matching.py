#!/usr/bin/env python3

def find_matching(L, pattern):
    result = [n for n, word in enumerate(L) if pattern in word]

    return result

def main():
    l = ["sensitive", "engine", "rubbish", "comment"]
    p = "en"

    print(find_matching(l, p))
if __name__ == "__main__":
    main()

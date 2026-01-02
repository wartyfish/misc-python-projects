#!/usr/bin/env python3

def interleave(*lists):
    result = []
    for list in zip(*lists):
        result.extend(list)
    return result

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c'], ['p', 'o', 'o']))

if __name__ == "__main__":
    main()

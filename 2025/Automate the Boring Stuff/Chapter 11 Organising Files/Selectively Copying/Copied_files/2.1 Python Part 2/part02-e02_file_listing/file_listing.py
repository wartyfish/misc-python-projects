#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    pattern = re.compile(r"jttoivon hyad-all\s*(\d+)\s*([a-z]{3})\s*(\d+)\s(\d\d):(\d\d)\s*([\w.]+)", re.IGNORECASE)
    with open(filename, "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                size = int(match.group(1))
                month = match.group(2)
                day = int(match.group(3))
                hour = int(match.group(4))
                min = int(match.group(5))
                name = match.group(6)

                result.append((size, month, day, hour, min, name))
    return result

def main():
    for line in file_listing("listing.txt"):
        print(line)

if __name__ == "__main__":
    main()

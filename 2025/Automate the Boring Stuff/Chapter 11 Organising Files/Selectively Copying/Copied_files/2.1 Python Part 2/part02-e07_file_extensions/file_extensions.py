#!/usr/bin/env python3

import re

def file_extensions(filename):
    with_extension = {}
    without_extension = []
    pattern = re.compile(r"\.([a-z]+)$", re.IGNORECASE)

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if match := pattern.search(line):   # koo koo kachoo
                suffix = match.group(1)
                if suffix not in with_extension:
                    with_extension[suffix] = []
                with_extension[suffix].append(line)
            else:
                without_extension.append(line)
    
    return without_extension, with_extension

def main():
    without_ex, with_ex = file_extensions("filenames.txt")
    print(f"{len(without_ex)} files with no extension")
    for ex in sorted(with_ex):
        print(ex, len(with_ex[ex]))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    return list(map(int, re.findall(r"\[\s*([+-]?\d+)\s*\]", s)))

def main():
    strings = [
        " afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx", 
        "afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx!"
        ]
    for s in strings:
        print(integers_in_brackets(s))

if __name__ == "__main__":
    main()

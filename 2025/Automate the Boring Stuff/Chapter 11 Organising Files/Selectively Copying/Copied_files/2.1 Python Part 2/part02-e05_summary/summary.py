#!/usr/bin/env python3

import sys
import math
import re

def summary(filename):
    numbers = []
    with open(filename, "r") as f:
        for line in f:
            match = re.match(r"^(-?\d+\.?\d*)\b", line)
            if match:
                numbers.append(float(match.group(1)))

    if len(numbers) == 0:
        return -1, -1, -1
    
    avg = sum(numbers) / len(numbers)
        
    if len(numbers) > 1:
        sd = math.sqrt(sum([(x - avg) ** 2 for x in numbers]) / (len(numbers) - 1))

    else:
        sd = -1

    return sum(numbers), avg, sd    

def main():
    for filename in sys.argv[1:]:
        sum_numbers, average, stddev = summary(filename)
        print(
            f"File: {filename} Sum: {sum_numbers:.6f} Average: {average:.6f} Stddev: {stddev:.6f}"
        )

if __name__ == "__main__":
    main()

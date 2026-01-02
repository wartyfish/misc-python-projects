#!/usr/bin/env python3

import pandas as pd

def main():
    data = pd.read_csv("src/municipal.tsv", sep="\t")
    
    table = pd.DataFrame(data)

    r, c = table.shape
    print(f"Shape: {r}, {c}")
    print("Columns:")
    for col in table.columns:
        print(col)


if __name__ == "__main__":
    main()

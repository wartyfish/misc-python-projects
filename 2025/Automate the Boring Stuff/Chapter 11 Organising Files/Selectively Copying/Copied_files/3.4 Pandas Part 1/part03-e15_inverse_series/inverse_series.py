#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    s2 = pd.Series(s.index, s.values)

    return s2

def main():
    s1 = pd.Series(["a", "b", "c"], index=["one", "two", "three"])

    s2 = inverse_series(s1)
    print(s1)
    print(s2)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import numpy as np
import pandas as pd

def read_series():
    indices = []
    values = []
    while True:
        ipt = input()
        if ipt == "":
            break
        else:
            try:
                i, v = ipt.split()
                indices.append(i)
                values.append(v)
            except:
                raise Exception
    
    return pd.Series(values, indices)


def main():
    print(read_series())

if __name__ == "__main__":
    main()

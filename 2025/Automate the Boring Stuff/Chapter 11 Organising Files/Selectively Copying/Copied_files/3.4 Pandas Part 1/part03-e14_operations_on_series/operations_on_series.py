#!/usr/bin/env python3
import numpy as np
import pandas as pd

def create_series(L1, L2):
    s1 = pd.Series(L1, index=list("abc"))
    s2 = pd.Series(L2, index=list("abc"))

    return s1, s2
    
def modify_series(s1, s2):
    s1["d"] = s2["b"]
    del s2["b"]

    return s1, s2

def main():
    l1 = ["dfasf", "dskfjls", "fdpsgojdfsiogvios"]
    l2 = ["asplpoxa", "xalpa", "a.sxapsx,..s,co"]

    s1, s2 = create_series(l1, l2)
    print(s1)
    
    s3, s4 = modify_series(s1, s2)
    print(s3)
    print(s4)

    result = s3+s4
    print(result)
    
if __name__ == "__main__":
    main()

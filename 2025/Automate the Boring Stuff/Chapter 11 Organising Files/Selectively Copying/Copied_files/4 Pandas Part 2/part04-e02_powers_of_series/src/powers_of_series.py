#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    cols = {n: s ** n for n in range(1, k+1)}
    
    print()
    return pd.DataFrame(cols, index=s.index)
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))

    
if __name__ == "__main__":
    main()

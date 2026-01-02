#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities_df = df.loc["Akaa":"Äänekoski"]

    print(df)
    print(municipalities_df)
    return municipalities_df

def main():
    df=municipalities_of_finland()

    c, r = df.shape

    print(f"Shape: {c}, {r}")

    for name in df.columns:

        print(name)

    

    
if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    growing_df = df[df["Population change from the previous year, %"]>0]
    return growing_df.shape[0]/df.shape[0]

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities_df = df.loc["Akaa":"Äänekoski"] 
    print(f"Proportion of growing municipalities: {100*growing_municipalities(municipalities_df):.1f}%")

if __name__ == "__main__":
    main()

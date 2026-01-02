#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities_df = df.loc["Akaa":"Äänekoski"]      
    swedish_speakers_df = municipalities_df[municipalities_df["Share of Swedish-speakers of the population, %"].astype("int") >= 5]
    df = swedish_speakers_df[swedish_speakers_df["Share of foreign citizens of the population, %"].astype("int") >= 5]

    result = df[["Population","Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
    return result

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()

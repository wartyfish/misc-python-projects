#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = load()
    result, pval = scipy.stats.pearsonr(data[:,0], data[:,2])
    return result

def correlations():
    data = load()
    
    return np.corrcoef(data[:,:4], rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()

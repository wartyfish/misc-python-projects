#!/usr/bin/env python3

import numpy as np

def diamond(n):
    #top_row_first_half = np.eye(n, dtype=int)[1:,0][::-1]
    #top_row_second_half = np.eye(n, dtype=int)[0]
    #print(np.concatenate((top_row_first_half, top_row_second_half)))
    rows = []
    for i in range(n):
        rows.append(np.concatenate((np.eye(n, dtype=int)[1:,i][::-1], np.eye(n, dtype=int)[i])))
    
    for j in range(n-2,-1,-1):
        rows.append(rows[j])

    result = np.stack((rows))
    return result
    

def main():
    print(diamond(5))

if __name__ == "__main__":
    main()

    # more "pythonic" method:
    if False:
        n = 3
        identity = np.eye(n, dtype=int)
        result_top = np.concatenate([identity[::-1], identity[:,1:]], axis=1)
        result = np.concatenate([result_top, result_top[:-1,:][::-1]])
        print(result)
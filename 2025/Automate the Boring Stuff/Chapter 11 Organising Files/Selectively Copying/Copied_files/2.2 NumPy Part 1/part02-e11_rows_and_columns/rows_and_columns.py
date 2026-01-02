#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    return [row for row in a]

def get_columns(a):
    return [col for col in a.T]

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    #main()
    a = np.array([2.1, 5.0, 17.2])
    b = np.array([-1, 3.2, 2.4])
    print(-a**2 * b)		
